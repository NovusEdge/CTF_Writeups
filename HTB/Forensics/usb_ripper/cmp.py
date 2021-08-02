import sys, os
import pathlib
import json
import re


#####################################################
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)
#####################################################

auth_data   = json.load(open('usb-ripper/auth.json', 'r'))
syslog_data = open('usb-ripper/syslog', 'r').read()

pattern = ": SerialNumber: ([0-9]+([a-zA-Z]+[0-9]+)+)"
matches = re.findall(pattern, syslog_data)
serials = set(auth_data['serial'])

found = list(filter(lambda x: x[0] not in serials, matches))

print(len(found))
