import pytest
import json

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from thingamon import Thing


def test_init():
    t = Thing('light1')

    assert t.name == 'light1'
    assert t.topic == '$aws/things/light1/shadow/update'

def test_publish_state():
    client = Mock()
    thing = Thing('light', client)
    on_state = {'on': True}
    thing.publish_state(on_state)

    expected_message = json.dumps({'state': {'reported': on_state}})
    client.publish.assert_called_once_with(thing.topic, expected_message)
    assert thing.state == on_state
