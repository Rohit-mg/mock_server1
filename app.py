from flask import Flask, jsonify, request
from mock_classes import KeyGenerator, post_instance
import time
from threading import Thread

app = Flask(__name__)

# this is a mock server for posting the required payload wherein there is a change in the public_key of the type
# edd25519
for_ker_id = {}
key_id1 = ""


@app.post('/key')
def generate_key():
    global key_id1
    data = request.get_json()
    name = data.get('name')
    public_key = data.get('public_key')
    type1 = data.get('type')
    key_generator = KeyGenerator(name, public_key, type1)
    key_id1 = key_generator.return_key_id()
    for_ker_id["key_gen"] = key_generator.generate_json()
    return for_ker_id["key_gen"]


# this is get function for the keys which returns the key_id value
@app.get('/key')
def extract_key_id():
    try:
        key_json = for_ker_id["key_gen"]
        return key_json
    except:
        return {"message": "first call the post /key before calling the get"}


# this is a mock server created for creating an instance with a different key_id(edd25519)

def wait_status():
    count = 0
    while count <= 10:
        count += 1
        time.sleep(1)


update_status_thread = None


@app.post('/instance')
def generate_instance():
    global for_ker_id
    global update_status_thread
    data = request.get_json()
    key_id = data.get('keys', [{}])[0].get('id')
    vpc_id = data.get('vpc', {}).get('id')
    vol_name = data.get('volume', {}).get('profile', {}).get('name')
    img_id = data.get('image', {}).get('id')
    subnet_id = data.get('primary_network_interface', {}).get('subnet', {}).get('id')

    key_instance = post_instance(key_id, vpc_id, vol_name, img_id, subnet_id)
    for_ker_id["ins_gen"] = key_instance.generate_json()
    update_status_thread = Thread(target=wait_status)
    update_status_thread.start()

    return jsonify(for_ker_id["ins_gen"])





@app.get('/instance')
def extract_ins_id():
    try:
        global for_ker_id

        ins_json = for_ker_id["ins_gen"]


        if update_status_thread and not update_status_thread.is_alive():
            ins_json["status"] = "running"

            return ins_json
        else:

            return ins_json


    except:
        return {"message": "call the post call /instance before get call"}


if __name__ == '__main__':
    app.run(debug=True)
