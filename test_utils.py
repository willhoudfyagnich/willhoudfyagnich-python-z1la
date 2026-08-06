"""Tests."""
import os,pytest
from utils import read_config,timestamp
def test_read_missing():assert read_config("/tmp/nope.json")=={}
def test_timestamp():
    t=timestamp()
    assert"T"in t and len(t)>=19
