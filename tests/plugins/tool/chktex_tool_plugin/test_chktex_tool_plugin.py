"""Unit tests for the chktex plugin."""
import argparse
import os
import subprocess

import mock
import pytest
from yapsy.PluginManager import PluginManager

import statick_tool
from statick_tool.config import Config
from statick_tool.package import Package
from statick_tool.plugin_context import PluginContext
from statick_tool.plugins.tool.chktex_tool_plugin import ChktexToolPlugin
from statick_tool.resources import Resources
from statick_tool.tool_plugin import ToolPlugin


def setup_chktek_tool_plugin():
    """Initialize and return an instance of the chktex plugin."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--show-tool-output", dest="show_tool_output",
                            action="store_true", help="Show tool output")

    resources = Resources([os.path.join(os.path.dirname(statick_tool.__file__),
                                        'plugins')])
    config = Config(resources.get_file("config.yaml"))
    plugin_context = PluginContext(arg_parser.parse_args([]), resources, config)
    ctp = ChktexToolPlugin()
    ctp.set_plugin_context(plugin_context)
    return ctp


def test_chktex_tool_plugin_found():
    """Test that the plugin manager can find the chktex plugin."""
    manager = PluginManager()
    # Get the path to statick_tool/__init__.py, get the directory part, and
    # add 'plugins' to that to get the standard plugins dir
    manager.setPluginPlaces([os.path.join(os.path.dirname(statick_tool.__file__),
                                          'plugins')])
    manager.setCategoriesFilter({
        "Tool": ToolPlugin,
    })
    manager.collectPlugins()
    # Verify that a plugin's get_name() function returns "chktex"
    assert any(plugin_info.plugin_object.get_name() == 'chktex' for
               plugin_info in manager.getPluginsOfCategory("Tool"))
    # While we're at it, verify that a plugin is named Chktex Tool Plugin
    assert any(plugin_info.name == 'Chktex Tool Plugin' for
               plugin_info in manager.getPluginsOfCategory("Tool"))


def test_chktek_tool_plugin_scan_valid():
    """Integration test: Make sure the chktex output hasn't changed."""
    ctp = setup_chktex_tool_plugin()
    if not ctp.command_exists('chktex'):
        pytest.skip("Can't find chktex, unable to test chktex plugin")
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))

    package['make_targets'] = []
    package['make_targets'].append({})
    package['make_targets'][0]['src'] = [os.path.join(os.path.dirname(__file__),
                                                      'valid_package', 'test.c')]
    package['headers'] = []
    issues = ctp.scan(package, 'level')
    assert len(issues) == 1
    assert issues[0].filename == os.path.join(os.path.dirname(__file__), 'valid_package', 'test.c')
    assert issues[0].line_number == '4'
    assert issues[0].tool == 'chktex'
    assert issues[0].issue_type == 'error/uninitvar'
    assert issues[0].severity == '5'
    assert issues[0].message == "Uninitialized variable: si"


def test_chktex_tool_plugin_scan_no_files():
    """Check what happens if the plugin isn't passed any files."""
    ctp = setup_chktex_tool_plugin()
    if not ctp.command_exists('chktex'):
        pytest.skip("Can't find chktex, unable to test chktex plugin")
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))
    package['make_targets'] = []
    package['make_targets'].append({})
    package['make_targets'][0]['src'] = []
    package['headers'] = []
    issues = ctp.scan(package, 'level')
    assert len(issues) == 0


def test_chktex_tool_plugin_scan_invalid_file():
    """Check what happens if the plugin is passed an invalid file."""
    ctp = setup_chktex_tool_plugin()
    if not ctp.command_exists('chktex'):
        pytest.skip("Can't find chktex, unable to test chktex plugin")
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))

    package['make_targets'] = []
    package['make_targets'].append({})
    package['make_targets'][0]['src'] = [os.path.join(os.path.dirname(__file__),
                                                      'valid_package', 'nope.c')]
    package['headers'] = []
    # This should raise a calledProcessError, so None will be returned
    issues = ctp.scan(package, 'level')
    assert issues is None


