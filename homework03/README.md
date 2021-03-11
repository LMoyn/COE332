# COE332 homework03

The homework03 folder also contains a dockerfile. This lets the user to containerize the code, which allows for the dependencies to be shipped together and ensures that the scripts run under the same conditions no matter where they are run.

# Instructions on how to download and run the scripts directly

The repository may be downloaded by using

```bash
git pull https://github.com/LMoyn/COE332.git
````

in the terminal. To run the scripts, first navigate to the appropriate subfolder. The homework03 

# Instructions on how to build an image with the Dockerfile provided

Before containerizing, it is necessary to navigate to the \web directory

The code in the homework03 folder may be containerized by using

```bash
docker build -t <image_name>:latest .
```

in the terminal. "username" should be replaced with the user's Dockerhub username. 

# Instructions on how to run use the containerized scripts
Our container may be accessed by using

```bash
docker run --name "give your container a name" -d -p <your portnumber>:5000 <image_name>
```

Inside the container, our code can be run as described in the previous homework's READMEs. exit the container by typing `exit`


Once the scripts are containerized, they can be run without entering the container using `docker run`. To run the generate_animals.py script and store the animals in a file called animals.json, use

```bash
docker run --rm -v $PWD:/data username/json-parser:1.0 generate_animals.py /data/animals.json`
```

Similarly, the read_animals.py script can read off the animals.json file using

```bash
docker run --rm -v $PWD:/data username/json-parser:1.0 read_animals.py /data/animals.json
```

#Using the Flask App

Before using the flask app, one must eneter the follow from the terminal:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -h localhost -p <port>
```

The app has the following functionality:

-Return all animals in animals.json:

```bash
curl localhost:<port>/animals.
```

-Return all animals in animals.json with a user defined head type:

```bash
curl localhost:<port>/animals/head/<head>.
```

-Return all animals in animals.json with a user defined number of legs:

```bash
curl localhost:<port>/animals/legs/<num_legs>.
```

The animal_consumer.py script uses this functionality. It may be run from the command line
