#!/usr/bin/env python3
import json
import random
import sys

#Gives an animal resulting from the mixing of two input animals' traits
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

    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)

    print(random.choice(animals['animals']))

if __name__ == '__main__':
    main()
