#!/usr/bin/python

import sys;
import urllib2;
import urllib;
import json
import CredentialManager;

from pprint import pprint

#######################################################################
# Written by Ryan D'souza
# 
# Sends a text to myself of a link
# If the link is too long, uses po.st to shorten the link
#
# Dependency: CredentialManager.py
#   See: tiny.cc/credentialManager.py
#
# Run:
#   python TextLink.py
#######################################################################

def compress_url(url):
        JSON = json.loads(urllib.urlopen("http://po.st/api/shorten?longUrl=" + url + "&apiKey=3E5C05F5-DDED-4485-A193-F486E947F547",'r').read());
        return JSON['short_url'];

url = "https://api.sendgrid.com/api/mail.send.json";
to = CredentialManager.get_value("PHONE") + "@vtext.com";
from_ = "MBProCL";
username = CredentialManager.get_value("SendGridUsername");
password = CredentialManager.get_value("SendGridPassword");

#If a link has been included as a parameter
if len(sys.argv) == 2:

    #If the link URL is less than 150 chars
    if len(sys.argv[1]) <= 150:
        bodyText = sys.argv[1];

    #Else, compress it
    else:
        bodyText = compress_url(sys.argv[1]);

#Otherwise, just prompt for link
else:
    bodyText = raw_input("Enter text content: ");

    if len(bodyText) >= 150:
        bodyText = compress_url(bodyText);

params = {
    "api_user": username,
    "api_key": password,
    "from": from_,
    "to": to,
    "subject": " ",
    "text": bodyText
};

params = urllib.urlencode(params);

request = urllib.urlopen(url, params);
response = request.read();

if response.find("success") == -1:
    print(response);
else:
    print("Successfully sent");
