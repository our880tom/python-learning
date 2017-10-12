from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
	         "Nice job, you died ...jackass.",
	         "Such a luser.",
	         "I have  a small puppy that's better at this."]
	print quips[randint(0, len(quips)-1)]
	exit(1)

def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	print "your entire crew. You are the last surviving member and your last"
	print "mission is to get the "