#/bin/bash

#Sends a request to the po.st API with the long url. po.st returns JSON with result information
JSONResult=$(python2 -c "import urllib; print urllib.urlopen(\"http://po.st/api/shorten?longUrl=$1&apiKey=3E5C05F5-DDED-4485-A193-F486E947F547\",'r').read()")

#Parses result to see if it was successful
Success=$(node -pe 'JSON.parse(process.argv[1]).status_txt' "$JSONResult")

if [ "$Success" == "OK" ] then
    echo YES
fi

echo $Success

