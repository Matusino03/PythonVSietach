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
#    conter += 1
#    if counter < 3:
#        continue
#    riadok_list = line.strip("\n")..strip("\r").split("\t")
#    while "" in riadok_list:
#        riadik_list.remove("")
#        vystup.append({"interface": riadok_list[0], "ip": riadok_list[1]})
#    
#    print(vystup)

#(stdin, stdout, stderr) = ssh_client.exec_command("conf t")
#(stdin, stdout, stderr) = ssh_client.exec_command("int lo0")
#(stdin, stdout, stderr) = ssh_client.exec_command("ip add 1.1.1.1 255.255.255.255")


