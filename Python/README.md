#Written by Ryan D'souza

##Various python files I run from the commandline to help me with miscellaneous tasks

####[iOS App Icon Resizer](https://github.com/dsouzarc/dotfiles/blob/master/Python/iOSAppIconResizer.py)
Quickly resizes an image of any extension to 5 png images according to Apple's iOS icon requirements. 
Creates a directory in the directory it is run from called 'AppIcon' and saves each file there with the appropriate title ie. iPhone6@3x.png will be 180 x 180

    #Can be run from any directory
    python iOSAppIconResizer.py imageName.jpg
