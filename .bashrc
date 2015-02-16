export PATH=/path/to/dir:$PATH

#Short form for where most of my code is stored
dboxprogram="/Users/Ryan/Dropbox/All\ Good\ Programming\ Books"

#DOTFILES SHORTCUTS
dotfiles="$dboxprogram/dotfiles"

#Runs a python script that converts an image to all the necessary sizes for an iOS app
alias iOSImageConverter="python $dotfiles/Python/iOSAppIconResizer.py"

#Runs a python script to send a text to my phone
alias TextPhone="python $dotfiles/Python/Textphone.py"

#Runs a python script that sends a link to my phone
alias TextLink="python $dotfiles/Python/TextLink.py"

#Runs a python script to text people
alias TextPeople="python $dotfiles/Python/TextPeople.py"

#Runs a python script to email stuff to myself
alias EmailLink="python $dotfiles/Python/EmailLink.py"
alias EmailMe="python $dotfiles/Python/EmailMe.py"

#Runs a bash script to shorten a link, print the shortened URL, and copy it to clipboard
alias ShortenLink="$dotfiles/Bash/./ShortenURL.sh"

#Prints current external IP Address
alias myIP="curl http://api.ipify.org; echo"
alias myip="myIP"

#Go places
alias toprogramming="cd $dboxprogram"
alias toalgos="toprogramming; cd Algorithms\ and\ Data\ Structures"
alias todotfiles="toprogramming; cd dotfiles"
alias toios="cd /Users/Ryan/iOS\ Development"
alias topython="toprogramming; cd Python"
alias todownloads="cd; cd Downloads"

#Normal ls but displays '/' for directories 
alias ls="ls -CF"

#Shortens git commiting everything
commitall() {
    git add --all

    #Gets all the input into one string
    message="$*"

    git commit -m "$message"
}

#Prints the contents of that directory. No formatting
peekn() {

    #If there is no input directory, print the current one
    if [ -z "$1"] 
    then
        ls

    #But if there is an input
    else
        #Get into it
        cd $1

        #Print in nice columns format
        ls

        #Go back
        cd ..
    fi
}

#Prints the contents of that directory in a nice format
peek() {

    #If there is no input directory, print the current one
    if [ -z "$1"] 
    then
        ls | column -c 200

    #But if there is an input
    else
        #Get into it
        cd $1

        #Print in nice columns format
        ls | column -c 200

        #Go back
        cd ..
    fi
}

#Make a directory and navigate into it
mcd() { 
    mkdir -p $1
    cd $1
}

#Convert all .jpg files to .png
pngtojpg() { 
    for i in *.jpg ; do 
        convert "$i" "${i%.*}.png"
    done
}

#Convert all .png files to .jpg
jpgtopng() { 
    for i in *.png ; do
        convert "$i" "${i%.*}.png"
    done
}

#Causes the changes to .bashrc to come true
alias bashme="cp ~/.bashrc ~/.bash_profile; source ~/.bashrc"

#Whether to use .bashrc or other files
if [ -f $HOME/.bash_aliases ]
then
  . $HOME/.bash_aliases
fi
