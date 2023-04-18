# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

## Changed

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
