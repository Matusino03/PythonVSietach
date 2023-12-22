from netmiko import ConnectHandler

IP = "158.193.152.166"
PORT = 22
USER = "admin"
PASS = "Admin123"

connection = ConnectHandler(device_type="cisco_ios", host=IP, username=USER, password=PASS)
vystup = connection.send_command("sh ip int br")
print(vystup)
loop_config = ["int lo11", "ip add 1.1.1.11 255.255.255.255", "no sh"]
connection.send_config_set(loop_config)
vystup = connection.connection.send_command("sh ip int br")
print(vystup)