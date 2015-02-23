#The Story

###2014
Throughout all of 2014, I had the Samsung Galaxy S4. I primarily used stock-apps with the exception of texting (QKSMS) and camera (switched to using Google Camera in May 2014)

I would backup my photos to Google+ Photos, where they would remain hidden.

###What went wrong - Multifold

+ Many, many duplicates
    - If I took a photo on Snapchat and downloaded the snap, the photo would show up in two folders: 'All Photos' and 'Snapchat'
    - I had the enhance quality enabled on Google+ Photos so for every photo I backed up, Google+ would store two versions: a slightly compressed version of the original photo I took on my device (Version B) and an edited/enhanced version (Version C). I did not know about the 'Version C' photo until I downloaded all of my Google+ Photos to my computer and looked through them

+ SD Card problems
    - On Android version 4.4 (Kitkat), Google had taken steps to stop rogue apps from viewing other apps' data stored on the SD card by restricting what data could be stored on the card and which apps had access to it
    - For some unknown reason - probably because of TouchWiz + Kitkat - I was unable to store my photos on my SD Card. I was also unable to store my downloaded songs/playlists from Spotify (Spotify Premium user) to my SD card, most likely because of Spotify. 
    - I decided it was best to root my 16GB Galaxy S4 in order to use an app that would trick apps into thinking my SD card was internal memory and would allow me to store a ton of apps' data on my SD card
        + My phone became setup like this: Spotify music on SD Card, old photos on SD card, newest photos on phone's internal memory before being moved to SD Card when space ran out. Also, all photos were backed up to Google+.
    - Worked well until I was halfway through my trip to Vienna, Salzburg, and Prague. For some weird reason, something happened to the write permissions that did not allow me to move my photos from my internal memory to SD Card. **I lost over 450 photos of the most historic and beautiful places in Vienna and Salzburg because Samsung 'successfully moved' photos to the SD card when it really did not**.
    - I thought it was a glitch and continued on with my trip, but the problems just got worse and worse.
    - In July, my write problems were severe - I could not even delete files from the SD card - and I broke the card in half and sent it to SanDisk to get a replacement 64GB SD card (under warranty)
    - I kept a few photos on that SD card, but nothing from that year's earlier trips to **London, Paris, Salzburg, Vienna, and Prague**.

###Fast-forward a few months

+ I converted to iOS/iPhone 6 and absolutely loved it. When I made the switch, I was able to successfully transfer all the photos on my Android phone (both internal memory and SD card) to my new iPhone
    - Unfortunately, I still had a lot of duplicate photos (ie. screenshots and snapchat downloads that were saved twice)
    - Some of the photos and dates were off

+ I eventually became frustrated with the duplicate, out-of-order photos and decided I would somehow transfer all the photos backed up to Google+ to my iPhone

###The problem

+ When I downloaded my photos from Google+ as a 10.5GB .tgz file, I discovered that:
    - Not only were there the duplicate photos, but there were also other edited/enhanced copies Google+ stored but did not display on either the Google+ Photos website or Photos section of the Google+ app. 
    - The dates were completely wrong on a significant number of the photos, which meant that when I transferred them to my iPhone, they would show up incorrect spots on the Photos app 
    - File names were really different and not uniform
        + Some photos saved from my iTouch (back in 2013) were saved in the typical iOS-taken-photo format: IMG_NUMBER.jpg
        + Photos from my Galaxy S4 were saved as DATE_TIME_NUMBER.jpg
        + Miscellaneous screenshots & downloaded photos were saved completely differently

###The silver lining

+ Even though the photo date-added and date-edited timestamp was wrong, it was still in a folder named with the photo's correct date taken stamp (YEAR_DAY_MONTH)
    - One slight problem was that multiple back-ups on the same day caused multiple folders (ie. 'DATE', 'DATE #2', 'DATE #3')
+ The edited/enhanced photos Google+ added were uniform ie. ORIGINAL_FILE_NAME-EDITED.jpg

###What I did

+ Decided to solve this problem programmatically

1. Delete duplicated photos
    + 'GoogleDuplicatePhotoRemover.java' recursively looks through all the photos in folders of a directory and deletes the original photo if it finds an enhanced version of that photo
2. Merge the directories with photos taken on the same day
    + 'MergeDirectories.java' looks at all the directory names inside a folder and if it finds names like 'DATE' 'DATE #2' 'DATE #3', moves all the photos from 'DATE #2' and 'DATE #3' to 'DATE'
3. Reset the file created time and date to the day it was created
    + 'ResetImageTimes.java' resets the date created timestamp of each photo in a directory to a date version of that directory's name and changes the image's name to a uniform version
    + For example, if a folder is named: 2015-02-22
        - Images in that folder would be named 2015-02-22_01.jpg 2015-02-22_02.jpg 2015-02-22_03.jpg
        - The date created/last modified timestamp of that photo would be: "Sunday, February 22nd 2015"


#My solution worked and I was able to successfully transfer all the photos backed up to Googel+ to my iPhone 6 :) 
