#!/bin/bash

#################################################################
#Written by Ryan D'souza
#Goes through each file in a directory
#If the name contains either 'Screenshot' or 'Screen shot'
#It renames it to Screenshot_X.yyy where
#X increments each time and yyy is the file's extension
#################################################################

#Start off with Screenshot_1
i=1;

for f in *
do

    #Screenshot classification
    if [[ $f == *"Screenshot"* ]] || [[ $f == *"Screen shot"* ]]
    then
        
        #Dealing with PNGs
        if [[ $f == *".png"* ]]
        then
            newFileName="Screenshot_$i.png";
            mv "$f" "$newFileName"
            echo Renamed $f to $newFileName
            i=$((i+1));

        #Dealing with JPGs
        elif [[ $f == *".jpg"* ]]
        then
            newFileName="Screenshot_$i.jpg";
            mv "$f" "$newFileName"
            echo Renamed $f to $newFileName
            i=$((i+1))
        fi
    fi
done

echo Renamed all files
