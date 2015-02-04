#Discovering the SMS protocol vulnerability that affects all Verizon phones

---

###How an exploit allows a man-in-the-middle attacker to spoof an SMS to any Verizon phone and allow the impersonation of any phone number and organization.

####2014
+ **Mid-December**: 
	- Viewed a question asking for help with writing a script that would send a notification to OSX's Notification Center after a bash process finished. 

	- I thought writing a similar script that sent a text notification from the command-line would be an interesting project, so I recorded it as an idea for a post-college-essay project.


####2015
+ **January 30th**: 
	- Began work on the script and chose to use SendGrid's API because: 
		+ 200 free messages a day <-- More than enough
		+ Familiarity with the API from previous projects
	
	- Finished writing the script (working version). Included: 
		+ Hiding the confidential username and password in a separate Python file and referring to it in a similar way as Java developers do with a .properties file
		+ Sending a text to my phone with a message inputted during run-time
	- **Important:** Discovered that I could send texts to my *Verizon iPhone 6* model *MG652LL/A* running *iOS 8.1.3* from the text string "Ryans MacBook Pro Command Line", though when the text was received, the from address was the spaceless version ("RyansMacbookProCommandLine")
+ 
+ 