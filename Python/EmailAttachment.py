#!/usr/bin/python
import base64;
import CredentialManager;
import sys;
import urllib2;
import urllib;

######################################################
# Written by Ryan D'souza
# Sends an attachment to myself using SendGrid's API
#
# Dependencies: CredentialManager
#   tiny.cc/credentialManager
#
# Run Instructions: 
#   python EmailAttachment.py
######################################################


#If filename is commandline argument
if len(sys.argv) == 2:
    fileName = sys.argv[1];
else:
    fileName = raw_input("Enter file name: ");

#Url for POST request
url = "https://api.sendgrid.com/api/mail.send.json";

#My Information
username = CredentialManager.get_value("SendGridUsername");
password = CredentialManager.get_value("SendGridPassword");
from_ = "MBProCL";
to = "dsouzarc@gmail.com";

#Parameters, same as usual
params = {
    "api_user": username,
    "api_key": password,
    "from": from_,
    "to": to,
    "subject": " ",
    "text": fileName,
};

#Add the file to the params
with open(fileName, 'rb') as f:
    params['files[' + fileName + ']'] = f.read();

#Encode them
params = urllib.urlencode(params);

#Request/response
request = urllib.urlopen(url, params);
response = request.read();

if response.find("success") == -1:
    print(response);
else:
    print("Successfully sent");
