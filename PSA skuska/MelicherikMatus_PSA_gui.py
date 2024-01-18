#                                                       Zadanie:
# Vytvorte program, ktorý bude pomocou knižnice Paramiko interagovať s MikroTik zariadením pomocou SSH protokolu.
# Prihlasovacie údaje (IP = 158.193.152.148, meno = admin, heslo = Admin123) Vám poskytne skúšajúci.
# Program bude schopný vypísať mená CDP/LLDP (identity) susedov a ich IPv4 adresu (vyparsujte z príkazu „ip neighbor print [detail]“)

# Importujeme knižnice, ktoré budeme potrebovať
# paramiko = pripojenie cez SSH
# tkinter = vytvorenie gui
from paramiko import SSHClient, AutoAddPolicy
from tkinter import Tk, Label, Text, Button

# Definujeme si premenné
IP = "158.193.152.148"
USER = "admin"
PASS = "Admin123"

# Vytvoríme si SSH clienta a uložíme ho do premennej ssh
ssh = SSHClient()

def connect_ssh():

    # Pripojime sa na SSH
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())

    # Prihlásime sa pomocou poskytnutých údajov (definovaných vyššie)
    ssh.connect(hostname=IP, username=USER, password=PASS)

    # Zadáme príkaz 'ip neighpor print' s použitím knižnice paramiko
    stdin, stdout, stderr = ssh.exec_command("ip neighbor print")
    
    # Výstup uložime do premennej
    output = stdout.read().decode('utf-8')

    # Vymažeme kontent textového riadku a vložíme tam výstup, ktorý sme si vyššie definovali
    text_box.delete(1.0, "end")
    text_box.insert("end", output)

# Vytvoríme nové okno pomocou tkinter
root = Tk()
root.title("SSH Client")

# Vytvoríme textový riadok pomocou tkinter
label = Label(root, text="Output:")
label.pack()

text_box = Text(root, height=10, width=100)
text_box.pack()

# Vytvoríme tlačidlo na pripojenie na server cez ssh a výpis výstupu pomocou tkinter
button = Button(root, text="Connect", command=connect_ssh)
button.pack()

# Zapneme cyklus eventov pre GUI
root.mainloop()