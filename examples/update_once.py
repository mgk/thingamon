#!/usr/bin/env python

"""Update the state of a thing once.

To use, follow the AWS IoT getting started guide and create a Thing.

  https://docs.aws.amazon.com/iot/latest/developerguide/iot-quickstart.html

You should have the following files:
  cert.pem - cert from AWS create-keys-and-certificate
  thing-private-key.pem - private key from AWS create-keys-and-certificate

Also take note of your specific AWS MQTT endpoint.

You do not need to download a root certificate as thingamon uses
certifi bundled certs by default.

Usage:

   update_once <AWS_ENDPOINT> <NAME_OF_THING> <MOOD>

For example:

   update_once B16HM459S4T9I0.iot.us-east-1.amazonaws.com foo happy

Then go into the AWS IoT console and see if your thing's state has been
updated.
"""

import sys
from thingamon import Client, Thing
import time

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('usage: update_once <AWS_ENDPOINT> <NAME_OF_THING> <MOOD>')
        sys.exit()

    host = sys.argv[1]
    name = sys.argv[2]
    mood = sys.argv[3]

    client = Client(host,
                    client_cert_filename='cert.pem',
                    private_key_filename='thing-private-key.pem',
                    log_mqtt=True)
    thing = Thing(name, client)
    thing.publish_state({'mood': mood})

    # thingamon uses MQTT in async mode, so here we wait a bit
    # for the message to get sent. Normal long running apps don't need
    # to do this except in their exit handlers.
    # Adjust the time as needed.
    time.sleep(3)
