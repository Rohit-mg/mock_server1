import datetime
from flask import Flask, jsonify, request
from datetime import datetime


import uuid




class KeyGenerator:
    def __init__(self, name, public_key, type):
        self.name = name
        self.public_key = public_key
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.type = type
        self.key_id = "a6b1a881-2ce8-41a3-80fc-36316a73f803"

    def generate_json(self):
        data = {

            "created_at": self.created_at,
            "crn": "crn:v1:staging:public:is:us-south:a/f3bad5305cff47af940f9ac4350cdb68::key:r134"
                   "-d0111ee0-771e-4e7d-9d80-a6edb8b4507b",
            "fingerprint": "SHA256:US3aORWGNeNyuJ4SaxFkELTGzgMBiAbtWzF7zAsMMlg",
            "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/keys/r134-d0111ee0"
                    "-771e-4e7d-9d80-a6edb8b4507b",
            "id": self.key_id,
            "length": 2048,
            "name": self.name,
            "public_key": self.public_key,
            "resource_group": {
                "href": "https://resource-controller.test.cloud.ibm.com/v2/resource_groups"
                        "/7820413784bc4594aafd9bd33d45b9dd",
                "id": "7820413784bc4594aafd9bd33d45b9dd",
                "name": "Default"
            },
            "type": self.type
        }

        data1 = {"name": self.name}
        return jsonify(data)

    def return_key_id(self):
        return self.key_id


class post_instance:
    def __init__(self, key_id, vpc_id, vol_name, img_id, subnet_id, name,profile):
        self.key_id = key_id
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.vpc_id = vpc_id
        self.vol_name = vol_name
        self.img_id = img_id
        self.subnet_id = subnet_id
        self.name = name
        self.profile = profile

    def random_id_generator(self):
        random_id = f"7187_{str(uuid.uuid4())}"
        return random_id


    def generate_json(self):
        data = {
            "availability_policy": {
                "host_failure": "restart"
            },
            "bandwidth": 4000,
            "boot_volume_attachment": {
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instances/7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd/volume_attachments/7187-d7338f1d-8a70-4894-b43a-463a77325216",
                "id": "7187-d7338f1d-8a70-4894-b43a-463a77325216",
                "name": "boot-vol"
            },
            "created_at": "2023-03-01T13:05:07Z",
            "crn": "crn:v1:staging:public:is:us-south-1:a/f3bad5305cff47af940f9ac4350cdb68::instance:7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd",
            "disks": [],
            "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instances/7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd",
            "id": self.random_id_generator(),
            "image": {
                "crn": "crn:v1:staging:public:is:us-south:a/c21088ea7a014ffb8f6a7bc4304699a0::image:r134-6a8861e0-654a-4cfc-b09d-b25f5cee1d9c",
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/images/r134-6a8861e0-654a-4cfc-b09d-b25f5cee1d9c",
                "id": self.img_id,
                "name": "ibm-ubuntu-18-04-6-minimal-amd64-6"
            },
            "lifecycle_reasons": [],
            "lifecycle_state": "pending",
            "memory": 8,
            "metadata_service": {
                "enabled": False
            },
            "name": self.name,
            "network_interfaces": [
                {
                    "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instances/7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd/network_interfaces/7187-14c62481-8a11-49c5-b990-0cf54a52998f",
                    "id": "7187-14c62481-8a11-49c5-b990-0cf54a52998f",
                    "name": "koru-marathon-esquire-exuberant",
                    "primary_ip": {
                        "address": "0.0.0.0",
                        "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/subnets/7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8/reserved_ips/7187-1130a99b-cd71-4ef8-9b11-f15e7df584e2",
                        "id": "7187-1130a99b-cd71-4ef8-9b11-f15e7df584e2",
                        "name": "trial-hatchet-stoplight-nickname",
                        "resource_type": "subnet_reserved_ip"
                    },
                    "resource_type": "network_interface",
                    "subnet": {
                        "crn": "crn:v1:staging:public:is:us-south-1:a/f3bad5305cff47af940f9ac4350cdb68::subnet:7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8",
                        "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/subnets/7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8",
                        "id": self.subnet_id,
                        "name": "patio-custody-lilac-breeches",
                        "resource_type": "subnet"
                    }
                }
            ],
            "primary_network_interface": {
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instances/7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd/network_interfaces/7187-14c62481-8a11-49c5-b990-0cf54a52998f",
                "id": "7187-14c62481-8a11-49c5-b990-0cf54a52998f",
                "name": "koru-marathon-esquire-exuberant",
                "primary_ip": {
                    "address": "0.0.0.0",
                    "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/subnets/7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8/reserved_ips/7187-1130a99b-cd71-4ef8-9b11-f15e7df584e2",
                    "id": "7187-1130a99b-cd71-4ef8-9b11-f15e7df584e2",
                    "name": "trial-hatchet-stoplight-nickname",
                    "resource_type": "subnet_reserved_ip"
                },
                "resource_type": "network_interface",
                "subnet": {
                    "crn": "crn:v1:staging:public:is:us-south-1:a/f3bad5305cff47af940f9ac4350cdb68::subnet:7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8",
                    "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/subnets/7187-79e12b3a-f93a-46f1-8f52-6425dd1e67f8",
                    "id": self.subnet_id,
                    "name": "patio-custody-lilac-breeches",
                    "resource_type": "subnet"
                }
            },
            "profile": {
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instance/profiles/bx2-2x8",
                "name": self.profile
            },
            "resource_group": {
                "href": "https://resource-controller.test.cloud.ibm.com/v2/resource_groups/7820413784bc4594aafd9bd33d45b9dd",
                "id": "7820413784bc4594aafd9bd33d45b9dd",
                "name": "Default"
            },
            "resource_type": "instance",
            "startable": True,
            "status": "pending",
            "status_reasons": [],
            "total_network_bandwidth": 3000,
            "total_volume_bandwidth": 1000,
            "vcpu": {
                "architecture": "amd64",
                "count": 2,
                "manufacturer": "intel"
            },
            "volume_attachments": [
                {
                    "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/instances/7187_3b92c0b9-e8ec-404d-8350-86c90837f0bd/volume_attachments/7187-d7338f1d-8a70-4894-b43a-463a77325216",
                    "id": "7187-d7338f1d-8a70-4894-b43a-463a77325216",
                    "name": "boot-vol"
                }
            ],
            "vpc": {
                "crn": "crn:v1:staging:public:is:us-south:a/f3bad5305cff47af940f9ac4350cdb68::vpc:r134-39cd0231-5f46-4b1a-8163-7b70529930fe",
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/vpcs/r134-39cd0231-5f46-4b1a-8163-7b70529930fe",
                "id": self.vpc_id,
                "name": "my-vpc",
                "resource_type": "vpc"
            },
            "zone": {
                "href": "https://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com/v1/regions/us-south/zones/us-south-1",
                "name": "us-south-1"
            }
        }

        return data
