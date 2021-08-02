import sys, os
import pathlib
import json
import re


#####################################################
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)
#####################################################

with open('usb-ripper/auth.json', 'r') as f:
    auth = json.load(f)

# Getting the serial numbers which are authorized
auth_serials = set(auth['serial'])


with open('usb-ripper/syslog', 'r') as f:
    logs = f.read()

pattern = r"SerialNumber: ([0-9]+([a-zA-Z]+[0-9]+)+)"
matches = set(dict(re.findall(pattern, logs)).keys())

print(matches.symmetric_difference(auth_serials))
