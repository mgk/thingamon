import pytest
import json
import ssl
import unittest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from thingamon import Client

class TestSsl(unittest.TestCase):
    def test_ssl_protocol(self):
        self.assertIsNotNone(getattr(ssl, 'PROTOCOL_TLSv1_2', None),
            "TLS v1.2 (openssl >= 1.0.1) is required by AWS IoT")

@patch('paho.mqtt.client.Client', autospec=True)
def test_tls(MockMqttClient):
    client = Client(ca_certs_filename='ca_certs_filename',
                    client_cert_filename='client_cert_filename',
                    private_key_filename='private_key_filename')
    MockMqttClient.return_value.tls_set.assert_called_once_with(
        ca_certs='ca_certs_filename',
        certfile='client_cert_filename',
        keyfile='private_key_filename',
        tls_version=ssl.PROTOCOL_TLSv1_2
        )

@patch('paho.mqtt.client.Client', autospec=True)
def test_connect(MockMqttClient):
    client = Client('host')

    # TODO: test threading properly, or expose Client.on_connect
    def on_connect(*args, **kwargs):
        client._connected = True
    MockMqttClient.return_value.connect.side_effect = on_connect

    client.connect()
    MockMqttClient.return_value.connect.assert_called_once_with(
        'host', port=8883)

@patch('paho.mqtt.client.Client', autospec=True)
def test_publish(MockMqttClient):
    client = Client('host')
    def on_connect(*args, **kwargs):
        client._connected = True
    MockMqttClient.return_value.connect.side_effect = on_connect
    client.connect()
    client.publish('msg', 'topic')
    MockMqttClient.return_value.publish.assert_called_once_with('msg', 'topic')

@patch('paho.mqtt.client.Client', autospec=True)
def test_publish_shoul_auto_connect(MockMqttClient):
    client = Client('host')
    def on_connect(*args, **kwargs):
        client._connected = True
    MockMqttClient.return_value.connect.side_effect = on_connect
    client.publish('msg', 'topic')
    MockMqttClient.return_value.connect.assert_called_once_with(
        'host', port=8883)
    MockMqttClient.return_value.publish.assert_called_once_with('msg', 'topic')
