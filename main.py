from flask import Flask, jsonify, request
from datetime import datetime
# from test import vpc_id,vol_name,img_id,subnet_id
import test
from test import create_ids

import ed25519
import os

app = Flask(__name__)


class KeyGenerator:
    def __init__(self, name, public_key, type):
        self.name = name
        self.public_key = public_key
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.type = type
        self.key_id = test.keey_id

    # returns the required json value for keys
    def generate_json(self):
        data = {
            "first": {
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/keys?limit=50"
            },
            "keys": [
                {
                    "created_at": self.created_at,
                    "id": self.key_id,

                    "name": self.name,
                    "public_key": self.public_key,

                    "type": self.type
                }
            ],
            "limit": 50,
            "total_count": 1
        }

        data1 = {"name": self.name}
        return jsonify(data)

    def return_key_id(self):
        return self.key_id


class post_instance:
    def __init__(self, key_id, vpc_id, vol_name, img_id, subnet_id):
        self.key_id = key_id
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.vpc_id = vpc_id
        self.vol_name = vol_name
        self.img_id = img_id
        self.subnet_id = subnet_id

    # returns the required json value for instance
    def generate_json(self):
        data = {

            "id": self.img_id,
            "name": "demo",
            "subnet": {
                "id": self.subnet_id,
                "name": "patio-custody-lilac-breeches",
                "resource_type": "subnet"
            },
            "vpc": {

                "id": self.vpc_id,

            },
            "zone": {
                "name": "us-south-1"
            }

        }
        return jsonify(data)


for_ker_id = {}
key_id1 = ""


# this is a mock server for posting the required payload wherein there is a change in the public_key of the type
# edd25519
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
    key_json = for_ker_id["key_gen"]
    print(key_id1)
    return key_json


# this is a mock server created for creating an instance with a different key_id(edd25519)
@app.post('/instance')
def generate_instance():
    # data = request.get_json()
    # key_id = data.get("keys")
    # keyid = data.get("id")
    # keyid = key_id[0]["id"]
    keyid = key_id1
    key_instance = post_instance(keyid, test.vpc_id, test.vol_name, test.img_id, test.subnet_id)
    return key_instance.generate_json()


if __name__ == '__main__':
    app.run(debug=True)
