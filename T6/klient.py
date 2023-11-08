import socket as s
from enum import IntEnum
import json

SERVER = "127.0.0.1"
PORT = 8080
SERVER_NAME = "Server"

class Operacia(IntEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3
    MSG = 4

class Sprava:
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.od = paOd
        self.komu = paKomu
        self.operacia = paOperacia
        self.text = paText

    def to_bytes(self):
        json_str = json.dumps(self.__dict__)
        return json_str.encode()

    @staticmethod
    def json_decoder(paObject):
        return Sprava(paObject['od'], paObject['komu'], paObject['operacia'], paObject['text'])

def napoveda():
    print("NAPOVEDA: ")
    print("     \q ukonci program")
    print("     \l vypise pouzivatelov")
    print("     \h help")
    print("     Spravu posielajte v tvare: prijemca:sprava")

print("CHAT KLIENT")
od = input("Zadaj meno: ")
napoveda()

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.connect((SERVER, PORT))

msg = Sprava(od, SERVER_NAME, Operacia.LOGIN.value, None)
sock.send(msg.to_bytes())

while True:
    text = input("Zadajte spravu alebo \ pre specialnu operaciu:")
    if text[0] == "\\":
        if text[1] == "h":
            napoveda()
            continue
        elif text[1] == "q":
            break
        elif text[1] == "l":
            msg = Sprava(od, SERVER_NAME, Operacia.USERS.value, None)
            sock.send(msg.to_bytes())
            server_msg = sock.recv(1000)
            msg = json.loads(server_msg.decode(), object_hook=Sprava.json_decoder)
            print("Zoznam prihlasenych pouzivatelov: {}".format(msg.text))
            continue
    
    pole_msg = text.split(":")
    msg = Sprava(od, pole_msg[0], Operacia.MSG.value, pole_msg[1])
    sock.send(msg.to_bytes())    

msg = Sprava(od, SERVER_NAME, Operacia.EXIT.value, None)
sock.send(msg.to_bytes())
sock.close()
