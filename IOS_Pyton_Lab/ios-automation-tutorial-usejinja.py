# Filename:                     ios-automation-tutorial-usejinja.py
# Command to run the program:   python3 ios-automation-tutorial-usejinja.py

# Import the required dependencies
from ncclient import manager
from jinja2 import Template
# Establish our NETCONF Session
m = manager.connect(host='192.168.128.37', port=830, username='admin',
                    password='admin', device_params={'name': 'csr'})

# Render our Jinja template
interface_template = Template(open('CSR_interfacev2.xml').read())
interface_rendered = interface_template.render(
  INTERFACE_INDEX='2', 
  IP_ADDRESS='10.0.0.2', 
  SUBNET_MASK='255.255.255.252'
)

# Execute the edit-config RPC
result = m.edit_config(target='running', config=interface_rendered)
print(result)

