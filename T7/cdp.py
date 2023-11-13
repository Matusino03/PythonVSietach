#!/usr/bin/env python 3
from scapy.all import *
import struct

def mac_to_bytes(mac):
    mac = mac.replace(":", "")
    mac_bytes = bytes.fromhex(mac)
    return mac_bytes

class Eth_hdr():
    def __init__(self, src_mac):
        self.dst_mac = "01:00:0c:cc:cc:cc"
        self.src_mac = src_mac
        self.length = 0
        self.payload = None

    def to_bytes(self):
        if self.payload == None:
            return None
        return mac_to_bytes(self.dst_mac) + mac_to_bytes(self.src_mac) + struct.pack("!H", self.length) + self.payload.to_bytes()

    def add_payload(self, payload):
        self.payload = payload
        self.length = len(payload.to_bytes())

class Llc_hdr():
    def __init__(self):
        self.dsap = 0xaa
        self.ssap = 0xaa
        self.ctrl = 0x03
        self.oui = "00:00:0c"
        self.pid = 0x2000
        self.payload = None

    def add_payload(self, payload):
        self.payload = payload

    def to_bytes(self):
        return struct.pack("!3B", self.dsap, self.ssap, self.ctrl) + mac_to_bytes(self.oui) + struct.pack("!H", self.pid) + self.payload.to_bytes()

class CDP_hdr():
    def __init__(self):
        self.version = 1
        self.ttl = 180
        self.checksum = 0
        self.payload = list()

    def add_payload(self, payload):
        self.payload.append(payload)

    def to_bytes(self):
        payload_bytes = bytes()
        for payload in self.payload:
            payload_bytes += payload.to_bytes()
        return struct.pack("!BBH", self.version, self.ttl, self.checksum) + payload_bytes

class TLV():
    def __init__(self, type):
        self.type = type
        self.length = 4

    def to_bytes(self):
        return struct.pack("!HH", self.type, self.length)

class TLV_device_id(TLV):
    def __init__(self, hostname):
        TLV.__init__(self, 0x0001)
        self.value = hostname

    def to_bytes(self):
        value_bytes = self.value.encode()
        self.length += len(value_bytes)
        return TLV.to_bytes(self) + value_bytes

#IFACES.show()

# index 18 MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
interface = IFACES.dev_from_index(18)
sock = conf.L2socket(iface=interface)

eth_hdr = Eth_hdr("00:11:22:33:44:55")
llc_hdr = Llc_hdr()
cdp_hdr = CDP_hdr()
tlv_device_id = TLV_device_id("IdeaPadWin11")
cdp_hdr.add_payload(tlv_device_id)
llc_hdr.add_payload(cdp_hdr)
eth_hdr.add_payload(llc_hdr)
sock.send(eth_hdr.to_bytes())