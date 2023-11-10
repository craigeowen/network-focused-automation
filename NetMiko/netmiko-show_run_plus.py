from netmiko import ConnectHandler

cisco_01 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.101",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco" # Enable password
}

connection = ConnectHandler(**cisco_01)
connection.enable() # Enable method

which_prompt = connection.find_prompt() # Find prompt method
print(which_prompt) # Print the prompt

priv_commands = ['show ip access-list', 'show ip int brief', 'show run' ]

for each_command in priv_commands:
        show_output = connection.send_command(each_command)
        print(show_output)

print('Closing Connection')
connection.disconnect()
