from flask import Flask, jsonify, request
from mock_classes import KeyGenerator, post_instance
import time
from threading import Thread
import json
import pdb
import atexit
import os

app = Flask(__name__)

file_path = '/Users/rohitmg/PycharmProjects/mock_server/data.json'


def delete_file():
    if os.path.exists(file_path):
        os.remove(file_path)


atexit.register(delete_file)

for_ker_id = {}
key_id1 = ""


@app.route('/')
def index():
    return 'Hello to Flask!'


@app.post('/v1/keys')
def generate_key():
    global key_id1
    data = request.get_json()
    if data['type'] not in data['public_key']:
        return jsonify(message="Key-type and public-key are not matched"), 400
    name = data.get('name')
    public_key = data.get('public_key')
    type1 = data.get('type')
    key_generator = KeyGenerator(name, public_key, type1)
    key_id1 = key_generator.return_key_id()
    for_ker_id["key_gen"] = key_generator.generate_json()
    return for_ker_id["key_gen"], 201


@app.get('/v1/keys')
def extract_key_id():
    try:
        key_json = for_ker_id["key_gen"]
        return key_json
    except:
        return {"message": "first call the post /key before calling the get"}



def wait_status():
    count = 0
    while count <= 20:
        count += 1
        time.sleep(1)


update_status_thread = None


@app.post('/v1/instances')
def generate_instance():
    global for_ker_id
    global update_status_thread
    data = request.get_json()
    key_id = data.get('keys', [{}])[0].get('id')
    vpc_id = data.get('vpc', {}).get('id')
    vol_name = data.get('volume', {}).get('profile', {}).get('name')
    img_id = data.get('image', {}).get('id')
    subnet_id = data.get('primary_network_interface', {}).get('subnet', {}).get('id')
    name = data.get('name')
    profile = data.get('profile',{}).get('name')

    key_instance = post_instance(key_id, vpc_id, vol_name, img_id, subnet_id, name,profile)
    for_ker_id["ins_gen"] = key_instance.generate_json()
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
            print(existing_data)
            for instance in existing_data:
                if for_ker_id["ins_gen"]["name"] == instance["name"]:
                    return jsonify({'message': 'Instance already exists.'}), 400
    except:
        existing_data = []
    print(for_ker_id["ins_gen"]["name"])

    existing_data.append(for_ker_id["ins_gen"])
    with open('data.json', 'w') as f:
        json.dump(existing_data, f)

    update_status_thread = Thread(target=wait_status)
    update_status_thread.start()
    print('--------')
    return jsonify(for_ker_id["ins_gen"]), 201

@app.get('/v1/instances')
def get_all_instances():
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
    except:
        existing_data = []


    return jsonify(existing_data), 200


@app.get('/v1/instances/<id>')
def get_instance(id):
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    for instance in existing_data:
        if instance['id'] == id:
            if update_status_thread and not update_status_thread.is_alive():
                instance["status"] = "running"
            return jsonify(instance), 200

    return jsonify({'message': 'Instance not found.'}), 404


@app.delete('/v1/instances/<id>')
def delete_instance(id):
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
    except:
        existing_data = []

    for i, instance in enumerate(existing_data):
        if instance['id'] == id:
            del existing_data[i]
            with open('data.json', 'w') as f:
                json.dump(existing_data, f)
            return jsonify({'message': 'Instance deleted.'}), 200

    return jsonify({'message': 'Instance not found.'}), 404

@app.delete('/v1/del_instances')
def delete_all_instances():
    try:
        with open('data.json', 'r') as f:
            existing_data = json.load(f)
    except:
        return jsonify({'message': 'No Instances found.'}), 404

    delete_file()
    return jsonify({'message': 'All instances deleted '}), 200





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
