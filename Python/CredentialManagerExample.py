import CredentialManager;

#Tests CredentialManager.py

#Two ways to save credentials:

#1
CredentialManager.save_credentials("gmailUsernameKey", "secretUsername", "gmailPasswordKey", "secretPassword");
#2. Prompts for info to be entered
#Enter 'python CredentialManager.py' in terminal

CredentialManager.save_key("gmailUsername", "gmailPassword");

password = CredentialManager.get_key("gmailUsername");

if CredentialManager.does_key_exist("gmailUsername"):
    CredentialManager.delete_key("gmailUsername");
