from PIL import Image;
import sys;

global originalImage;

def resizeImage(newWidth, newHeight, imageDescription):
    newImage = originalImage.resize((newWidth, newHeight), Image.ANTIALIAS);
    newImage.save("Icon-" + imageDescription + ".png", quality=100);

if len(sys.argv) == 1:
    fileName = raw_input("Enter file name and directory:\n");

else:
    fileName = sys.argv[1];

originalImage = Image.open(fileName);

resizeImage(180, 180, "Small");
