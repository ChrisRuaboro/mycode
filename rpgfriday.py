#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

import random


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


def enterCombat(enemy, deterrent="deterrent"):
    print(f"Since you didn't have a {deterrent}, you are now in combat with {enemy}")
    playeralive = True
    # Player always enters with 100 health
    playerhealth = 100
    enemyhealth = 100
    choices = ['attack', 'run']
    while enemyhealth >= 0:
        playerchoice = input(choices)
        if playerchoice == "attack":
            print(f"Attacking {enemy}")
            # Get random damage amount
            attackdamage = random.randint(0, 100)
            print(f"You did {attackdamage} to {enemy}")
            # Subtract damage from enemy health
            enemyhealth -= attackdamage
            if enemyhealth > 0:
                print(f"{enemy} is at {enemyhealth}")
            if enemyhealth <0 :
                print(f"{enemy} defeated!")
                break
        elif playerchoice == "run":
            ## TODO implement updating currentRoom to lastroomentered
            break
    if enemyhealth <= 0:
        # Monster defeated, take him out of the room
        del rooms[currentRoom]['item']
    # Players dead change player alive
    if playerhealth <= 0:
        playeralive = False
    # Returning if player won, ran, or lost
    return playeralive


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room',
        'east': 'Labyrinth',
        'item': 'gardening boots',
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    },
    'Labyrinth': {
        'west': 'Labyrinth',
        'north': 'Labyrinth',
        'south': 'Labyrinth',
        'east': 'Labyrinth',
        'northeast': 'Garden',
        'item': 'spike traps',
    }
}

# start the player in the Hall
currentRoom = 'Hall'
lastenteredroom = ''

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            lastenteredroom = currentRoom
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' obtained!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster BUT HAS A COOKIE
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
        print('The monster takes your cookie and runs away! Whew!')
        del rooms[currentRoom]['item']
        inventory.remove('cookie')

    ## If a player enters a room with a monster and has no cookie
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster is here')
        enemy = rooms[currentRoom]['item']
        playerwon = enterCombat(enemy, 'cookie')
        if not playerwon:
            break

    ## If a player enters a room with spike traps BUT HAS gardening boots on
    if 'item' in rooms[currentRoom] and 'spike traps' in rooms[currentRoom]['item'] and 'gardening boots' in inventory:
        print('Spike Traps activated from below! Good thing you had Gardening Boots')
        del rooms[currentRoom]['item']

    ## If a player enters a room with spiketraps
    elif 'item' in rooms[currentRoom] and 'spike traps' in rooms[currentRoom]['item']:
        print('Get spiked noob! GAME OVER!')
        break

    ## If player enters Labyrinth
    if currentRoom == 'Labyrinth':
        hint = "The direction you are looking for is in between what you normally choose"
        print(hint)

