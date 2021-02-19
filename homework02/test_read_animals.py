#!/usr/bin/env python3
import unittest
import json
import sys
from read_animals import breedAnimals

class Test_read_animals(unittest.TestCase):

    def test_breedAnimals(self):
        #Opens the json file
        with open(sys.argv[1], 'r') as f:
        	animals = json.load(f)

        #The codes tests over parent pairs with the (x,y) pairs below as their indices
        xlist = [1,3,7,10,19]
        ylist = [7,18,5,13,9]
        iterator = 0
        while iterator < len(xlist):
            #Performs checks for the offspring of a the xth and yth animals
            x = xlist[iterator]
            y = ylist[iterator]

            parent1 = animals[x]
            parent2 = animals[y]
            offspring = breedAnimals(x,y,animals)

            #Checks that the head is the same as the head of one of the parents

            parent1_in_head = (parent1['head']) in offspring['head']
            parent2_in_head = parent2['head'] in offspring['head']
            self.assertTrue(parent1_in_head or parent2_in_head)

            #Creates a list containing both animals making up each body
            parent1_body_animals = parent1['body'].split("-")
            parent2_body_animals = parent2['body'].split("-")

            #Checks that at least one animal from each of the parents' bodies
            #Are present in the offspring body
            parent1_in_offspring_body = parent1_body_animals[0] in offspring['body'] or parent1_body_animals[1] in offspring['body']
            parent2_in_offspring_body = parent2_body_animals[0] in offspring['body'] or parent2_body_animals[1] in offspring['body']
            self.assertTrue(parent1_in_offspring_body and parent2_in_offspring_body)

            #Checks that the number of arms matches what we get from averaging the values from the parents
            average_arms = round((parent1['arms'] + parent2['arms'] )/2)
            self.assertEqual(average_arms,offspring['arms'])

            #Checks that the number of legs matches what we get from averaging the values from the parents
            average_legs = round((parent1['legs'] + parent2['legs'] )/2)
            self.assertEqual(average_legs,offspring['legs'])

            #Checks that the tail is what we expect from the arm and leg values
            self.assertEqual(average_arms+average_legs, offspring['tail'])

            iterator = iterator + 1

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as f:                                                                                                                                    animals = json.load(f)   
	unittest.main()
