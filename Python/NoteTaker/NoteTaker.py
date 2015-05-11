import pyPdf;
import random;

fileName = "Dubliners.pdf";
noteSheetName = "Dubliners Notes.md";
startPage = 4;
noteFrequency = 2;
minLineLength = 8;

#Returns a random note line based on some conditions
def randomNote(lines):
    randomNoteLine = random.choice(lines);

    if len(randomNoteLine) <= minLineLength:
        return randomNote(lines);
    else:
        return randomNoteLine + ".";

#Format line for notes
def formatLine(pageNumber, line):
    formattedLine = "- **Page " + str(pageNumber) + "**: " + line + "\n";
    return formattedLine;

book = file("dubliners.pdf", "rb");
pdf = pyPdf.PdfFileReader(book);
notes = open(noteSheetName, "w");

for i in range(startPage, pdf.getNumPages()):

    #If it is time to take a note
    if (i - startPage) % noteFrequency == 0:
        page = pdf.getPage(i);
        text = page.extractText();
        text = text.replace("\n", " ");
        lines = text.split(".");

        randomNoteLine = randomNote(lines);
        formattedLine = formatLine(i, randomNoteLine);

        try: 
            notes.write(formattedLine);
        except (UnicodeEncodeError):
            formattedLine = formatLine(i, rrandomNote(lines));
            notes.write(formattedLine);

notes.close();
print("Notes created. Check: " + noteSheetName);
