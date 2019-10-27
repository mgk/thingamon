# -*- coding: utf-8 -*-

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient, DROP_OLDEST
from AWSIoTPythonSDK.core.protocol import paho
import logging
from threading import Lock
import json
import ssl
import time
import certifi
from .thing import Thing


logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S%z')
log = logging.getLogger('thingamon-client')
log.setLevel(logging.DEBUG)


class Client(object):
    """AWS IoT MQTT client.

    Thin wrapper around AWSIoTMQTTClient that publishes MQTT messages
    asynchornously.
    """

    def __init__(self,
                 host=None,
                 port=8883,
                 root_ca_filename=certifi.where(),
                 client_cert_filename=None,
                 private_key_filename=None,
                 log_mqtt=True):
        """Create a Client instance for MQTT communication.

        Args:
            host (str): hostname of MQTT broker server
            port (int): port of MQTT broker. The default port of 8883 is used
                by AWS IoT.
            root_ca_filename (str): name of file containing a root
                certificate. By default the currently installed
                `certi <https://certifi.io/>`_ certificate file is used.
            client_cert_filename (str): name of file containing your client
                certificate
            private_key_filename (str): name of file containing the private
                key for your client certificate. Together with the client
                certificate this is how the client authenticates itself to
                the MQTT server.
            log_mqtt (bool): if True MQTT data sent and received is logged.
        """
        self.connect_attempted = False
        self._connected = False
        self._connected_lock = Lock()

        self.client = AWSIoTMQTTClient('thingamon')
        self.client.disableMetricsCollection()
        self.client.configureEndpoint(host, port)
        self.client.configureCredentials(root_ca_filename,
                                         private_key_filename,
                                         client_cert_filename)
        self.client.configureOfflinePublishQueueing(1000, DROP_OLDEST)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)

        if log_mqtt:
            logging.getLogger("AWSIoTPythonSDK.core").setLevel(logging.DEBUG)

    @property
    def connected(self):
        with self._connected_lock:
            return self._connected

    @connected.setter
    def connected(self, value):
        with self._connected_lock:
            self._connected = value

    def connect(self):
        """Connect to MQTT server"""
        if not self.connect_attempted:
            self.connect_attempted = True
            self.client.connectAsync()

    def disconnect(self):
        self.client.disconnectAsync()

    def publish(self, topic, message, qos=1):
        """Publish an MQTT message to a topic."""
        self.connect()
        self.client.publishAsync(topic, message, qos)
        log.info('publish({}, qos={} msg={})'.format(topic, qos, message))
