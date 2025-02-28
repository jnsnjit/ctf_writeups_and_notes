#!/bin/bash
#working for centos linux distro!!

#check for user input file
if [[! username.txt ]]; then
    echo "text file not found"
    exit 1
fi

INPUTF = "$1"
#read line by line, split into words
while IFS=read -r line; do
    words = ($line) #spline line into its words
    sudo adduser -m "${words[2]}"
    echo "${words[2]}:${words[3]}" | sudo chpasswd
done > usernames.txt
echo "ran sucessfully!"

#notes: change username file when needed
# in this case, the third word in each line is the username, and the fourth is password
# change script accordingly