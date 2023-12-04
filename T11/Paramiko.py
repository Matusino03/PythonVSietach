from paramiko import *

IP = "158.193.152.167"
PORT = 22
USER = "admin"
PASS = "Admin123"

ssh_client = SSHCLIENT
ssh_client.set_missing_key_policy(AutoAddPolicy())
ssh_client.connest(hostname=IP, port=PORT, username=USER, password=PASS)
(stdin, stdout, stderr) = ssh_client.exec_command("sh ip int br")
vystup = list()
for line in stdout:
    riadok_list = line.strip("\n")..strip("\r").split("\t")
    while "" in riadok_list:
        riadik_list.remove("")
    print(riadok_list)

