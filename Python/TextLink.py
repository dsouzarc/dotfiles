#!/usr/bin/python
import config;
import sendgrid;
import sys;
import urllib;
import json
from pprint import pprint

sg = sendgrid.SendGridClient(config.SG_USERNAME, config.SG_PASSWORD);
message = sendgrid.Mail();

message.add_to("Ryan D'souza <" + config.PHONE + "@vtext.com>");
message.set_from("MBPro CL");

#If a link has been included as a parameter
if len(sys.argv) == 2:

    #If the link URL is less than 150 chars
    if len(sys.argv[1]) <= 150:
        bodyText = sys.argv[1];

    #Else, compress it
    else:
        JSON = json.loads(urllib.urlopen("http://po.st/api/shorten?longUrl=" + sys.argv[1] + "&apiKey=3E5C05F5-DDED-4485-A193-F486E947F547",'r').read());
        bodyText = JSON['short_url'];

#Otherwise, just prompt for link
else:
    bodyText = raw_input("Enter text content: ");

#Blank subject
message.set_subject(" ");

#Text is what the user inputted
message.set_text(bodyText);

#Send the message
status, msg = sg.send(message);

#Print error
if msg.find("success") == -1:
    print msg;

#Print message successfully sent
else:
    print "Successfully sent"


#Old message text that involved command line arguments
'''
#If there is only one parameter, the subject is blank
if len(sys.argv) == 2:
    message.set_subject(" ");
    message.set_text(sys.argv[1]);

#But, if there's also a subject
if len(sys.argv) == 3:
    message.set_subject(sys.argv[1]);
    message.set_subject(sys.argv[2]);
'''
