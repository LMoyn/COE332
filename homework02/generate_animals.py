#!/usr/bin/env python3
import petname
import json
import sys

#Declares a list of dicionaries
#Each dictionary describes a single animal
animals = [dict() for x in range(20)]

#Gives head choices
heads = ['snake', 'bull', 'lion', 'raven', 'bunny']

#Loops over the 20 animals we generate
iterator = 0
while iterator < 20:
    animals[iterator]['head'] = petname.random.choice(heads)
    #Generates two animal names and concatenates them to make the body
    body1 = petname.name()
    body2 = petname.name()
    body = body1 + "-"+body2
    animals[iterator]['body'] = body
    animals[iterator]['arms'] = 2*petname.random.randint(1,5)
    animals[iterator]['legs'] = 3*petname.random.randint(1,4)
    animals[iterator]['tail'] = animals[iterator]['arms']+animals[iterator]['legs']
    iterator = iterator +1

#Stores the animal list in the json file
with open(sys.argv[1], 'w') as f:         
    json.dump(animals, f, indent=2)  