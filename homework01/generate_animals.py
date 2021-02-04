import petname
import json

#Declares a list of dicionaries
#Each dictionary describes a single animal
animals = [dict() for x in range(20)]

#Loops over the 20 animals we generate
iterator = 0
while iterator < 20:
    animals[iterator]['head'] = petname.name()
    #Generates two animal names and concatenates them to make the body
    body1 = petname.name()
    body2 = petname.name()
    body = body1 + "-"+body2
    animals[iterator]['body'] = body
    animals[iterator]['arms'] = petname.random.randint(1,6)
    animals[iterator]['legs'] = petname.random.randint(2,12)
    animals[iterator]['tail'] = animals[iterator]['arms']+animals[iterator]['legs']
    iterator = iterator +1

#Stores the animal list in the json file
with open('animals.json', 'w') as out:
    json.dump(animals,out,indent = 2)