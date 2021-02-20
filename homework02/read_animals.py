#!/usr/bin/env python3
import json
import petname
import sys

#Gives an animal resulting from the mixing of two input animals' traits
def breedAnimals(firstParentIndex, secondParentIndex, animals_dict):
    offspring = {}
    

    #Randomly selects to have one of the parents' body's and head
    offspring['head'] = petname.random.choice([ animals_dict[firstParentIndex]['head'], animals_dict[secondParentIndex]['head'] ])
    
    #Creates a list containing both animals making up each body
    parent1_body_animals = (animals_dict[firstParentIndex]['body']).split("-")
    parent2_body_animals = (animals_dict[secondParentIndex]['body']).split("-")

    body1 = petname.random.choice([parent1_body_animals[0], parent1_body_animals[1]])
    body2 = petname.random.choice([parent2_body_animals[0], parent2_body_animals[1]])
    offspring_body = body1 + "-"+body2
    offspring['body'] = offspring_body
    
    #Averages the number of arms and legs of the parents to get offspring data
    offspring['arms'] = round((animals_dict[firstParentIndex]['arms'] + animals_dict[secondParentIndex]['arms'] )/2)
    offspring['legs'] = round((animals_dict[firstParentIndex]['legs'] + animals_dict[secondParentIndex]['legs'] )/2)
    offspring['tail'] = offspring['arms'] + offspring['legs']
    return offspring

def main():

    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)

    animal_dict = animals['animals']
    print(petname.random.choice(animal_dict))
    parent1 = petname.random.randint(0,19)
    parent2 = petname.random.randint(0,19)
    child = breedAnimals(parent1, parent2, animal_dict)
    print(child)

if __name__ == '__main__':
    main()