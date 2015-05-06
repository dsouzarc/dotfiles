#!/usr/bin/python
import CredentialManager;
import sendgrid;
import sys;

sg = sendgrid.SendGridClient(CredentialManager.get_value("SendGridUsername"), CredentialManager.get_value("SendGridPassword"));
message = sendgrid.Mail();

message.add_to("dsouzarc@gmail.com");
message.set_from("Ryan D'souza <Ryans Macbook Pro Command Line>");

bodyText = raw_input("Enter text content: ");

#Blank subject
message.set_subject("MBPro CL");

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
