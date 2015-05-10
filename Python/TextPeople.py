#!/usr/bin/python
import CredentialManager;
import sys;
import urllib2;
import urllib;

######################################################
# Written by Ryan D'souza
# Sends a text to a person using SendGrid's API
#
# Dependencies: CredentialManager
#   tiny.cc/credentialManager
#
# Run Instructions: 
#   python TextPeople.py
######################################################

to = raw_input("To: ");
from_ = raw_input("From: ");
message = raw_input("Message: ");

#Url for POST request
url = "https://api.sendgrid.com/api/mail.send.json";

#My Information
username = CredentialManager.get_value("SendGridUsername");
password = CredentialManager.get_value("SendGridPassword");

params = {
    "api_user": username,
    "api_key": password,
    "from": from_,
    "to": to,
    "subject": " ",
    "text": message
};

params = urllib.urlencode(params);

request = urllib.urlopen(url, params);
response = request.read();

if response.find("success") == -1:
    print(response);
else:
    print("Successfully sent");
