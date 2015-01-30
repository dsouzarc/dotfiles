import config;
import sendgrid;
import sys;

sg = sendgrid.SendGridClient(config.SG_USERNAME, config.SG_PASSWORD);

message = sendgrid.Mail();

message.add_to("Ryan D'souza <" + config.PHONE + "@vtext.com>");
message.set_from("Ryan D'souza <Ryans Macbook Pro Command Line>");

message.set_subject(sys.argv[1]);

if len(sys.argv) > 2:
    message.set_text(sys.argv[2]);

status, msg = sg.send(message);

print status;
print msg;
