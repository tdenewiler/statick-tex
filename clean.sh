#!/bin/bash

rm -rf build/ dist/ .tox/ output-py* statick_output/* */*.egg-info
find . -name __pycache__ | xargs rm -rf
find . -name \*.pyc | xargs rm -f
