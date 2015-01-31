#!/usr/bin/python
import config;
import sendgrid;
import sys;

sg = sendgrid.SendGridClient(config.SG_USERNAME, config.SG_PASSWORD);
message = sendgrid.Mail();

message.add_to("Ryan D'souza <" + raw_input("Enter to: ") + ">");
message.set_from("Ryan D'souza <" + raw_input("Enter from: ") + ">");

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
