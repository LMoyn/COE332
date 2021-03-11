# COE332 homework03

The homework03 folder also contains a dockerfile. This lets the user to containerize the code, which allows for the dependencies to be shipped together and ensures that the scripts run under the same conditions no matter where they are run.

# Instructions on how to download and run the scripts directly

The repository may be downloaded by using

`git pull https://github.com/LMoyn/COE332.git`

in the terminal. To run the scripts, first navigate to the appropriate subfolder. The homework03 

# Instructions on how to build an image with the Dockerfile provided

The code in the homework03 folder may be containerized by using

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


