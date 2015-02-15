#/bin/bash

JSONResult=$(python2 -c "import urllib; print urllib.urlopen(\"http://po.st/api/shorten?longUrl=facebook.com&apiKey=3E5C05F5-DDED-4485-A193-F486E947F547\",'r').read()")

echo $JSONResult
