#!/usr/bin/python

from PIL import Image;
import os;
import sys;

#Original image
global originalImage;

#Path to save to: path program run from + directory 'AppIcon'
global saveToPath;

#Resizes the image and saves it
#width/height are ints, imageDescription is string describing new image
def resizeImage(newWidth, newHeight, imageDescription):
    newImage = originalImage.resize((newWidth, newHeight), Image.ANTIALIAS);
    
    newFileName = saveToPath + "/Icon-" + imageDescription + ".png";
    newImage.save(newFileName, quality=100);

#If the image name/directory is not inputted, prompt user for it
if len(sys.argv) == 1:
    fileName = raw_input("Enter file name and directory:\n");

#If image name/directory is inputted as command parameter
else:
    fileName = sys.argv[1];

#Open the original image
originalImage = Image.open(fileName);

#Path to save files to (see 'saveToPath' declaration
pathWhenExecuting = os.getcwd();
saveToPath = pathWhenExecuting + "/AppIcon";

#If the 'AppIcon' directory does not exist, make it
if not os.path.exists(saveToPath):
    os.makedirs(saveToPath);

#Creates a copy of the original image, resizes to those dimensions, saves it to disk
resizeImage(180, 180, "iPhone6@3x");
resizeImage(120, 120, "iOS7-8@2x");
resizeImage(120, 120, "iPhone4S@2x");
resizeImage(152, 152, "iPad(mini)@2x");
resizeImage(76, 76, "iPad2(mini)@1x");

#iOS Sizes link: https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/IconMatrix.html
