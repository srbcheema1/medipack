import pytest

from medipack.lib.time import Time

def test_get_time():
    assert Time.get_time('0:5') == '00:00:05'

def test_relative_time():
    assert Time.get_relative_time('0:5','0:15') == '00:00:10'
