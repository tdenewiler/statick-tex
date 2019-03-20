# Statick TeX/LaTeX Plugins

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover TeX/LaTeX files and perform
static analysis on those files.

If you have statick, statick-tex, and a latex project laid out as follows:

  - src
    - statick
    - statick-output
    - statick-tex
    - latex-project

Then the following commands run in `src` would scan your latex project:

    ./statick/statick latex-project statick-output --user-paths ./statick-tex/statick_tool --profile tex-profile.yaml

If statick and statick-tex are installed (either via local install commands or from pip) then you do not need to give
the entire path to `statick` and `statick-tex/statick_tool`.
