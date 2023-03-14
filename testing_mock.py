import json
import time

import urls
from app import app
from unittest import TestCase
from test import new_id
from testmarker import mark
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')



def wait_status():
    print("Sleep started")
    count = 0
    while count <= 10:
        print(count)
        count += 1
        time.sleep(1)


@mark.a
class testapp(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_key(self):
        data = new_id.pay_key
        resp = self.app.post('/key', json=data)
        self.assertEqual(resp.status_code, 200)

        key_json = json.loads(resp.data)
        logging.debug("test for post /key")
        self.assertEqual(key_json['keys'][0]['name'], data["name"])
        logging.debug(f"expected: {key_json['keys'][0]['name']}      actual: {data['name']} ")
        self.assertEqual(key_json['keys'][0]['type'], data['type'])
        logging.debug(f"expected: {key_json['keys'][0]['type']}      actual: {data['type']} ")
        self.assertEqual(key_json['keys'][0]['public_key'], data["public_key"])
        logging.debug(f"expected: {key_json['keys'][0]['public_key']}      actual: {data['public_key']} ")
        logging.debug('\n')


@mark.b
class testapp1(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_extract_key_id(self):
        data = new_id.pay_key
        resp = self.app.post('/key', json=data)
        self.assertEqual(resp.status_code, 200)
        key_json = json.loads(resp.data)

        resp = self.app.get('/key')
        self.assertEqual(resp.status_code, 200)
        extracted_json = json.loads(resp.data)

        logging.debug("test for get /key")
        self.assertEqual(extracted_json, key_json)
        self.assertEqual(key_json['keys'][0]['type'], data['type'])
        logging.debug(f"expected: {key_json['keys'][0]['type']}      actual: {data['type']} ")
        self.assertEqual(key_json['keys'][0]['name'], data["name"])
        logging.debug(f"expected: {key_json['keys'][0]['name']}      actual: {data['name']} ")
        logging.debug('\n')


@mark.c
class testapp3(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_instance(self):
        data = new_id.pay_ins

        resp = self.app.post('/instance', json=data)
        self.assertEqual(resp.status_code, 200)
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


@mark.d
class testapp4(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_extract_ins_id(self):
        data = new_id.pay_ins
        resp = self.app.post('/instance', json=data)
        self.assertEqual(resp.status_code, 200)
        ins_json = json.loads(resp.data)

        resp = self.app.get('/instance')
        self.assertEqual(resp.status_code, 200)
        extracted_json = json.loads(resp.data)
        self.assertEqual(extracted_json['status'], "pending")
        logging.debug("test for get /instance")
        logging.debug(f"expected: {extracted_json['status']}      actual: 'pending' ")


        count = 0
        while(count<13):
            time.sleep(3)
            logging.debug(f"expected: {extracted_json['status']}      actual: 'running' ")
            count+=3



        resp = self.app.get('/instance')
        self.assertEqual(resp.status_code, 200)
        extracted_json = json.loads(resp.data)
        self.assertEqual(extracted_json['status'], "running")
        logging.debug(f"expected: {extracted_json['status']}      actual: 'running' ")
        logging.debug('\n')
