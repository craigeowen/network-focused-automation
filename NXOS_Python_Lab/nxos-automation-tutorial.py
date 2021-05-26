# Filename:                     nxos-automation-tutorial.py
# Command to run the program:   python nxos-automation-tutorial.py

# Import the required dependencies
from ncclient import manager
import re
from jinja2 import Template

# Establish our NETCONF Session
nexus = manager.connect(host='192.168.128.19', port=443, username='admin', password='admin',
    allow_agent=False,
    look_for_keys=False,
    hostkey_verify=False,
    unknown_host_cb=True)


# Execute the get-config RPC
for capability in nexus.server_capabilities:
    print (capability)
