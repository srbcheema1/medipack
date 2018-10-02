import pytest

from medipack.lib.time import Time

def test_get_time():
    assert Time.get_time('0:5') == '00:00:05'
