# -*- coding: utf-8 -*-

import logging
from threading import Lock
import json
import ssl
import time
import paho.mqtt.client as mqtt
import certifi
from .thing import Thing


logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S%z')
log = logging.getLogger('thingamon-client')
log.setLevel(logging.DEBUG)


class Client(object):
    """Authenticated connection to MQTT server"""

    def __init__(self, host=None, port=8883, ca_certs_filename=certifi.where(),
                 client_cert_filename=None, private_key_filename=None,
                 tls_version=ssl.PROTOCOL_TLSv1_2, log_mqtt=False):
        """Create a Client instance for MQTT communication

        Args:
            host (str): hostname of MQTT broker server
            port (int): port of MQTT broker. The default port of 8883 is used
                by AWS IoT.
            ca_certs_filename (str): name of file containing a root
                certificate. By default the currently installed
                `certi <https://certifi.io/>`_ certificate file is used.
            client_cert_filename (str): name of file containing your client
                certificate
            private_key_filename (str): name of file containing the private
                key for your client certificate. Together with the client
                certificate this is how the client authenticates itself to
                the MQTT server.
            tls_version (init): SSL protocol version to use. The default
                is currently the only version accepted by AWS IoT.
            log_mqtt (bool): if True MQTT data sent and received is logged.
        """
        self.connect_attempted = False
        self._connected = False
        self._connected_lock = Lock()
        self.host = host
        self.port = port
        self.client = mqtt.Client()
        self.client.tls_set(ca_certs=ca_certs_filename,
                            certfile=client_cert_filename,
                            keyfile=private_key_filename,
                            tls_version=tls_version)

        def on_connect(client, userdata, rc):
            self.connected = True
            log.info('MQTT connect: {}'.format(mqtt.connack_string(rc)))

        def on_disconnect(client, userdata, rc):
            self.connected = False
            log.info('MQTT disconnect: {}'.format(mqtt.connack_string(rc)))

        def on_log(client, userdata, level, buf):
            log.debug('{} {} {}'.format(userdata, level, buf))

        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        if log_mqtt:
            self.client.on_log = on_log

    @property
    def connected(self):
        with self._connected_lock:
            return self._connected

    @connected.setter
    def connected(self, value):
        with self._connected_lock:
            self._connected = value

    def connect(self):
        """Connect to MQTT server and wait for server to acknowledge"""
        if not self.connect_attempted:
            self.connect_attempted = True
            self.client.connect(self.host, port=self.port)
            self.client.loop_start()

            while not self.connected:
                log.info('waiting for MQTT connection...')
                time.sleep(1)

    def disconnect(self):
        self.client.loop_stop()

    def publish(self, topic, message):
        """Publish an MQTT message to a topic."""
        log.info('publish {}'.format(message))
        self.connect()
        self.client.publish(topic, message)
