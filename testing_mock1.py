import unittest
import json
from flask import Flask
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_key(self):
        data = {
            "name": "demian-ssh-laptop",
            "public_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMxh4gVsvQWbD8ymVHmX9uLzv5Z43kwmy8hM2jxh/1nV your_email@example.com",
            "type": "ed25519"
        }
        response = self.app.post('/key', json=data)
        self.assertEqual(response.status_code, 200)

        key_json = json.loads(response.data.decode('utf-8'))
        print(key_json)
        # self.assertIn('id', key_json)

    def test_extract_key_id(self):
        data = {
            "name": "demian-ssh-laptop",
            "public_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMxh4gVsvQWbD8ymVHmX9uLzv5Z43kwmy8hM2jxh/1nV your_email@example.com",
            "type": "ed25519"
        }

        response = self.app.post('/key', json=data)

        key_json = json.loads(response.data.decode('utf-8'))

        response = self.app.get('/key')
        self.assertEqual(response.status_code, 200)

        extracted_key_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(key_json, extracted_key_json)

    def test_generate_instance(self):
        data = {
            'keys': [{'id': 'key_id'}],
            'vpc': {'id': 'vpc_id'},
            'volume': {'profile': {'name': 'vol_name'}},
            'image': {'id': 'img_id'},
            'primary_network_interface': {'subnet': {'id': 'subnet_id'}}
        }
        response = self.app.post('/instance', json=data)
        self.assertEqual(response.status_code, 200)

        instance_json = json.loads(response.data.decode('utf-8'))
        self.assertIn('id', instance_json)

    def test_extract_ins_id(self):
        data = {
            'keys': [{'id': 'key_id'}],
            'vpc': {'id': 'vpc_id'},
            'volume': {'profile': {'name': 'vol_name'}},
            'image': {'id': 'img_id'},
            'primary_network_interface': {'subnet': {'id': 'subnet_id'}}
        }
        response = self.app.post('/instance', json=data)

        instance_json = json.loads(response.data.decode('utf-8'))

        response = self.app.get('/instance')
        self.assertEqual(response.status_code, 200)

        extracted_instance_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(instance_json, extracted_instance_json)


if __name__ == '__main__':
    unittest.main()
