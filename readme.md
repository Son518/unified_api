
[![N|Solid](https://github.com/agilecrm/unified2/blob/develop/unified/static/unified.png)](https://unified.ly)

| Build status | Production | 
|--|--|
| 1 | [![TEST-SUITE](https://github.com/agilecrm/unified2/actions/workflows/test-suite.yml/badge.svg?branch=develop)](https://github.com/agilecrm/unified2/actions/workflows/test-suite.yml) |



# Unified API App
This app will run as 

# Build and Test

> For development purpose run

    python run-in-local.py

> For production

generate  binary package (output will be in dist folder)

    python3 setup.py bdist_wheel

install it in remote system

    pip install unified2-1.0.0-py3-none-any.whl

run the server port 8080 default

    waitress-serve unified2:unified2

run the server in different port

    waitress-serve --listen=*:8081 unified2:unified2

test it at

    http://127.0.0.1:8080/_version 