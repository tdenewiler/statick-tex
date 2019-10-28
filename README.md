# Statick TeX/LaTeX Plugins

| Service   | Status |
| --------- | ------ |
| Build     | [![Travis-CI](https://api.travis-ci.org/tdenewiler/statick-tex.svg?branch=master)](https://travis-ci.org/tdenewiler/statick-tex/branches) |
| PyPI      | [![PyPI version](https://badge.fury.io/py/statick-tex.svg)](https://badge.fury.io/py/statick-tex) |
| Codecov   | [![Codecov](https://codecov.io/gh/tdenewiler/statick-tex/branch/master/graphs/badge.svg)](https://codecov.io/gh/tdenewiler/statick-tex/) |
| Coveralls | [![Coverage Status](https://coveralls.io/repos/github/tdenewiler/statick-tex/badge.svg?branch=master)](https://coveralls.io/github/tdenewiler/statick-tex?branch=master) |

![Python Versions](https://img.shields.io/pypi/pyversions/statick-tex.svg)
![License](https://img.shields.io/pypi/l/statick-tex.svg)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-tex.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-tex.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-tex.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover TeX/LaTeX files and perform
static analysis on those files.

The current plugins will discover TeX/LaTeX files in a project and can be configured to check those files using
[ChkTeX](https://ctan.org/pkg/chktex) and [LaCheck](https://ctan.org/pkg/lacheck).
Custom exceptions can be applied the same way they are with
[Statick exceptions](https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml).

## Installation

The recommended method to install these Statick plugins is via pip:

    pip install statick-tex

You can also clone the repository and use it locally.

## Usage

### Pip Install

The most common usage is to use statick and statick-tex from pip.
In that case your directory structure will look like the following:

  - doc
    - latex-project
    - statick-output

To run with the default configuration for the statick-tex tools use:

    statick latex-project/ statick-output/ --profile tex-profile.yaml

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the latex-project, such that the directory structure is:

  - doc
    - latex-project
      - statick-config
        - rsc
          - exceptions.yaml
    - statick-output

For this setup you will run the following:

    statick latex-project/ statick-output/ --user-paths latex-project/statick-config/ --profile tex-profile.yaml

### Source Install and Custom Configuration

The last type of setup will be to have all of the tools available from cloning repositories, not installing from pip.
The directory structure will look like:

  - doc
    - latex-project
      - statick-config
        - rsc
          - exceptions.yaml
    - statick-output
    - statick
    - statick-tex

Using the example where we want to override the default exceptions with custom ones in the latex-project, the command to run would be:

    ./statick/statick latex-project/ statick-output/ --user-paths statick-tex/,latex-project/statick-config/ --profile tex-profile.yaml

## Tests and Contributing

If you write a new feature for Statick or are fixing a bug, you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify future regressions) if you can add a small
unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not introduced any regressions or violated any code style guidelines.
