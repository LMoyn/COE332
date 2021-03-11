# COE332 homework03

The homework02 folder contains modified generate_animals.py and read_animals.py code that allows for the user to decide the name of the JSON file to read/write to at runtime. Additionally, the read_animals.py script has been modified and contains a breedAnimals() function which takes in the data from two animals and returns data for a new animal that inherets traits from its parents. A test_read_animals.py script performs unit tests to verify that this code functions as expected by checking if the traits possessed by offspring are consistent with the ones possessed by parents.

The homework02 folder also contains a dockerfile. This lets the user to containerize the code, which allows for the dependencies to be shipped together and ensures that the scripts run under the same conditions no matter where they are run.

# Instructions on how to download and run the scripts directly

The repository may be downloaded by using

`git pull https://github.com/LMoyn/COE332.git`

in the terminal. To run the scripts, first navigate to the appropriate subfolder. The homework02 read_animals.py and generate_animals.py must be provided with the name of the JSON file to read/write to. To generate animals and store them in a file called "animals.json", use

`python3 generate_animals.py animals.json`

and

`python3 read_animals.py animals.json`

# Instructions on how to build an image with the Dockerfile provided

The code in the homework02 folder may be containerized by using

`docker build -t username/json-parser:1.0 .`

in the terminal. "username" should be replaced with the user's Dockerhub username. 

# Instructions on how to run use the containerized scripts
Our container may be accessed by using

`docker run --rm -it username/json-parser:1.0 /bin/bash`

Inside the container, our code can be run as described in the previous sections. exit the container by typing `exit`

Once the scripts are containerized, they can be run without entering the container using `docker run`. To run the generate_animals.py script and store the animals in a file called animals.json, use

`docker run --rm -v $PWD:/data username/json-parser:1.0 generate_animals.py /data/animals.json`

Similarly, the read_animals.py script can read off the animals.json file using

`docker run --rm -v $PWD:/data username/json-parser:1.0 read_animals.py /data/animals.json`

# Instructions on how to run the unit test

test_read_animals.py is run in the same manner as the homework01 scripts. In the terminal in the homework02 folder, write

`python3 test_read_animals.py`
