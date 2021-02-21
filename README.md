# COE332

This repository contains my homework submissions for COE332. Each subfolder contains a specific assignment.

The homework homework01 folder contains a generate_animals.py script which creates an animals.json file containing data describing 20 animals, and the read_animals.py script reads over the animal data of this JSON file and prints information for a random animal.

The homework02 folder contains modified generate_animals.py and read_animals.py code that allows for the user to decide the name of the JSON file to read/write to at runtime. Additionally, the read_animals.py script has been modified and contains a breedAnimals() function which takes in the data from two animals and returns data for a new animal that inherets traits from its parents. A test_read_animals.py script performs unit tests to verify that this code functions as expected.

The homework02 folder also contains a dockerfile. This lets the user to containerize the code, which allows for the dependencies to be shipped together and ensures that the scripts run under the same conditions no matter where they are run.

# Instructions on how to download and run the scripts directly

The repository may be downloaded by using




in the terminal



# Instructions on how to build an image with the Dockerfile provided




# Instructions on how to run the scripts inside a container



# Instructions on how to run the unit test(s)


