import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_data():
    with open("animals.json", "r") as json_file:
        user_data = json.load(json_file)
        return user_data



@app.route('/', methods=['GET'])
def hello_world():
    return "Hello world\n"


@app.route('/animals', methods=['GET'])
def get_animals():
    #Returns a JSON string contained a dictionary of animals

    animal_dict = get_data()
    return jsonify(animal_dict)


@app.route('/animals/head/<head>', methods=['GET'])
def get_heads(head):

    animal_dict = get_data()
    head_dict = {}
    head_dict['animals'] = []

    #If an animal has the correct head, adds it to the dictionary
    for animal in animal_dict['animals']:
        if animal['head'] == head:
            head_dict['animals'].append(animal)
    
    return jsonify(head_dict)

@app.route('/animals/legs/<num_legs>', methods=['GET'])
def get_legs(num_legs):
    animal_dict = get_data()
    leg_dict = {}
    leg_dict['animals'] = []

    n = int(num_legs)

    #If animal has the correct number of legs, add it to the dictionary
    for animal in animal_dict['animals']:
        if animal['legs'] == n:
            leg_dict['animals'].append(animal)
    
    return jsonify(leg_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')