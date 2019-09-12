# Statick TeX/LaTeX Plugins

| Service | Status |
| ------- | ------ |
| Build   | [![Travis-CI](https://api.travis-ci.org/tdenewiler/statick-tex.svg?branch=master)](https://travis-ci.org/tdenewiler/statick-tex/branches) |
| PyPI    | [![PyPI version](https://badge.fury.io/py/statick-tex.svg)](https://badge.fury.io/py/statick-tex) |
| Codecov | [![Codecov](https://codecov.io/gh/tdenewiler/statick-tex/branch/master/graphs/badge.svg)](https://codecov.io/gh/tdenewiler/statick-tex/) |

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

If you have statick, statick-tex, and a latex project laid out as follows:

  - src
    - statick
    - statick-output
    - statick-tex
    - latex-project

Then the following commands run in `src` would scan your TeX project using the default Statick configuration:

    ./statick/statick latex-project statick-output --profile tex-profile.yaml

If your LaTeX project had its own custom Statick configuration it could be stored under `latex-project/statick_config`.
In that case you would use the following command in `src` to invoke your custom Statick configuration:

    ./statick/statick latex-project statick-output --user-paths ./latex-project/statick_config --profile tex-profile.yaml

If statick and statick-tex are installed (either via local install commands or from pip) then you do not need to give
the entire path to `statick`.

## Tests and Contributing

If you write a new feature for Statick or are fixing a bug, you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify future regressions) if you can add a small unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not introduced any regressions or violated any code style guidelines.
