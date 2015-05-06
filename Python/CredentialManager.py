import base64;
import json;
import getpass; 
import os;

directory_path = str(os.path.expanduser("~")) + "/.my_credential_manager";

file_path = directory_path + ".credential_files.json";

if not os.path.exists(directory_path):
    print("Initialized credential manager: " + file_path);
    os.makedirs(directory_path);

if os.path.isfile(file_path):
    try:
        credentials = json.load(file_path);
        print("Credentials loaded");
    except Error:
        print("Problem loading existing credentials from file. Building new file");
        credentials = {};
else:
    print("No existing credentials");
    credentials = {};

usernameKey = raw_input("Username key: ");
username = raw_input("Username: ");

passwordKey = raw_input("Password key: ");
password = getpass.getpass("Password: ");

print(password);
