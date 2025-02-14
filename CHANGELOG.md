# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## v0.5.0 - 2025-02-07

This set of plugins was merged into the main [Statick] repository and Python package.
All future development will happen in that repository.

### Updated

- The Statick dependency was pinned to lower than version 0.12.
  - This will ensure these plugins are not installed in the same space as the main `statick` package.
    Having both packages installed would cause conflicts between plugins.

## v0.4.0 - 2025-01-20

### Added

- Support for Python 3.12 and 3.13.
- Use of `pyproject.toml` instead of `setup.py` and `requirements.txt`.
- Supports new plugin discovery mechanism for the main Statick tool.
  - Switched from yapsy to setuptools for plugin mechanism. (sscpac/statick#508)

### Changed

- Disabled code coverage requirements in CI for now.
  - Unable to get line coverage working with new plugin mechanism.
    Unit tests still work to find problems.
- Rename plugin modules so they are shorter and less redundant.
- Upgrade statick-action from 0.1.0 to 0.9.2.

### Removed

- No longer support Python 3.8.

## v0.3.5 - 2023-06-21

### Changed

- Unpin documentation requirement for sphinx.
  Was pinned at `1.7.9` but that version is missing support for flags used by some GitHub actions.
  Current version is `4.4.0`.

## v0.3.4 - 2023-06-21

### Fixed

- Revert version used for sphinx-action to perform linting of Sphinx files.

## v0.3.3 - 2023-06-21

### Changed

- Cleanup supported versions. (#77)
  - Drop support for Python 3.7 due to end-of-life on 27 June 2023.
  - Run deployment actions on ubuntu-latest.
  - Make setup.py and tox.ini consistent with supported versions.
  - Update versions of actions to use only tags.

## v0.3.2 - 2023-06-21

### Added

- Update Read the Docs to required [v2 configuration file](https://blog.readthedocs.com/migrate-configuration-v2/).

### Changed

- Updated tool plugins to match new structure introduced in sscpac/statick#423.
- Update `inherits_from` usage in configuration file to match new list format.

### Fixed

- Process all Python source files at once with pylint tool plugin, instead of one pylint run per file. (#73)
- Pin flake8<5 and pycodestyle<2.9.0 until <https://github.com/tholo/pytest-flake8/issues/87> is fixed.

### Removed

- Removed deprecated pypi package [codecov](https://github.com/codecov/codecov-python) from Tox configuration. (#74)
  Discussion at: <https://community.codecov.com/t/codecov-yanked-from-pypi-all-versions/4259>.

## v0.3.1 - 2022-10-10

### Changed

- Updated tool plugins to match new structure introduced in sscpac/statick#423.
- Use Statick action v0.0.2 instead of main.

### Fixed

- Pin flake8<5 and pycodestyle<2.9.0 until <https://github.com/tholo/pytest-flake8/issues/87> is fixed.

## v0.3.0 - 2022-01-04

### Removed

- Drop support for Python 3.6 due to end-of-life of that distribution.
  See <https://endoflife.date/python>.
  To continue using Statick with Python 3.6 [pin the version](https://pip.pypa.io/en/stable/user_guide/)
  used to the `0.2` tags.
  An example is at the discussion at <https://github.com/sscpac/statick/discussions/376>.

## v0.2.5 - 2022-01-04

### Added

- Add Python 3.10 support.
- Add scheduled weekly workflow run.
- Add ability to manually trigger workflow run for any branch.
- Switch type hints from comment style to inline style.
- Switch workflow testing from local installed Statick to
  [Statick GitHub Action](https://github.com/sscpac/statick-action).

### Fixed

- Fix pylint warnings related to using the open call without specifying an encoding.
- Switch to Pythonic way of checking that a variable is not equal to more than one value (fixes pylint warning).
- Use quotes for version numbers in YAML to avoid truncating trailing zeros.
- Switch use of codecov-action from v1 to v2 for increased stability when uploading reports.
- Do not fail workflow if Codecov results are not uploaded successfully.
  That step is too brittle and fails intermittently.

### Removed

- Remove support for Ubuntu 16.04 and Python 3.5.

## v0.2.4 - 2021-01-19

### Changed

- Convert use of print() and show tool output flags to the built-in Python logging module.

## v0.2.3 - 2020-12-22

### Added

- Python 3.9 is now supported and tested.
- Use new discovery plugin cache of file information instead of walking the package directory structure
  independently.
  Provides large speed improvement in discovery phase (about 3x faster). (Alexander Xydes, @xydesa)

## v0.2.2 - 2020-10-26

### Added

- Documentation is generated and published to GitHub Pages on new tags.
- Tests are run on Ubuntu 16.04, 18.04, and 20.04 in addition to previous operating systems.
- The `--strict` flag is used for Mypy.
- Markdown linting using statick-md.

### Fixed

- Tox configuration updated so that unit tests continue working.
- Limit discovery plugins that are run on default levels to speed up Statick.

## v0.2.1 - 2020-03-29

### Added

- Type hints that are verified using mypy.
- Unit tests to exercise case where `file` command does not exist.
  This increased code coverage to 100%.
- Running tests on Ubuntu, MacOS, and Windows via Github Actions.
  This includes publishing results to Codecov.

### Changed

- Switched from Travis CI to Github Actions.
- Formatted all code with black.
  Checking on all pull requests via Github Actions.

### Removed

- Dropped support for Python 2.7 and Python 3.4.

## v0.2.0 - 2019-11-13

### Changed

- Switched from ad-hoc layout to source layout.
