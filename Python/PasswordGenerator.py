import itertools;

#Returns a string with every ASCII key
#Essentially returns ' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def getAllAsciiValues():

    string = "";
    asciiValue = 32;

    while asciiValue <= 126:
        string = string + chr(asciiValue);
        asciiValue += 1;

    return string;

def writePasswordCombinations(fileName = None, fromString = None, maxCharacters = None, minCharacters = None):

    if fromString is None:
        fromString = getAllAsciiValues();
    if maxCharacters is None:
        maxCharacters = 10;
    if minCharacters is None:
        minCharacters = 3;
    if fileName is None:
        fileName = str(minCharacters) + "-" + str(maxCharacters) + "_passwords.txt";

    numPasswords = 0;
    numFiles = 1;

    passwordFile = open(str(numFiles) + "-" + fileName, 'w');

    while minCharacters <= maxCharacters:
        res = itertools.product(fromString, repeat=minCharacters); 
        for i in res: 
            passwordFile.write(''.join(i) + "\n");
            numPasswords += 1;

            if numPasswords % 1000000000 == 0:
                passwordFile.close();
                numFiles += 1;
                passwordFile = open(str(numFiles) + "-" + fileName, 'w');
            if numPasswords % 1000000 == 0:
                print("# of passwords: " + str(numPasswords));
        minCharacters += 1;

    passwordFile.close();

letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
writePasswordCombinations(fileName = "pure_letters_numbers.txt", fromString = letters, maxCharacters = 14, minCharacters = 8);
