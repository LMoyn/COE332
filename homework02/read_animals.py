import json
import petname

#Opens the json file
with open('animals.json', 'r') as f:
    animals = json.load(f)

#Selects a random index telling us which of the animals in the json file will be printed
animalIndex = petname.random.randint(0,20-1)
#Prints the animal data for this index
animal = animals[animalIndex]
print(animal)
#Prints the animal data in a readable form
#Concatenation of text and data
print("head: "+animal['head'])
print("body: "+animal['body'])
#String conversion of integer data
print("arms: "+str(animal['arms']))
print("legs: "+str(animal['legs']))
print("tail: "+str(animal['tail']))

