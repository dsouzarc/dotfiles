#!/usr/bin/python
import CredentialManager;
import sys;
import urllib2;
import urllib;

######################################################
# Written by Ryan D'souza
# Sends an email to myself using SendGrid's API
#
# Dependencies: CredentialManager
#   tiny.cc/credentialManager
#
# Run Instructions: 
#   python EmailMe.py
######################################################

#If message is commandline argument
if len(sys.argv) == 2:
    message = sys.argv[1];
else:
    message = raw_input("Enter message: ");

#Url for POST request
url = "https://api.sendgrid.com/api/mail.send.json";

#My Information
username = CredentialManager.get_value("SendGridUsername");
password = CredentialManager.get_value("SendGridPassword");
from_ = "RyansMacbookProCommandLine";
to = "dsouzarc@gmail.com";

params = {
    "api_user": username,
    "api_key": password,
    "from": from_,
    "to": to,
    "subject": "MBPro CL",
    "text": message
};

params = urllib.urlencode(params);

request = urllib.urlopen(url, params);
response = request.read();

if response.find("success") == -1:
    print(response);
else:
    print("Successfully sent");
