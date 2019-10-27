#!/usr/bin/env python

"""Example script that updates the state of a thing once.

To use, follow the AWS IoT getting started guide and register a thing.

  https://docs.aws.amazon.com/iot/latest/developerguide/iot-quickstart.html

Download the certificate and private key for the Thing.

Activate the new Thing.

Add an IAM policy that allows all IoT actions to your Thing, such as:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Connect"
      ],
      "Resource": "*"
    }
  ]
}

Usage:

   update_once <AWS_ENDPOINT> <CERT> <PRIVATE-KEY> <NAME_OF_THING> <ANY-STRING>

Then go into the AWS IoT console to confirm that your Thing's state has been
updated.
"""

import sys
from thingamon import Client, Thing
import time

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('usage: update_once <AWS_ENDPOINT> <CERT> <PRIVATE-KEY> <NAME_OF_THING> <ANY-STRING>')
        sys.exit()

    host, root_ca, cert, key, name, mood = sys.argv[1:]

    client = Client(host, client_cert_filename=cert, private_key_filename=key)
    thing = Thing(name, client)
    thing.publish_state({'mood': mood})

    # thingamon uses MQTT in async mode, so here we wait a bit
    # for the message to get sent. Normal long running apps don't need
    # to do this except in their exit handlers.
    time.sleep(3)
