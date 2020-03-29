"""Unit tests for the TeX discovery plugin."""
import contextlib
import os

from yapsy.PluginManager import PluginManager

import statick_tool
from statick_tool.discovery_plugin import DiscoveryPlugin
from statick_tool.exceptions import Exceptions
from statick_tool.package import Package
from statick_tool.plugins.discovery.tex_discovery_plugin import TexDiscoveryPlugin


# From https://stackoverflow.com/questions/2059482/python-temporarily-modify-the-current-processs-environment
@contextlib.contextmanager
def modified_environ(*remove, **update):
    """
    Temporarily updates the ``os.environ`` dictionary in-place.

    The ``os.environ`` dictionary is updated in-place so that the modification
    is sure to work in all situations.

    :param remove: Environment variables to remove.
    :param update: Dictionary of environment variables and values to add/update.
    """
    env = os.environ
    update = update or {}
    remove = remove or []

    # List of environment variables being updated or removed.
    stomped = (set(update.keys()) | set(remove)) & set(env.keys())
    # Environment variables and values to restore on exit.
    update_after = {k: env[k] for k in stomped}
    # Environment variables and values to remove on exit.
    remove_after = frozenset(k for k in update if k not in env)

    try:
        env.update(update)
        [env.pop(k, None) for k in remove]
        yield
    finally:
        env.update(update_after)
        [env.pop(k) for k in remove_after]


def test_tex_discovery_plugin_found():
    """Test that the plugin manager finds the TeX discovery plugin."""
    manager = PluginManager()
    # Get the path to statick_tool/__init__.py, get the directory part, and
    # add 'plugins' to that to get the standard plugins dir
    manager.setPluginPlaces(
        [os.path.join(os.path.dirname(statick_tool.__file__), "plugins")]
    )
    manager.setCategoriesFilter(
        {"Discovery": DiscoveryPlugin,}
    )
    manager.collectPlugins()
    # Verify that a plugin's get_name() function returns "tex"
    assert any(
        plugin_info.plugin_object.get_name() == "tex"
        for plugin_info in manager.getPluginsOfCategory("Discovery")
    )
    # While we're at it, verify that a plugin is named C Discovery Plugin
    assert any(
        plugin_info.name == "TeX Discovery Plugin"
        for plugin_info in manager.getPluginsOfCategory("Discovery")
    )


def test_tex_discovery_plugin_scan_valid():
    """Test that the TeX discovery plugin finds valid TeX source and bib files."""
    package = Package(
        "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
    )
    tdp = TexDiscoveryPlugin()
    tdp.scan(package, "level")
    expected = ["test.tex", "test.bib", os.path.join("ignore_this/ignoreme.tex")]
    if tdp.file_command_exists():
        expected += ["oddextensiontex.source"]
    # We have to add the path to each of the above...yuck
    expected_fullpath = [os.path.join(package.path, filename) for filename in expected]
    # Neat trick to verify that two unordered lists are the same
    assert set(package["tex"]) == set(expected_fullpath)


def test_tex_discovery_plugin_scan_invalid():
    """Test that the TeX discovery plugin doesn't find non-TeX files."""
    package = Package(
        "invalid_package", os.path.join(os.path.dirname(__file__), "invalid_package")
    )
    tdp = TexDiscoveryPlugin()
    tdp.scan(package, "level")
    assert not package["tex"]


def test_tex_discovery_plugin_scan_exceptions():
    """Test that the tex discovery plugin properly respects exceptions."""
    tdp = TexDiscoveryPlugin()
    package = Package(
        "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
    )
    exceptions = Exceptions(os.path.join(os.path.dirname(__file__), "exceptions.yaml"))
    tdp.scan(package, "level", exceptions)
    expected_src = ["test.tex", "test.bib", "oddextensiontex.source"]
    # We have to add the path to each of the above...yuck
    expected_src_fullpath = [
        os.path.join(package.path, filename) for filename in expected_src
    ]
    # Neat trick to verify that two unordered lists are the same
    assert set(package["tex"]) == set(expected_src_fullpath)


def test_tex_discovery_plugin_no_file_cmd():
    """
    Test when file command does not exist.

    Test that files are not discovered with file command output if file
    command does not exist.
    """
    with modified_environ(PATH=""):
        tdp = TexDiscoveryPlugin()
        package = Package(
            "valid_package", os.path.join(os.path.dirname(__file__), "valid_package")
        )
        tdp.scan(package, "level")
        expected = ["test.tex", "test.bib", os.path.join("ignore_this", "ignoreme.tex")]
        # We have to add the path to each of the above...yuck
        expected_fullpath = [
            os.path.join(package.path, filename) for filename in expected
        ]
        # Neat trick to verify that two unordered lists are the same
        assert set(package["tex"]) == set(expected_fullpath)
