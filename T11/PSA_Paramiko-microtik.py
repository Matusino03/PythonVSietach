from paramiko import *

IP = "158.193.152.167"
PORT = 22
USER = "admin"
PASS = "Admin123"

ssh_client = SSHCLIENT
ssh_client.set_missing_key_policy(AutoAddPolicy())
ssh_client.connest(hostname=IP, port=PORT, username=USER, password=PASS, look_for_key)

(stdin, stdout, stderr) = ssh_client.exec_command("/ip address print")
vystup = list()
counter 0
for line in stdout:
    line_list = line.strip("\n").strip("\r").split(" ")
    if len(line_list) < 2:
        continue
    vystup.append({"interface": line_list[3].split("=")[1], "ip": line_list[1].split("=")[1]})
    print(vystup)

#(stdin, stdout, stderr) = ssh_client.exec_command("conf t")
#(stdin, stdout, stderr) = ssh_client.exec_command("int lo0")
#(stdin, stdout, stderr) = ssh_client.exec_command("ip add 1.1.1.1 255.255.255.255")


