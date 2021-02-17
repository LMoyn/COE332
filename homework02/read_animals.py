#!/usr/bin/env python3
import json
import petname
import sys

#Prints information for the animal at the provided index
def printAnimal(animalIndex,animals):
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

#Prints an animal resulting from the mixing of two input animals' traits
def breedAnimals(firstParentIndex, secondParentIndex, animals):
    offspring = dict()
    #Randomly selects to have one of the parents' body's and head
    offspring['head'] = petname.random.choice([animals[firstParentIndex]['head'], animals[secondParentIndex]['head']])
    
    #Creates a list containing both animals making up each body
    parent1_body_animals = (animals[firstParentIndex]['body']).split("-")
    parent2_body_animals = (animals[secondParentIndex]['body']).split("-")

    body1 = petname.random.choice([parent1_body_animals[0], parent1_body_animals[1]])
    body2 = petname.random.choice([parent2_body_animals[0], parent2_body_animals[1]])
    offspring_body = body1 + "-"+body2
    offspring['body'] = offspring_body
    
    #Averages the number of arms and legs of the parents to get offspring data
    offspring['arms'] = round((animals[firstParentIndex]['arms'] + animals[secondParentIndex]['arms'] )/2)
    offspring['legs'] = round((animals[firstParentIndex]['legs'] + animals[secondParentIndex]['legs'] )/2)
    offspring['tail'] = offspring['arms'] + offspring['legs']
    return offspring
    

def main():
    #Opens the json file
    with open(sys.argv[1], 'r') as f:       
    animals = json.load(f)  

    #Selects a random index telling us which of the animals in the json file will be printed
    parent1Index = petname.random.randint(0,20-1)
    parent2Index = petname.random.randint(0,20-1)
    while(parent1Index == parent2Index):
        parent2Index = petname.random.randint(0,20-1)
    print("First Parent:")
    printAnimal(parent1Index,animals)
    print("Second Parent:")
    printAnimal(parent2Index,animals)
    print("Offspring:")
    offspring = breedAnimals(parent1Index,parent2Index,animals)
    #Prints the offspring data in a readable form
    #Concatenation of text and data
    print("head: "+offspring['head'])
    print("body: "+offspring['body'])
    #String conversion of integer data
    print("arms: "+str(offspring['arms']))
    print("legs: "+str(offspring['legs']))
    print("tail: "+str(offspring['tail']))

if __name__ == '__main__':
    main()