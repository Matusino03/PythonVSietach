import paramiko
from paramiko.client import AutoAddPolicy

IP = "158.193.152.167"
PORT = 22
USER = "admin"
PASS = "Admin123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(hostname=IP, port=PORT, username=USER, password=PASS, look_for_keys=False)

(stdin, stdout, stderr) = ssh_client.exec_command("/ip address print")
vystup = []
counter = 0
for line in stdout:
    line_list = line.strip().split(" ")
    if len(line_list) < 2:
        continue
    vystup.append({"interface": line_list[3].split("=")[1], "ip": line_list[1].split("=")[1]})
print(vystup)