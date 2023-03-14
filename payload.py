
class payload_c:
    def __init__(self):
        self.vpc_id = None
        self.cidr = None
        self.vol_name = None
        self.subnet_id = None
        self.vpc_id = None
        self.img_id = None
        self.key_id = None


        self.data = {"grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                     "apikey": "OvrA5nAnnQQeSEtMo1Dk58dhxjLNcZnLKTxyaPZNvUnF"}

        self.pay_key = {
            "name": "demian-ssh-laptop",
            "public_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMxh4gVsvQWbD8ymVHmX9uLzv5Z43kwmy8hM2jxh/1nV your_email@example.com",
            "type": "ed25519"
        }

        self.pay_vpc = {
            "name": "my-vpc"
        }

        self.pay_sub = {
            "vpc": {"id": self.vpc_id},
            "zone": {"name": "us-south-1"},
            "ipv4_cidr_block": self.cidr
        }

        self.pay_ins = {
            "name": "demo",
            "boot_volume_attachment": {
                "delete_volume_on_instance_delete": True,
                "name": "boot-vol",
                "volume": {
                    "source_snapshot": "{{SNAPSHOT_ID}}",
                    "profile": {
                        "name": self.vol_name
                    }
                }
            },
            "keys": [
                {
                    "id": self.key_id
                }
            ],
            "primary_network_interface": {
                "subnet": {
                    "id": self.subnet_id
                }
            },
            "profile": {
                "name": "bx2-2x8"
            },
            "vpc": {
                "id": self.vpc_id
            },
            "zone": {
                "name": "us-south-1"
            },
            "image": {
                "id": self.img_id
            }
        }

    def print_sub_id(self):

        self.pay_sub = {
            "vpc": {"id": self.vpc_id},
            "zone": {"name": "us-south-1"},
            "ipv4_cidr_block": self.cidr
        }



    def print_ins_id(self):

        self.pay_ins = {
            "name": "demo",
            "boot_volume_attachment": {
                "delete_volume_on_instance_delete": True,
                "name": "boot-vol",
                "volume": {
                    "source_snapshot": "{{SNAPSHOT_ID}}",
                    "profile": {
                        "name": self.vol_name
                    }
                }
            },
            "keys": [
                {
                    "id": self.key_id
                }
            ],
            "primary_network_interface": {
                "subnet": {
                    "id": self.subnet_id
                }
            },
            "profile": {
                "name": "bx2-2x8"
            },
            "vpc": {
                "id": self.vpc_id
            },
            "zone": {
                "name": "us-south-1"
            },
            "image": {
                "id": self.img_id
            }
        }