def test_chktex_tool_plugin_parse_valid():
    """Verify that we can parse the normal output of chktex."""
    ctp = setup_chktek_tool_plugin()
    output = "[test.c:4]: (error uninitvar) Uninitialized variable: si"
    issues = ctp.parse_output(output)
    assert len(issues) == 1
    assert issues[0].filename == 'test.c'
    assert issues[0].line_number == '4'
    assert issues[0].tool == 'chktex'
    assert issues[0].issue_type == 'error/uninitvar'
    assert issues[0].severity == '5'
    assert issues[0].message == "Uninitialized variable: si"


def test_chktex_tool_plugin_parse_invalid():
    """Verify that we can parse the normal output of chktex."""
    ctp = setup_chktex_tool_plugin()
    output = "invalid text"
    issues = ctp.parse_output(output)
    assert not issues


def test_chktex_tool_plugin_scan_missing_fields():
    """
    Test what happens when key fields are missing from the Package argument.

    Expected result: issues is empty
    """
    ctp = setup_chktex_tool_plugin()
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))
    # Missing make_targets
    issues = ctp.scan(package, 'level')
    assert not issues


@mock.patch('statick_tool.plugins.tool.chktex_tool_plugin.subprocess.check_output')
def test_chktex_tool_plugin_scan_oserror(mock_subprocess_check_output):
    """
    Test what happens when an OSError is raised (usually means chktex doesn't exist).

    Expected result: issues is None
    """
    mock_subprocess_check_output.side_effect = OSError('mocked error')
    ctp = setup_chktex_tool_plugin()
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))
    package['make_targets'] = []
    package['make_targets'].append({})
    package['make_targets'][0]['src'] = [os.path.join(os.path.dirname(__file__),
                                                      'valid_package', 'test.c')]
    package['headers'] = []
    issues = ctp.scan(package, 'level')
    assert issues is None


def calledprocesserror_helper(*popenargs, **kwargs):
    """
    Helper for the calledprocesserror test.

    Lambdas can't raise exceptions, so this logic gets its own function.
    """
    # Workaround so that the --version check doesn't throw a CalledProcessError
    if "--version" in popenargs[0]:
        return "1.2.3"
    else:
        raise subprocess.CalledProcessError(2, '', output="mocked error")


@mock.patch('statick_tool.plugins.tool.chktex_tool_plugin.subprocess.check_output')
def test_chktex_tool_plugin_scan_calledprocesserror(mock_subprocess_check_output):
    """
    Test what happens when a CalledProcessError is raised (usually means chktex hit an error).

    Expected result: issues is None
    """
    mock_subprocess_check_output.side_effect = calledprocesserror_helper
    ctp = setup_chktex_tool_plugin()
    package = Package('valid_package', os.path.join(os.path.dirname(__file__),
                                                    'valid_package'))
    package['make_targets'] = []
    package['make_targets'].append({})
    package['make_targets'][0]['src'] = [os.path.join(os.path.dirname(__file__),
                                                      'valid_package', 'test.c')]
    package['headers'] = []
    issues = ctp.scan(package, 'level')
    assert issues is None


def test_checkforexceptions_true():
    """Test check_for_exceptions behavior where it should return True."""
    mm = mock.MagicMock()
    mm.group.side_effect = (
        lambda i: "test.c" if i == 1 else "variableScope" if i == 4 else False
    )
    assert ChktexToolPlugin.check_for_exceptions(mm)


def test_checkforexceptions_false():
    """Test check_for_exceptions behavior where it should return False."""
    mm = mock.MagicMock()
    mm.group.side_effect = (
        lambda i: "test.c" if i == 1 else "some-other-error" if i == 6 else False
    )
    assert not ChktexToolPlugin.check_for_exceptions(mm)
