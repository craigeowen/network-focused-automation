# Filename:                     nxos-get-running.py
# Command to run the program:   python nxos-get-running.py


# Import the required dependencies
from ncclient import manager
from jinja2 import Template
# Establish our NETCONF Session
m = manager.connect(host='192.168.128.19', port=830, username='admin',
                    password='admin', device_params={'name': 'nexus'})



# Execute the get-config RPC
result = m.get_config('running')
print(result)
