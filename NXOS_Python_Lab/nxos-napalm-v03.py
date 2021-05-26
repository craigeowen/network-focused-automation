#!/usr/bin/env python

# Filename:                     nxos-napalm-v01.py
# Command to run the program:   python3 nxos-napalm-v01.py

# Import dependencies
from napalm import get_network_driver
import json

# print interface ip address
# what cisco kit type
driver = get_network_driver('ios')
# device, username,password
device = driver('192.168.128.37', 'admin', 'admin')
device.open()
# this is the strin that does the work
device.load_merge_candidate(config='interface GigabitEthernet2\n description Changed by NAPALM Again\n ip address 10.0.0.1 255.255.255.0\n no shutdown\n end\n')
print(device.compare_config())
device.commit_config()
device.close()
