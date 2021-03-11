# COE332 homework03

This is the third homework for COE332. A Flask app was developed that can return information from an included animals.json file. The app can be run directly or through a Docker container, and instructions for both use cases are provided.

# Instructions on how to download and run the scripts directly

The repository may be downloaded by using

```bash
git pull https://github.com/LMoyn/COE332.git
````

in the terminal. To run the scripts, first navigate to the appropriate subfolder /homework03 

# Instructions on how to build an image with the Dockerfile provided

Before containerizing, it is necessary to navigate to the /web directory

The code in the homework03 folder may be containerized by using

```bash
docker build -t <image_name>:latest .
```

in the terminal.

# Instructions on how to run use the containerized scripts
Our container may be accessed by using

```bash
docker run --name "give your container a name" -d -p <your portnumber>:5000 <image_name>
```

We can verify that the container is running by looking at the list of containers which appears after entering

```bash
docker ps -a
```

The container can be stopped by using

```bash
docker stop <image_name>
```

And it can be removed with

```bash
docker rmi <image_name>
```

#Using the Flask App

Before using the flask app, one must eneter the follow from the terminal:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -h localhost -p <your portnumber>
```

The app has the following functionality:

-Return all animals in animals.json:

```bash
curl localhost:<your portnumber>/animals.
```

-Return all animals in animals.json with a user defined head type:

```bash
curl localhost:<your portnumber>/animals/head/<head>.
```

-Return all animals in animals.json with a user defined number of legs:

```bash
curl localhost:<your portnumber>/animals/legs/<num_legs>.
```

The animal_consumer.py script uses this functionality. It may be run from the command line using

```bash
python3 animal_consumer.py
```

The Response1, Response2, and Response3 outputs use the functionality in the order they are described above.

The port number in the animals_consumer.py file may also be edited to access another student's Flask app.
