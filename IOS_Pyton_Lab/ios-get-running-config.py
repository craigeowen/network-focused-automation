# Filename:                     cisco-automation-tutorial.py
# Command to run the program:   python cisco-automation-tutorial.py

# Import the required dependencies
from ncclient import manager
from jinja2 import Template
# Establish our NETCONF Session
m = manager.connect(host='192.168.128.37', port=830, username='admin',
                    password='admin', device_params={'name': 'csr'})



# Execute the get-config RPC
result = m.get_config('running')
print(result)
