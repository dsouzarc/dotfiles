import itertools;

#############################################################
# Written by Ryan D'souza
# Generates password combinations and saves them to a file
#############################################################


#Returns a string with every ASCII key
#Essentially returns ' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
def getAllAsciiValues():
    string = "";
    asciiValue = 32;
    while asciiValue <= 126:
        string = string + chr(asciiValue);
        asciiValue += 1;
    return string;


#Writes the password combinations to a file
def writePasswordCombinations(fileName = None, fromString = None, maxCharacters = None, minCharacters = None):

    #All combinations of what string
    if fromString is None:
        fromString = getAllAsciiValues();

    #Max number of characters for password
    if maxCharacters is None:
        maxCharacters = 10;

    #Min number of characters for password
    if minCharacters is None:
        minCharacters = 3;

    #File name to save the password combinations to
    if fileName is None:
        fileName = str(minCharacters) + "-" + str(maxCharacters) + "_passwords.txt";

    numPasswords = 0;
    numFiles = 1;

    #Create a new file with the format 1-passwordFileName.txt
    passwordFile = open(str(numFiles) + "-" + fileName, 'w');

    #Get all combinations from minCharacter length to maxCharacterlength
    while minCharacters <= maxCharacters:
        res = itertools.product(fromString, repeat=minCharacters); 
        for i in res: 
            passwordFile.write(''.join(i) + "\n");
            numPasswords += 1;

            #Every 1,000,000,000, store the combinations in a new file with format 2-passwordFileName.txt
            if numPasswords % 1000000000 == 0:
                passwordFile.close();
                numFiles += 1;
                passwordFile = open(str(numFiles) + "-" + fileName, 'w');

            #Print a status update every now and then
            if numPasswords % 1000000 == 0:
                print("# of passwords: " + str(numPasswords));

        #For incrementing password length
        minCharacters += 1;

    passwordFile.close();

#For my testing purpose, just testing letters and numbers
letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
writePasswordCombinations(fileName = "pure_letters_numbers.txt", fromString = letters, maxCharacters = 14, minCharacters = 8);
