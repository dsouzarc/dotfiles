import pyPdf;
import random;

from docx import Document;

####################################################################
# Written by Ryan D'souza
# Generates notes randomly from a PDF
# See: github.com/dsouzarc/dotfiles/tree/master/Python/NoteTaker
####################################################################

#UPDATE THESE
fileName = "Dubliners.pdf";
noteSheetName = "Dubliners Notes.md";
noteSheetWordName = "Dubliners Notes.docx";
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
wordDocument = Document();

for i in range(startPage, pdf.getNumPages()):

    #If it is time to take a note
    if (i - startPage) % noteFrequency == 0:

        #Gets each line on the page
        page = pdf.getPage(i);
        text = page.extractText();
        text = text.replace("\n", " ");
        lines = text.split(".");

        #While loop for continually retrying 'try' until there is no exception
        while True:

            #Try writing to both files (possible encoding error)
            try: 

                #Get a formatted line at random from the page
                randomNoteLine = randomNote(lines);
                formattedLine = formatLine(i, randomNoteLine);

                #Add the line to the word document note sheet and the markdown note sheet
                notes.write(formattedLine);
                noteLine = wordDocument.add_paragraph('', style='ListBullet');
                noteLine.add_run('Page ' + str(i) + ': ').bold = True
                noteLine.add_run(randomNoteLine).bold = False;

            #Sometimes there is an encoding error. Choose a new line and repeat
            except (UnicodeEncodeError):
                continue;
            break;

#Save and print mission success :)
notes.close();
wordDocument.save(noteSheetWordName);
print("Notes created. Check: " + noteSheetName + " and " + noteSheetWordName);
