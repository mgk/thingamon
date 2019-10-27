"""
|Build Status| |Coverage Status| |Downloads|

thingamon
=========

`thingamon`_ is a library for working with AWS IoT Things using MQTT. See
`thingpin`_ for an example application that uses a Raspberry Pi as a door
sensor reporting to AWS IoT.

Installation
============

.. code::

    pip install thingamon

Usage
=====

`See Documentation for details`_

.. _See Documentation for details: https://github.com/mgk/thingamon/blob/master/README.md

.. _thingpin: https://github.com/mgk/thingpin

.. |Build Status| image:: https://travis-ci.org/mgk/thingamon.svg?branch=master
   :target: https://travis-ci.org/mgk/thingamon
.. |Coverage Status| image:: https://coveralls.io/repos/mgk/thingamon/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/mgk/thingamon?branch=master
.. |Downloads| image:: https://img.shields.io/pypi/dm/thingamon.svg
   :target: https://pypi.python.org/pypi/thingamon
"""
import os
import sys

from setuptools import setup, find_packages

setup(
    name='thingamon',
    version='1.0.0',
    description='AWS MQTT IoT Thing monitor',
    long_description=__doc__,
    url='https://github.com/mgk/thingamon/blob/master/README.md',
    author='Michael Keirnan',
    author_email='michael@keirnan.com',
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        'paho-mqtt',
        'certifi '
    ],
    tests_require=['pytest'],
    zip_safe=False,
    platforms='any',
    license='MIT',
    keywords="aws iot mqtt sensor",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Home Automation',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
