#!/usr/bin/env python3
"""willhoudfyagnich-python-z1la."""
import sys,argparse
from utils import timestamp
def main():
    p=argparse.ArgumentParser(description="willhoudfyagnich-python-z1la")
    p.add_argument("--version",action="version",version="1.0.0")
    p.add_argument("-v","--verbose",action="store_true")
    a=p.parse_args()
    if a.verbose:print(f"[{timestamp()}] willhoudfyagnich-python-z1la v1.0.0")
    print(f"Hello from willhoudfyagnich-python-z1la!")
    return 0
if __name__=="__main__":sys.exit(main())
