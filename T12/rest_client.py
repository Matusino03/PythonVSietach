#!/usr/bin/env python3

import requests
from flask import Flask, render_template, request

IP = "158.193.152.176"
PORT = 22
USER = "admin"
PASS = "Admin123"

app = Flask(__name__)

def get_interfaces():
    prikaz = "/ip/interface"
    url = "http://{}:{}/rest{}".format(IP, PORT, prikaz)
    requests.get(url, auth=(USER, PASS), verify=False)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(resp.status_code)
        print(resp.json())
        return None

def get_ip():
    prikaz = "/ip/iddress"
    url = "http://{}:{}/rest{}".format(IP, PORT, prikaz)
    resp = requests.get(url, auth=(USER, PASS), verify=False)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(resp.status_code)
        print(resp.json())
        return None

def sh_ip_int_brief(interface, ip):
    vystup = list()
    for i in interface:
        ip_found = None
        for addr in ip:
            if addr["interface"] == i["name"]:
                ip_found = addr["address"]
                break
        vystup.append({"name": i["name"], "status": i["running"], "ip": ip_found})   
    return vystup 

def create_loop(loop_name):
    prikaz = "/interface/bridge"
    url = "http://{}:{}/rest{}".format(IP, PORT, prikaz)
    body = {"name": loop_name}
    resp = requests.put(url, auth=(USER, PASS), verify=False, json=body)
    if resp.status_code == 200:
        return True
    else:
        print(resp.status_code)
        print(resp.json())
        return False

@app.route("/")
def index():
    if "loop_name" in request.args:
        create_loop(request.args.get("loop_name"))
    interfaces = get_interfaces()
    ip = get_ip()
    ip_int = sh_ip_int_brief(interfaces, ip)
    return render_template("index.html", interfaces=ip_int)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
    # create_loop("lo11")