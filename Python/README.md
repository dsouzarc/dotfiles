#Written by Ryan D'souza

##Various python files I run from the commandline to help me with miscellaneous tasks

####[Credential Manager](https://github.com/dsouzarc/dotfiles/blob/master/Python/CredentialManager.py)

Super lightweight, secure (base64encode), quick, and easy to use credential manager to save and retrieve passwords. Stores the encrypted passwords in a secret json file in a secret folder in the home directory, enabling the script to be run from anywhere on the computer.

There's only one file needed (quick for copying/pasting), and all imports are from the standard python library so downloading it is as simple as 
    curl -L tiny.cc/credentialManager.py > CredentialManager.py

and using it as simple as
    python CredentialManager.py

I mainly built this to use on my school's computer where installing commandline tools like 'pip' is not allowed. Because of that, I can't install python's 'keyring' library to securely store my usernames/passwords. So, I made this script which can be run from anywhere

#####How to use
Installation & Setup

    #Sets up directory and json file, and also prompts for quickly saving a username and password (password entering is hidden)
    python CredentialManager.py

Accessing stored data

    import CredentialManager;

    username = CredentialManager.get_value("sendgridUsername");
    password = CredentialManager.get_value("sendgridPassword");

Quickly modifying data (Option 1) --> [Example](https://github.com/dsouzarc/dotfiles/blob/master/Python/CredentialManagerExample.py)

    import CredentialManager;

    CredentialManager.save_credentials("sendgridUsername", "someusername", sendgridPassword", "somePassword");
    CredentialManager.save_key("PromMeParseAPIKey", "someapikey");

    CredentialManager.delete_key("PromMeParseAPIKey");

Quickly modifying data (Option 2) --> Run from the terminal

    python -c 'import CredentialManager; CredentialManager.save_key("myKey", "myValue")'
    python -c 'import CredentialManager; CredentialManager.delete_key("gmailUsername")'


####[iOS App Icon Resizer](https://github.com/dsouzarc/dotfiles/blob/master/Python/iOSAppIconResizer.py)
Quickly resizes an image of any extension to 5 png images according to Apple's iOS icon requirements. 
Creates a directory in the directory it is run from called 'AppIcon' and saves each file there with the appropriate title ie. iPhone6@3x.png will be 180 x 180

    #Can be run from any directory
    python iOSAppIconResizer.py imageName.jpg
