#!/usr/bin/env python3

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

print("Welcome, today we determine your yeet strength!")

while True:
    try:
        yeet_distance = float(input("How many feet do you think you can throw a baseball?"))
        break
    except:
        print("Bruh we need a number.")

yeetstrength = " "
totalyeetdistance = 0
totalboosted = 1

def initiateBoosters():
    global totalboosted
    boosted = 1
    for _ in range(3):
        input("Press ENTER to boost your yeet distance!")
        boostmultiply = randint(0,20)
        boosted *= boostmultiply
        print(f"With a random boost of {boostmultiply}, for a total boost of {boosted}")
    totalboosted = boosted

initiateBoosters()

totalyeetdistance = totalboosted * yeet_distance

print(f"Total yeet distance is {totalyeetdistance}")

if totalyeetdistance <= 2500:
    yeetstrength = "Spongebob Arms"
    print("Your yeet strength is:", yeetstrength)

elif totalyeetdistance <= 8999:
    yeetstrength = "small yeet energy"
    print("Your yeet strength is:", yeetstrength)

elif totalyeetdistance <= 15000:
    yeetstrength = "OVER9000!!!"
    print("Your yeet strength is:", yeetstrength)

elif totalyeetdistance <= 25000:
    yeetstrength = "BIG YEET ENERGY"
    print("Your yeet strength is:", yeetstrength)

else:
    yeetstrength = "Elon Musk sending a Telsa Roadster into space"
    print("Your yeet strength is:", yeetstrength)
