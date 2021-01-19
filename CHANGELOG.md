# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

### Added

### Fixed

### Removed

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
