from _datetime import datetime

ENDPOINT = "us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com"
DATE = datetime.today().strftime('%Y-%m-%d')
identity_url = "https://iam.test.cloud.ibm.com/identity/token"
baseUrl = "http://us-south-genesis-dal10-compute1.iaasdev.cloud.ibm.com",
key_url = "http://127.0.0.1:5000/key"
vpc_url = f"https://{ENDPOINT}:443/v1/vpcs?generation=2&version={DATE}"
vpc_cidr_url = "https://{ENDPOINT}:443/v1/vpcs/{vpc_id}/address_prefixes?generation=2&version={DATE}"
subnet_url = f"https://{ENDPOINT}:443/v1/subnets?generation=2&version={DATE}"
img_url = f"https://{ENDPOINT}/v1/images?version={DATE}&generation=2"
vol_url = f"https://{ENDPOINT}/v1/volume/profiles?generation=2&version={DATE}"
ins_url = "http://127.0.0.1:5000/instance"
