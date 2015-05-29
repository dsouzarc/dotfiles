export PATH=/path/to/dir:$PATH

#Copy current directory to clipboard
alias cpwd='pwd | xclip -selection clipboard'

#Quickly find file
alias ff='find . -type f -name'

#Quickly find directory
alias fd='find . -type d -name'

#get internet speed
alias speedtest='wget -O /dev/null http://speedtest.wdc01.softlayer.com/downloads/test500.zip'

#Short form for where most of my code is stored
dboxprogram="~/Dropbox/All\ Good\ Programming\ Books"

#DOTFILES SHORTCUTS
dotfiles="$dboxprogram/dotfiles"

#Counts number of files in directories and subdirectories
alias countall="find */ -type f | wc -l"

#Runs a python script that converts an image to all the necessary sizes for an iOS app
alias iOSImageConverter="python $dotfiles/Python/iOSAppIconResizer.py"

#Runs a python script to email a file to myself as an attachment
alias EmailAttachment="python $dotfiles/Python/EmailAttachment.py"
alias EmailAttch="EmailAttachment"

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

#Prints the definition of a word and its usage in a sentence
alias define="python $dotfiles/Python/Dictionary.py"

#Prints current external IP Address
alias myIP="curl http://api.ipify.org; echo" #Other option: 'curl ifconfig.me'
alias myip="myIP"

#Prints local IP Address
alias myIPL="ipconfig getifaddr en1"
alias myipl="myIPL"

#Go places
alias toprogramming="cd $dboxprogram"
alias toalgos="toprogramming; cd Algorithms\ and\ Data\ Structures"
alias todotfiles="toprogramming; cd dotfiles"
alias toios="cd ~/iOS\ Development"
alias topython="toprogramming; cd Python"
alias todownloads="cd; cd Downloads"
alias tobmf="toprogramming; cd Bring\ Me\ Food"
alias tocharles="toprogramming; cd Charles\ Proxying"

#Downloads any website's content
downloadsite() {
    wget  --random-wait  -r  -p  -e  robots=off  -U  mozilla $1
}

#Normal ls but displays '/' for directories 
alias ls="ls -CF"

#Lists only the directories in a directory
alias lsd="ls -d */"

#Lists only the directories in a directory but in fancy formatting
alias lsdf="ls -d */ | cut -f1 -d'/'"

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

#Copy file to clipboard
copyfile() {
    cat $1 | xclip -selection clipboard
}

#Last 10 modified files
last() {
    ls -lt -a $1 | head
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

#Whether to use .bashrc or other files
if [ -f $HOME/.bash_aliases ]
then
  . $HOME/.bash_aliases
fi

#Causes the changes to .bashrc to come true
alias bashme="cp ~/.bashrc ~/.bash_profile; source ~/.bashrc"
