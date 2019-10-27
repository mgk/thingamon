[![Build Status](https://travis-ci.org/mgk/thingamon.svg?branch=master)](https://travis-ci.org/mgk/thingamon)
[![Coverage Status](https://coveralls.io/repos/mgk/thingamon/badge.svg?branch=master&service=github)](https://coveralls.io/github/mgk/thingamon?branch=master)
[![Downloads](https://img.shields.io/pypi/dm/thingamon.svg)](https://pypi.python.org/pypi/thingamon)

# thingamon
[thingamon](https://github.com/mgk/thingamon) is a library to publish [MQTT](http://mqtt.org/) messages for [AWS IoT](https://aws.amazon.com/iot/) Things.

## *Deprecation Warning: New projects should instead use the AWS SDK directly*
*Most applications are better off using the AWS SDK directly. When `thingamon` started it was a wrapper around the [Pahoo MQTT client library](https://www.eclipse.org/paho/clients/python/). At that time thingamon provided the AWS IoT boilerplate and freed the calling application from worring about the subtleties of working with asynchronous MQTT.*

*At this point the AWS IoT library itself is a wrapper around Paho that encapsulates all the AWS IoT knowledge (including all the IoT supported authentication methods). The AWS library handles all of the above concerns as well as integrating natively with the AWS IoT device shadow abstraction.*

## Overview
`thingamon` provides two abstractions:

 - **Client**: a thin wrapper around the [AWS IoT MQTT Client](https://github.com/aws/aws-iot-device-sdk-python)
 - **Thing**: representation of an IoT thing that knows how to publish its state

The related project, [thingpin](https://github.com/mgk/thingpin) is a Raspberry Pi application that uses `thingamon` to update the state of multiple things from sensor inputs (pins).

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

### TLS 1.2 required
AWS IoT requires TLS 1.2 SSL connections. This means you need a version of python that is uses openssl >= 1.0.1.
To check your python SSL version:

**TODO: put in automated test**

```
python -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

To confirm that TLS 1.2 works in your python:

```
python -c "import ssl; v = ssl.PROTOCOL_TLSv1_2; print('Yay')"
```

Yay means you're good. Otherwise you'll need to update your version of Python. Google "python openssl version TLS".

### Root CA Certificates
Root SSL certificates effectively tell SSL/HTTPS clients who to trust to verify the identity of servers. Browsers and OSes build in the root certificates. Python does not bundle root certificates.

`thingamon` uses the [certifi](https://certifi.io) for root certificates by default. You can override this to, for example use the AWS recommended root certificate downloadable from the AWS IoT dashboard.

## Developing
```console
make install-dev
make test
```

## License
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
