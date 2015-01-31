#Runs a python script to send a text to my phone
alias TextPhone="python /Users/Ryan/Dropbox/All\ Good\ Programming\ Books/dotfiles/TextPhone.py"

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
