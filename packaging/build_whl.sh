#!/bin/bash

set -x
cd /src
rm -rf build dist minty.egg-info
cd minty/mstplib
make clean_build
cd /src

/opt/_internal/cpython-2.7.15-ucs4/bin/python setup.py bdist_wheel
/opt/_internal/cpython-2.7.15-ucs2/bin/python setup.py bdist_wheel
/opt/_internal/cpython-2.7.15-ucs2/bin/python setup.py sdist
