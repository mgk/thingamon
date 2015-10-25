import pytest

try:
    from unittest.mock import patch, Mock
except ImportError:
    from mock import patch, Mock

from thingamon import Thing


def test_class_exists():
    t = Thing()
    assert True
