#usr/bin/env python3

import socket
import struct

DNS = "8.8.8.8"
DNS_PORT = 53
SRC_PORT = 50000

class Dns:
    def __init__(self):
        self.id = 0x1234
        self.flags = 0x0100 #standard query
        self.questions = 1
        self.answers = 0
        self.authority = 0
        self.additional = 0
        self.payload = list()

    def addPayload(self, payload):
        self.payload.append(payload)

    def to_bytes(self):
        payload_bytes = bytes()
        for payload in self.payload:
            payload_bytes += payload.to_bytes
        return struct.pack("!6H", self.id, self.flags, self.questions, self.answers, self.authority, self.additional) + payload_bytes

    class DNS_question:
        def __init__(self, query):
            self.query = bytes()
            liss_labels = query.split(".")
            for label in liss_labels:
                label_bytes = label.encode()
