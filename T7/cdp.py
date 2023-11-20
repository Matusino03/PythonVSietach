#!/usr/bin/env python 3
from scapy.all import *
import struct


def mac_to_bytes(mac):
    mac = mac.replace(":", "")
    mac_bytes = bytes.fromhex(mac)
    return mac_bytes


class Eth_hdr:
    def __init__(self, src_mac):
        self.dst_mac = "01:00:0c:cc:cc:cc"
        self.src_mac = src_mac
        self.length = 0
        self.payload = None

    def to_bytes(self):
        if self.payload == None:
            return None
        return mac_to_bytes(self.dst_mac) + mac_to_bytes(self.src_mac) + struct.pack("!H",
                                                                                     self.length) + self.payload.to_bytes

    def add_payload(self, payload):
        self.payload = payload
        self.length = len(payload.to_bytes)


class Llc_hdr:
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
        return struct.pack("!3B", self.dsap, self.ssap, self.ctrl) + mac_to_bytes(self.oui) + struct.pack("!H",
                                                                                                          self.pid) + self.payload.to_bytes


class CDP_hdr:
    def __init__(self):
        self.version = 1
        self.ttl = 180
        self.checksum = 0xbf42
        self.payload = list()

    def add_payload(self, payload):
        self.payload.append(payload)

    def to_bytes(self):
        payload_bytes = bytes()
        for payload in self.payload:
            payload_bytes += payload.to_bytes
        return struct.pack("!BBH", self.version, self.ttl, self.checksum) + payload_bytes


class TLV:
    def __init__(self, type):
        self.type = type
        self.length = 4

    def to_bytes(self):
        return struct.pack("!HH", self.type, self.length)


class TLV_device_id(TLV):
    def __init__(self, hostname):
        TLV.__init__(self, 0x0001)
        self.value = hostname
        value_bytes = self.value.encode()
        self.length += len(value_bytes)

    def to_bytes(self):
        value_bytes = self.value.encode()
        print(self.length)
        return TLV.to_bytes(self) + value_bytes


class TLV_port_id(TLV_device_id):
    def __init__(self, port):
        super().__init__(port)
        self.type = 0x0003


class TLV_software(TLV_device_id):
    def __init__(self):
        super().__init__("Windows 11 23H2")
        self.type = 0x0005

class TLV_capabilities(TLV):
    def __init__(self, router=False, switch=False, host=True):
        TLV.__init__(self, 0x0004)
        self.capabilities = 0
        self.length = 8 # constantna cela dlzka TLV
        if router:
            self.capabilities = self.bit_set(self.capabilities, 1)
        if switch:
            self.capabilities = self.bit_set(self.capabilities, 4)
        if host:
            self.capabilities = self.bit_set(self.capabilities, 5)

    def bit_set(self, vstup, por_bit):
        return vstup | (1 << por_bit-1)

    def to_bytes(self):
        return TLV.to_bytes(self) + struct.pack("!I", self.capabilities)

# IFACES.show()

# index 18 MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
interface = IFACES.dev_from_index(18)
sock = conf.L2socket(iface=interface)

eth_hdr = Eth_hdr("00:11:22:33:44:55")
llc_hdr = Llc_hdr()
cdp_hdr = CDP_hdr()
tlv_device_id = TLV_device_id("IdeaPad")
cdp_hdr.add_payload(tlv_device_id)
tlv_port_id = TLV_port_id("wifi")
cdp_hdr.add_payload(tlv_port_id)
tlv_cap = TLV_capabilities(host=True, router=True, switch=True)
cdp_hdr.add_payload(tlv_cap)
tlv_software = TLV_software()
cdp_hdr.add_payload(tlv_software)
llc_hdr.add_payload(cdp_hdr)
eth_hdr.add_payload(llc_hdr)
sock.send(eth_hdr.to_bytes())
