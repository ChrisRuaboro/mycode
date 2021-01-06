#!/usr/bin/env python3

#prompt user
userfilechoice = input("whats your file name: \n")

## create file object in "r"ead mode
with open(userfilechoice, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(len(configlist))
