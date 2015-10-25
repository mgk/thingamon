import json


class Thing(object):
    """An IoT Thing"""

    def __init__(self, name, client=None):
        """Create a Thing.

        Args:
            name (str): name of the Thing. This corresponds to the
                AWS IoT Thing name.
            client (str): MQTT client connection to use. This can be set
                anytime before publishing Thing messages to the server.
        """
        self._name = name
        self.client = client
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def topic(self):
        return '$aws/things/{}/shadow/update'.format(self.name)

    def publish_state(self, state):
        """Publish thing state to AWS IoT.

        Args:
            state (dict): object state. Must be JSON serializable (i.e., not
                have circular references).
        """
        message = json.dumps({'state': {'reported': state}})
        self.client.publish(self.topic, message)
        self._state = state

    @property
    def state(self):
        """Most recently published state"""
        return self._state
