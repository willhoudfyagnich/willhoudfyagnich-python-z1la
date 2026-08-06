"""Utilities."""
import os,json
from datetime import datetime
def read_config(p="config.json"):
    if not os.path.exists(p):return{}
    try:
        with open(p)as f:return json.load(f)
    except:return{}
def timestamp():return datetime.now().isoformat()
