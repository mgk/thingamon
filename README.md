[![Build Status](https://travis-ci.org/mgk/thingamon.svg?branch=master)](https://travis-ci.org/mgk/thingamon)
[![Coverage Status](https://coveralls.io/repos/mgk/thingamon/badge.svg?branch=master&service=github)](https://coveralls.io/github/mgk/thingamon?branch=master)
[![Downloads](https://img.shields.io/pypi/dm/thingamon.svg)](https://pypi.python.org/pypi/thingamon)

# thingamon

[thingamon](https://github.com/mgk/thingamon) is a library to publish [MQTT](http://mqtt.org/) messages for [AWS IoT](https://aws.amazon.com/iot/) Things.

See [thingpin](https://github.com/mgk/thingpin) for an application example: it is a Raspberry Pi door sensor.

## Getting Started

You'll need an AWS account with IoT enabled. Run through the AWS IoT quickstart to create and test a sample thing. The setup may feel a little cumbersome, but the instructions work if followed closely.

Once setup you use an x.509 certificate to authenticate your thing: no HTTP, AWS access keys or event AWS SDKS are needed for your Thing to operate.

## Installation

```console
pip install thingamon
```

## Package Details

There is a [example](examples) of how to update a Thing's state. More on the way.

This package is a work in progress. The design of thingamon includes two classes:

  + `Client` - manages the MQTT connection to the AWS IoT server (aka message broker)
  + `Thing` - representation of an AWS IoT thing that can publish updates

## TODO

  + document async MQTT setup and threading
  + talk about AWS's topic namespace and IoT approach
  + complete app example
  + maybe use [certifi](http://docs.python-requests.org/en/latest/user/advanced/#ca-certificates) like python requests does

## SSL notes

### TLS 1.2 required
Like many servers AWS IoT requires TLS 1.2 SSL connections. This means you need a version of python that is uses openssl >= 1.0.1. To check your python SSL version:

```
python -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

To double check that TLS 1.2 works in your python:

```
python -c "import ssl; v = ssl.PROTOCOL_TLSv1_2; print('Yay')"
```

Yay means you're good. An `AttributeError` means you need to update your python's ssl. Some options:

  + [Anaconda](https://www.continuum.io/downloads) - has a ton of bundled packages

  + [miniconda](http://conda.pydata.org/miniconda.html) - Anaconda without all the packages

  + on a Mac install `openssl` and `python` with [Homebrew](http://brew.sh)

  + Google "python openssl version TLS"

### Root CA Certificates

Unlike web browsers Python ssl does not bundle a set of root SSL certificates. thingamon uses the [certifi](https://certifi.io) root CA file by default. Keep your Things secure by keeping your certifi package up to date. Sign up for email notifications when the Certifi Trust Database is updated.

## Developing

Pull requests welcome.

Getting started:

```console
make install-dev
make test
```

*Note for conda users*

If you're using [conda](http://conda.pydata.org/docs/) some tox envs may not be able to run tests. To solve this update your `PATH` so that no `python`, `python3`, etc. points at a Python managed by conda.

On OSX install `openssl`, `python`, and `python3` using [Homebrew](http://brew.sh).
Then if you are using `conda`, remove it fully from your path:

```console
export PATH=$(conda ..deactivate)
```

## License
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
