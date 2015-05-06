import base64;
import json;
import getpass; 
import os;

directory_path = str(os.path.expanduser("~")) + "/.my_credential_manager/";
file_path = directory_path + ".credential_files.json";

if not os.path.exists(directory_path):
    print("Initialized credential manager: " + file_path);
    os.makedirs(directory_path);

if os.path.isfile(file_path):
    try:
        with open(file_path) as credential_file:
            credentials = json.load(credential_file);
            print(credentials);
            print("Credentials loaded");
    except ValueError:
        print("Value error for loading existing credentials from file. Building new file");
        credentials = {};
else:
    print("No existing credentials");
    credentials = {};

def save_credentials(usernameKey, username, password, passwordKey):
    
    if usernameKey in credentials:
        print("Username already exists for '" + usernameKey + "'.");

        answer = raw_input("Override? y/n: ");

        if answer == 'y':
            credentials[usernameKey] = base64.b64encode(username);
            credentials[passwordKey] = base64.b64encode(password);

            with open(file_path, 'w') as file:
                json.dump(credentials, file, sort_keys = True, indent = 4, ensure_ascii = False);
                print("Credentials saved");
                return;
        else:
            print("Cancelled");
            return;
    else:
        credentials[usernameKey] = base64.b64encode(username);
        credentials[passwordKey] = base64.b64encode(password);
        
        with open(file_path, 'w') as file:
            json.dump(credentials, file, sort_keys = True, indent = 4, ensure_ascii = False);
            print("Credentials saved");
            return;

usernameKey = raw_input("Username key: ");
username = raw_input("Username: ");

passwordKey = raw_input("Password key: ");
password = getpass.getpass("Password: ");

save_credentials(usernameKey, username, password, passwordKey);

