import json
import time

import payload
import urls
from app import app
from unittest import TestCase
from test import new_id
from testmarker import mark
import logging
from api_call import instance_delete
import pdb

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


@mark.a
class testapp(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pdb.set_trace()
        instance_delete()


    def test_generate_key(self):
        data = new_id.pay_key
        print(data)
        resp = self.app.post(urls.key_url, json=data)
        print(resp)
        self.assertEqual(resp.status_code, 201)

        key_json = json.loads(resp.data)
        logging.debug('\n')
        logging.debug("test for post /key")
        self.assertEqual(key_json['name'], data["name"])
        logging.debug(f"expected: {key_json['name']}      actual: {data['name']} ")
        self.assertEqual(key_json['type'], data['type'])
        logging.debug(f"expected: {key_json['type']}      actual: {data['type']} ")
        self.assertEqual(key_json['public_key'], data["public_key"])
        logging.debug(f"expected: {key_json['public_key']}      actual: {data['public_key']} ")
        logging.debug('\n')



    def test_extract_key_id(self):
        data = new_id.pay_key
        resp = self.app.post(urls.key_url, json=data)
        self.assertEqual(resp.status_code, 201)
        key_json = json.loads(resp.data)

        resp = self.app.get(urls.key_url)
        self.assertEqual(resp.status_code, 201)
        extracted_json = json.loads(resp.data)

        logging.debug("test for get /key")
        self.assertEqual(extracted_json, key_json)
        self.assertEqual(key_json['type'], data['type'])
        logging.debug(f"expected: {key_json['type']}      actual: {data['type']} ")
        self.assertEqual(key_json['name'], data["name"])
        logging.debug(f"expected: {key_json['name']}      actual: {data['name']} ")
        logging.debug('\n')




    def test_generate_instance(self):
        new_id.print_ins_id(name="demo2")
        data = new_id.pay_ins
        resp = self.app.post(urls.ins_url, json=data)
        self.assertEqual(resp.status_code, 201)
        ins_json = json.loads(resp.data)

        logging.debug("test for post /instance")
        self.assertEqual(ins_json['primary_network_interface']['subnet']['id'],
                         data['primary_network_interface']['subnet']['id'])
        logging.debug(
            f"expected: {ins_json['primary_network_interface']['subnet']['id']}      actual: {data['primary_network_interface']['subnet']['id']} ")
        self.assertEqual(ins_json['profile']['name'], data['profile']['name'])
        logging.debug(f"expected: {ins_json['profile']['name']}      actual: {data['profile']['name']} ")
        self.assertEqual(ins_json['image']['id'], data['image']['id'])
        logging.debug(f"expected: {ins_json['image']['id']}      actual: {data['image']['id']} ")
        logging.debug('\n')




    def test_extract_ins_id(self):
        name = "demo3"
        new_id.print_ins_id(name=name)
        data = new_id.pay_ins
        resp = self.app.post(urls.ins_url, json=data)
        self.assertEqual(resp.status_code, 201)
        ins_json = json.loads(resp.data)
        id = ins_json["id"]
        change_url = urls.ins_url + '/' + id
        resp = self.app.get(change_url)
        self.assertEqual(resp.status_code, 200)
        extracted_json = json.loads(resp.data)
        self.assertEqual(extracted_json['status'], "pending")
        logging.debug("test for get /instance")
        logging.debug(f"expected: {extracted_json['status']}      actual: 'pending' ")

        count = 0
        while count < 30:
            resp = self.app.get(change_url)
            extracted_json = json.loads(resp.data)
            # extracted_json = resp.json()
            if extracted_json['status'] == "running":
                break
            else:
                time.sleep(3)
                count += 3
                logging.debug(f"instance status :{extracted_json['status']}")

        resp = self.app.get(change_url)
        self.assertEqual(resp.status_code, 200)
        extracted_json = json.loads(resp.data)
        self.assertEqual(extracted_json['status'], "running")
        logging.debug(f"expected: {extracted_json['status']}      actual: 'running' ")
        logging.debug('\n')
