#                                                       Zadanie:
# Vytvorte program, ktorý bude pomocou knižnice Paramiko interagovať s MikroTik zariadením pomocou SSH protokolu.
# Prihlasovacie údaje (IP = 158.193.152.148, meno = admin, heslo = Admin123) Vám poskytne skúšajúci.
# Program bude schopný vypísať mená CDP/LLDP (identity) susedov a ich IPv4 adresu (vyparsujte z príkazu „ip neighbor print [detail]“)

# Importujeme knižnice, ktoré budeme potrebovať
# paramiko = pripojenie cez SSH
from paramiko import SSHClient, AutoAddPolicy

# Definujeme si premenné
IP = "158.193.152.148"
USER = "admin"
PASS = "Admin123"

# Vytvoríme si SSH clienta a uložíme ho do premennej ssh
ssh = SSHClient()

# Pripojime sa na SSH
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(AutoAddPolicy())

# Prihlásime sa pomocou poskytnutých údajov (definovaných vyššie)
ssh.connect(hostname=IP, username=USER, password=PASS)

# Zadáme príkaz 'ip neighpor print' s použitím knižnice paramiko
stdin, stdout, stderr = ssh.exec_command("ip neighbor print")

# Vypíše výstup na konzolu
print(stdout.read().decode('utf-8'))

# Vypíše všetky riadky výstupu
for line in stdout.readlines():
    print(line)