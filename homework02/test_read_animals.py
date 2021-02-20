#!/usr/bin/env python3
import unittest
import sys
import petname
from read_animals import breedAnimals

class Test_read_animals(unittest.TestCase):
   
    def test_breedAnimals(self):

        #Generates a set of animals to test over
        animal_dict = {}
        animal_dict['animals'] = []
        
        for i in range(20):
            this_animal = {}
            this_animal['head'] = petname.random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])
            this_animal['body'] = petname.name() + '-' + petname.name()
            this_animal['arms'] = petname.random.randint(1,5) * 2
            this_animal['legs'] = petname.random.randint(1,4) * 3
            this_animal['tail'] = this_animal['legs'] + this_animal['arms']
            animal_dict['animals'].append(this_animal)
        
        animal_list = animal_dict['animals']

        #The codes tests over parent pairs with the (x,y) pairs below as their indices
        x = 0
        y= 0
        while x < 20:
            y = 0
            while y < 20:
            #Performs checks for the offspring of a the xth and yth animals
            
                parent1 = animal_list[x]
                parent2 = animal_list[y]
                offspring = breedAnimals(x,y,animal_list)

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

                y = y+1
            x = x+1

if __name__ == '__main__':
    unittest.main()