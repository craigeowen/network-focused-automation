#!/usr/bin/env python

# Filename:                     nxos-napalm-v01.py
# Command to run the program:   python3 nxos-napalm-v01.py

# Import dependencies
from napalm import get_network_driver
import json

# what cisco kit type
driver = get_network_driver('ios')
# device, username,password
device = driver('192.168.128.37', 'admin', 'admin')
device.open()
# this is the strin that does the work
print(json.dumps(device.get_facts(), indent=2))
device.close()
