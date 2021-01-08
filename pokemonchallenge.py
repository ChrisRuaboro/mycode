#!/usr/bin/env python3

# imports always go at the top of your code
import requests


def validpokemon(chosenpokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{chosenpokemon}")
    if response.status_code != 200:
        return False
    else:
        return True


def lookuppokemon(chosenpokemon):
    while validpokemon(chosenpokemon):
        pokedata = requests.get(f"https://pokeapi.co/api/v2/pokemon/{chosenpokemon}").json()
        return pokedata


def grabimageurl(pokedata):
    imageurl = pokedata["sprites"]["front_default"]
    return imageurl


def getgameindices(pokedata):
    count = len(pokedata["game_indices"])
    return count


def getpokemonmoves(pokedata):
    moves = []
    for move in pokedata["moves"]:
        moves.append(move["move"]["name"])
    return moves


def getgamesappearedin(pokedata):
    games = []
    gameindices = pokedata["game_indices"]
    for indice in gameindices:
        games.append(indice["version"]["name"])
    return games


def displaylist(list):
    for item in list:
        print(item)


def main():
    userpokedata = {}
    while True:
        userinput = input("What pokemon do you want to search up?\n")
        userpokedata = lookuppokemon(userinput)
        if userpokedata is None:
            print(f"{userinput} doesn't exist.")
        else:
            break
    # Print the URL to "front_default", which is a link to an image of your Pokemon!
    imageurl = grabimageurl(userpokedata)
    print("Here's your Pokemon's picture!\n", imageurl, sep="")

    # Return a count of how many "game_indices" the selected Pokemon has been in!
    usersgameindices = getgameindices(userpokedata)
    print(f"{userinput} appeared in {usersgameindices} games")
    appearedin = getgamesappearedin(userpokedata)
    displaylist(appearedin)

    # Print out the "name"s of ALL the selected Pokemon's "moves".
    userspokemoves = getpokemonmoves(userpokedata)
    print(f"{userinput}'s moves are ")
    displaylist(userspokemoves)
    # print(imageurl)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

