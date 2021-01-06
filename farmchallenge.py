#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
         
animals = ["sheep","cow","pigs","chickens", "llamas","cats"]

for farm in farms:
    if farm["name"] == "NE Farm":
        print(farm["agriculture"])

def getfarmslist():
    x = []
    for farm in farms:
        option = farm["name"].replace(" Farm", "")
        x.append(option)
        
    return x
def getanimals(farm):
    animalsonfarm = []
    for element in farm["agriculture"]:
        if element in animals:
            animalsonfarm.append(element)
    return animalsonfarm
userfarmchoice = input("Choose a farm to view: " + str(getfarmslist()))

farmlist = getfarmslist()
if userfarmchoice in farmlist:
    userfarmchoicekey = userfarmchoice + " Farm"
    for farm in farms:
        if userfarmchoicekey == farm["name"]:
            print(farm)
            break
else:
        print(f"{userfarmchoice} not in list")
        
        
userfarmchoiceanimals = input("Choose a farm to view it animals: " + str(getfarmslist()))


if userfarmchoiceanimals in farmlist:
    userfarmchoicekey = userfarmchoice + " Farm"
    for farm in farms:
        if userfarmchoicekey == farm["name"]:
            print(getanimals(farm))
else:
        print(f"{userfarmchoiceanimals} not in list")
