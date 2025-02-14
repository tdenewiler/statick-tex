# Statick TeX/LaTeX Plugins

![Unit Tests](https://github.com/tdenewiler/statick-tex/workflows/Unit%20Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/statick-tex.svg)](https://badge.fury.io/py/statick-tex)
[![Codecov](https://codecov.io/gh/tdenewiler/statick-tex/branch/master/graphs/badge.svg)](https://codecov.io/gh/tdenewiler/statick-tex/)
![Python Versions](https://img.shields.io/pypi/pyversions/statick-tex.svg)
![License](https://img.shields.io/pypi/l/statick-tex.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-tex.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-tex.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-tex.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover TeX/LaTeX files and perform
static analysis on those files.

The current plugins will discover TeX/LaTeX files in a project and can be configured to check those files using
[ChkTeX](https://ctan.org/pkg/chktex) and [LaCheck](https://ctan.org/pkg/lacheck).
Custom exceptions can be applied the same way they are with
[Statick exceptions](https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml).

## Deprecated

This set of plugins was merged into the main [Statick] repository and Python package.
All future development will happen in that repository.

## Installation

The recommended method to install these Statick plugins is via pip:

    pip install statick-tex

You can also clone the repository and use it locally.

To use the _tool_ plugins you need to install the tools they are based on.
For Ubuntu Linux you would use

    apt install chktex lacheck

## Usage

### Pip Install

The most common usage is to use statick and statick-tex from pip.
In that case your directory structure will look like the following:

- doc
  - project
  - output

To run with the default configuration for the statick-tex tools use:

    statick project/ --output-directory output/ --profile tex-profile.yaml

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the project, such that the directory structure is:

- doc
  - project
    - statick-config
      - rsc
        - exceptions.yaml
  - output

For this setup you will run the following:

    statick project/ --output-directory output/ --user-paths project/statick-config/ --profile tex-profile.yaml

### Source Install and Custom Configuration

The last type of setup will be to have all of the tools available from cloning repositories, not installing from pip.
The directory structure will look like:

- doc
  - project
    - statick-config
      - rsc
        - exceptions.yaml
  - output
  - statick
  - statick-tex

Using the example where we want to override the default exceptions with custom ones in the project, the command
to run would be:

    ./statick/statick project/ --output-directory output --user-paths statick-tex,project/statick-config --profile tex-profile.yaml

## Tests and Contributing

If you write a new feature for Statick or are fixing a bug, you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify future regressions) if you can add a small
unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not introduced any regressions or violated any code
style guidelines.

### Mypy

Statick uses [mypy](http://mypy-lang.org/) to check that type hints are being followed properly.
Type hints are described in [PEP 484](https://www.python.org/dev/peps/pep-0484/) and allow for static typing in Python.
To determine if proper types are being used in Statick plugins the following command will show any errors, and create several
types of reports that can be viewed with a text editor or web browser.

    pip install mypy
    mkdir report
    mypy --ignore-missing-imports --strict --html-report report/ --txt-report report src/

It is hoped that in the future we will generate coverage reports from mypy and use those to check for regressions.

### Formatting

Statick code is formatted using [black](https://github.com/psf/black).
To fix locally use

    pip install black
    black src
