# Change Log
This project uses [Semantic Versioning](http://semver.org/).

##  [1.0.0](https://github.com/mgk/thingamon/releases/tag/v1.0.0) - [2019-10-27]
### Changed
- breaking change: Use AWS Python SDK instead of Paho. This also changes the `Client` constructor incompatibly.
- announce deprecation of project as AWS SDK obviates need for thingamon
- all operations are asynchronous

## [0.2.2](https://github.com/mgk/thingamon/releases/tag/v0.2.2) - [2015-11-01]

### Fixed
- #3 add Client.disconnect() method

## [0.2.1](https://github.com/mgk/thingamon/releases/tag/v0.2.1) - [2015-10-25]
### Fixed
- #2 setup dependency bug
- #1 remove need to call client.connect()

## [0.2.0](https://github.com/mgk/thingamon/releases/tag/v0.2.0) - [2015-10-25]
### Added
- [certifi](https://certifi.io) bundled root certificates ftw

## [0.1.1](https://github.com/mgk/thingamon/releases/tag/v0.1.1) - [2015-10-25]
### Fixed
- kwarg test expectation on python 2.7

## [0.0.1](https://github.com/mgk/thingamon/releases/tag/v0.0.1) - [2015-10-25]
### Added
- initial working version with example
