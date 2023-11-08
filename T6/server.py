from threading import Thread as tred
import socket
import json
from enum import IntEnum as enum

SERVER = "0.0.0.0"
PORT = 8080
MLEN = 1000
QUEVE_LENGTH = 10

class Operacia(enum):
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

    @staticmethod
    def JsonDecoder(paObj):
        return Sprava(paObj['od'],paObj['komu'],paObj['operacia'],paObj['text'])

def VybavKlienta(paClientSocket, paClientAddr, paPouzivatelia):

    while True:
        sprava = paClientSocket.recv(MLEN)
        jsonStr = sprava.decode()
        try:
            message = json.loads(jsonStr, object_hook=Sprava.JsonDecoder)
        except:
            continue

        if message.operacia == Operacia.LOGIN:
            paPouzivatelia.append(message.od)
            print("Prihlasil sa {} z IP {}, port {}".format(message.od, paClientAddr[0], paClientAddr[1]))
            continue
        
        if message.operacia == Operacia.EXIT:
            paPouzivatelia.remove(message.od)
            print("Odhlasil sa {} z IP {}, port {}".format(message.od, paClientAddr[0], paClientAddr[1]))
            return
        
        if message.operacia == Operacia.USERS:      
            odpoved = Sprava("Server", message.od, Operacia.USERS.value, paPouzivatelia)
            jsonStr = json.dumps(odpoved.__dict__)
            paClientSocket.send(jsonStr.encode())
            continue

        if message.operacia == Operacia.MSG:
            print("Sprava od {} komu {} text: {}".format(message.od, message.komu, message.text))
            continue

        

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))
    sock.listen(QUEVE_LENGTH)

    pouzivatelia = list()

    print("Server ide PECKA!!!!")

    while True:
        (clientSock, cliendAddr) = sock.accept()
        t = tred(target=VybavKlienta, args=(clientSock, cliendAddr, pouzivatelia))
        t.start()
    


