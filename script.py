#!/usr/bin/env python

import requests.packages.urllib3
import requests
import os.path
import time
import json
import re

URL = "https://www.teamspeak.com/downloads"
FILE = "VERSION"

if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    while True:
        data = requests.get(URL)
        if data.status_code == 200:
            break
        time.sleep(60)
    client = re.findall("Client [^>]+([^<]+)", data.text)[0][1:]
    server = re.findall("Server [^>]+([^<]+)", data.text)[0][1:]
    if os.path.isfile(FILE):
        with open(FILE, "r") as f:
            prev = json.loads(f.read())
        if prev["client"] != client:
            print "Client is now: " + client
        if prev["server"] != server:
            print "Server is now: " + client
        with open(FILE, "w") as f:
            f.write(json.dumps({"server":server, "client":client}))
    else:
        print "Client: %s\nServer: %s" % (client, server)
        with open(FILE, "w") as f:
            f.write(json.dumps({"server":server, "client":client}))
