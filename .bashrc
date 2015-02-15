export PATH=/path/to/dir:$PATH

#Runs a python script that converts an image to all the necessary sizes for an iOS app
alias iOSImageConverter="python /Users/Ryan/Dropbox/All\ Good\ Programming\ Books/dotfiles/Python/iOSAppIconResizer.py"

#Runs a python script to send a text to my phone
alias TextPhone="python /Users/Ryan/Dropbox/All\ Good\ Programming\ Books/dotfiles/Python/TextPhone.py"

#Runs a python script that sends a link to my phone
alias TextLink="python /Users/Ryan/Dropbox/All\ Good\ Programming\ Books/dotfiles/Python/TextLink.py"

#Runs a bash script to shorten a link, print the shortened URL, and copy it to clipboard
alias ShortenLink="/Users/Ryan/Dropbox/All\ Good\ Programming\ Books/dotfiles/Bash/./ShortenURL.sh"

#Prints current external IP Address
alias myIP="curl http://api.ipify.org; echo"
alias myip="myIP"

#Normal ls but displays '/' for directories 
alias ls="ls -CF"

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
alias bashme="cp .bashrc .bash_profile; source .bashrc"

#Whether to use .bashrc or other files
if [ -f $HOME/.bash_aliases ]
then
  . $HOME/.bash_aliases
fi
