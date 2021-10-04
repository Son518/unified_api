#!/bin/bash
# Copyright 2020 500apps.com

BUILD_TIME=$(date "+%d-%B-%Y %H:%M:%S (UTC)")

sed -i -e "s/{BUILD_TIME}/$BUILD_TIME/" unified/modules/health-check/application.py
sed -i -e "s/{BUILD_NUMBER}/$1/" unified/modules/health-check/application.py

python3 setup.py bdist_wheel

sed -i -e "s/$BUILD_TIME/{BUILD_TIME}/" unified/modules/health-check/application.py
sed -i -e "s/$1/{BUILD_NUMBER}/" unified/modules/health-check/application.py
# find . -type d -name __pycache__ -exec rmdir {} \;
find . -name __pycache__ -exec rm -rf {} \;
rm -rf *.egg-info build