import pyPdf;
import random;

####################################################################
# Written by Ryan D'souza
# Generates notes randomly from a PDF
# See: github.com/dsouzarc/dotfiles/tree/master/Python/NoteTaker
####################################################################

#UPDATE THESE
fileName = "Dubliners.pdf";
noteSheetName = "Dubliners Notes.md";
startPage = 4; #The actual first page of the book

#Optional Update
noteFrequency = 2;
minLineLength = 8;

#Returns a random note line based on some conditions
def randomNote(lines):
    randomNoteLine = random.choice(lines);

    if len(randomNoteLine) <= minLineLength:
        return randomNote(lines);
    else:
        return randomNoteLine + ".";

#Markdown format line for notes
def formatLine(pageNumber, line):
    formattedLine = "- **Page " + str(pageNumber) + "**: " + line + "\n";
    return formattedLine;

#PDF version of the book
book = file("dubliners.pdf", "rb");
pdf = pyPdf.PdfFileReader(book);

#Create a notes file
notes = open(noteSheetName, "w");

for i in range(startPage, pdf.getNumPages()):

    #If it is time to take a note
    if (i - startPage) % noteFrequency == 0:

        #Gets each line on the page
        page = pdf.getPage(i);
        text = page.extractText();
        text = text.replace("\n", " ");
        lines = text.split(".");

        #A formatted, random line
        randomNoteLine = randomNote(lines);
        formattedLine = formatLine(i, randomNoteLine);

        #Sometimes there's an encoding error when writing to file, so just choose another line
        try: 
            notes.write(formattedLine);
        except (UnicodeEncodeError):
            formattedLine = formatLine(i, rrandomNote(lines));
            notes.write(formattedLine);

#Save and print mission success :)
notes.close();
print("Notes created. Check: " + noteSheetName);
