from PIL import Image;
import os;
import sys;

global originalImage;
global saveToPath;

def resizeImage(newWidth, newHeight, imageDescription):
    newImage = originalImage.resize((newWidth, newHeight), Image.ANTIALIAS);
    
    newFileName = saveToPath + "/Icon-" + imageDescription + ".png";
    newImage.save(newFileName, quality=100);

if len(sys.argv) == 1:
    fileName = raw_input("Enter file name and directory:\n");

else:
    fileName = sys.argv[1];

originalImage = Image.open(fileName);

pathWhenExecuting = os.getcwd();
saveToPath = pathWhenExecuting + "/AppIcon";

if not os.path.exists(saveToPath):
    os.makedirs(saveToPath);

resizeImage(180, 180, "Small");

