import sys;
import urllib;
import json;

#########################################################################
# Written by Ryan D'souza
# Prints the definition of a word and an example of it in a sentence
# Uses Pearson Dictionary API
#
# Dependencies: None
# Usage:
#   python Dictionary.py perfunctory
#
# Or, to prompt:
#   python Dictionary.py
#########################################################################


#Prints results in a nice format
def printResults(dictionary):

    senses = dictionary['senses'];

    for sense in senses:

        if 'definition' in sense:
            definition = sense['definition'];
            
            #Multiple definitions
            if isinstance(definition, list):
                for defi in definition:
                    print("Definition: " + defi);
            else:
                print("Definition: " + definition);

        #Not all definitions include an example
        if 'examples' in sense:
            examples = sense['examples'];

            #Multiple examples
            for example in examples:
                print("\tExample: " + example['text']);

#API URL
url = "https://api.pearson.com:443/v2/dictionaries/entries?headword=";

if len(sys.argv) == 1:
    word = raw_input("Enter word to define: ");
else:
    word = sys.argv[1];

url += word;

request = urllib.urlopen(url);
response = request.read();

if request.getcode() != 200:
    print("Error getting data: " + str(response));

response = json.loads(response);

if int(response["total"]) == 0:
    print("No definitions");
else:
    results = response["results"];

    for array in results:
        dataset = array["datasets"][0];
        if dataset == "laad3" or dataset == "ldoce5" or dataset == "lasde" or dataset == "laes" or dataset == "brep":
            printResults(array);

