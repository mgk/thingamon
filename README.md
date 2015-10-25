[![Build Status](https://travis-ci.org/mgk/thingamon.svg?branch=master)](https://travis-ci.org/mgk/thingamon)
[![Coverage Status](https://coveralls.io/repos/mgk/thingamon/badge.svg?branch=master&service=github)](https://coveralls.io/github/mgk/thingamon?branch=master)
[![Downloads](https://img.shields.io/pypi/dm/thingamon.svg)](https://pypi.python.org/pypi/thingamon)

# thingamon

[thingamon](https://github.com/mgk/thingamon) is a package to publish MQTT messages for AWS IoT Things.

## Installation

```console
pip install thingamon
```

## Usage


```console
thingamon -h
```

## Developing

Pull requests welcome.

Getting started:

```console
make install-dev
make test
```

*Note for conda users*

If you're using [conda](http://conda.pydata.org/docs/) some tox envs may not be able to run tests. To solve this update your `PATH` so that no `python`, `python3`, etc. points at a Python managed by conda. For example on OS X:

```console
export PYTHON_ROOT="/Library/Frameworks/Python.framework/Versions/3.4"
export PATH="$PYTHON_ROOT/bin:$PATH"
make install-dev
make test
```

## License
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
