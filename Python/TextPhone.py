#!/usr/bin/python

import sys
import urllib2
import urllib

from CredentialManager import CredentialManager

######################################################
# Written by Ryan D'souza
# Sends a text to myself using SendGrid's API
#
# Dependencies: CredentialManager
#   tiny.cc/credentialManager
#
# Run Instructions: 
#   python TextPhone.py
######################################################


#If message is commandline argument
if len(sys.argv) == 2:
    message = sys.argv[1]
else:
    message = raw_input("Enter message: ")

#Url for POST request
url = "https://api.sendgrid.com/api/mail.send.json"

#My Information
username, password = CredentialManager().get_account('SendGrid')
from_ = "6099154930"
to = from_ + "@vtext.com"

params = {
    "api_user": username,
    "api_key": password,
    "from": from_,
    "to": to,
    "subject": " ",
    "text": message
}

params = urllib.urlencode(params)

request = urllib.urlopen(url, params)
response = request.read()

if response.find("success") == -1:
    print(response)
else:
    print("Successfully sent")
