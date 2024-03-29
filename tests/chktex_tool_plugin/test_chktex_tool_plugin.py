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


def setup_chktex_tool_plugin():
    """Initialize and return an instance of the chktex plugin."""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--show-tool-output",
        dest="show_tool_output",
        action="store_false",
        help="Show tool output",
    )

    resources = Resources(
        [os.path.join(os.path.dirname(statick_tool.__file__), "plugins")]
    )
    config = Config(resources.get_file("config.yaml"))
    plugin_context = PluginContext(arg_parser.parse_args([]), resources, config)
    plugin_context.args.output_directory = os.path.dirname(__file__)
    ctp = ChktexToolPlugin()
    ctp.set_plugin_context(plugin_context)
    return ctp


def test_chktex_tool_plugin_found():
    """Test that the plugin manager can find the chktex plugin."""
    manager = PluginManager()
    # Get the path to statick_tool/__init__.py, get the directory part, and
    # add 'plugins' to that to get the standard plugins dir
    manager.setPluginPlaces(
        [os.path.join(os.path.dirname(statick_tool.__file__), "plugins")]
    )
    manager.setCategoriesFilter(
        {
            "Tool": ToolPlugin,
        }
    )
    manager.collectPlugins()
    # Verify that a plugin's get_name() function returns "chktex"
    assert any(
        plugin_info.plugin_object.get_name() == "chktex"
        for plugin_info in manager.getPluginsOfCategory("Tool")
    )
    # While we're at it, verify that a plugin is named Chktex Tool Plugin
    assert any(
        plugin_info.name == "Chktex Tool Plugin"
        for plugin_info in manager.getPluginsOfCategory("Tool")
    )


def test_chktex_tool_plugin_scan_valid():
    """Integration test: Make sure the chktex output hasn't changed."""
    cttp = setup_chktex_tool_plugin()
    if not cttp.command_exists("chktex"):
        pytest.skip("Missing chktex executable.")
    package = Package(
        "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
    )
    package["tex"] = [
        os.path.join(os.path.dirname(__file__), "valid_package", "test.tex")
    ]
    issues = cttp.scan(package, "level")
    # We expect to have length of dash warning.
    assert len(issues) == 1


def test_chktex_tool_plugin_parse_valid():
    """Verify that we can parse the normal output of chktex."""
    cttp = setup_chktex_tool_plugin()
    output = (
        "a\nb\nc\nd\nWarning 8 in /e line 13: Wrong length of dash may have been used.\n"
        "Adding intentional chktex warning -- for dashes --- should have three of them.\n^^\n"
    )
    issues = cttp.parse_output([output])
    assert len(issues) == 1
    assert issues[0].line_number == "13"
    assert issues[0].tool == "chktex"
    assert issues[0].issue_type == "8"
    assert issues[0].severity == "3"
    assert issues[0].message == "Wrong length of dash may have been used."


def test_chktex_tool_plugin_parse_invalid():
    """Verify that we can parse the normal output of chktex."""
    cttp = setup_chktex_tool_plugin()
    output = "invalid text"
    issues = cttp.parse_output(output)
    assert not issues


@mock.patch("statick_tool.plugins.tool.chktex_tool_plugin.subprocess.check_output")
def test_chktex_tool_plugin_scan_calledprocesserror(mock_subprocess_check_output):
    """
    Test what happens when a CalledProcessError is raised (usually means chktex hit an error).

    Expected result: issues is None
    """
    mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(
        0, "", output="mocked error"
    )
    cttp = setup_chktex_tool_plugin()
    package = Package(
        "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
    )
    package["tex"] = [
        os.path.join(os.path.dirname(__file__), "valid_package", "test.tex")
    ]
    issues = cttp.scan(package, "level")
    assert issues is None

    mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(
        1, "", output="mocked error"
    )
    issues = cttp.scan(package, "level")
    assert not issues


@mock.patch("statick_tool.plugins.tool.chktex_tool_plugin.subprocess.check_output")
def test_chktex_tool_plugin_scan_oserror(mock_subprocess_check_output):
    """
    Test what happens when an OSError is raised (usually means chktex doesn't exist).

    Expected result: issues is None
    """
    mock_subprocess_check_output.side_effect = OSError("mocked error")
    cttp = setup_chktex_tool_plugin()
    package = Package(
        "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
    )
    package["tex"] = [
        os.path.join(os.path.dirname(__file__), "valid_package", "test.tex")
    ]
    issues = cttp.scan(package, "level")
    assert issues is None
