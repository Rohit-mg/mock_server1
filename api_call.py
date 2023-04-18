import json
import requests
import payload
import urls
from urls import ENDPOINT, DATE
from payload import payload_c
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def access_token(payload):
    data = payload
    response = requests.post(urls.identity_url, data)
    access_token = eval(response.text)
    return access_token["access_token"]


def auth(payload):
    baseUrl = urls.baseUrl
    auth_token = access_token(payload)

    hed = {'Authorization': 'Bearer ' + auth_token}
    return baseUrl, hed


logging.debug("------")


def get_key_id(hed, payload):
    header = {"Content-Type": "application/json"}
    pay_key = payload
    data_json_key = json.dumps(pay_key)
    response_key = requests.post(urls.key_url, data_json_key,
                                 headers=header)

    logging.debug(response_key)
    data_key = response_key.json()
    keey_id = data_key["id"]
    logging.debug("keey_id- %s", keey_id)
    return keey_id


#####################################################################
def get_vpc_id(hed, payload):
    res_vpcs = requests.get(urls.vpc_url, headers=hed)
    data_vpc = res_vpcs.json()
    try:
        vpc_id = data_vpc["vpcs"][0]["id"]
    except:
        vpc_id = 0
    if vpc_id == 0:
        pay_vpc = payload
        print(pay_vpc)
        data_json_vpc = json.dumps(pay_vpc)
        response_sub = requests.post(urls.vpc_url, data_json_vpc,
                                     headers=hed)

        logging.debug(response_sub)
        res_vpcs = requests.get(
            urls.vpc_url,
            headers=hed)

        data_vpc = res_vpcs.json()

        vpc_id = data_vpc["vpcs"][0]["id"]
    logging.debug("------")
    logging.debug("vpc_id- %s", vpc_id)
    return vpc_id


def get_vpc_cidr(hed, vpc_id):
    res_vpcs = requests.get(
        urls.vpc_cidr_url.format(ENDPOINT=ENDPOINT, vpc_id=vpc_id, DATE=DATE),
        headers=hed)
    data_vpc_cidr = res_vpcs.json()
    cidr = data_vpc_cidr["address_prefixes"][0]["cidr"]
    logging.debug("cidr- %s", cidr)
    return cidr


#####################################################################
def get_subnet_id(hed, payload):
    res_subnet = requests.get(urls.subnet_url,
                              headers=hed)
    data_subnet = res_subnet.json()
    print("------")
    logging.debug("------")
    try:
        subnet_id = data_subnet["subnets"][0]["id"]
    except:
        subnet_id = 0
    if subnet_id == 0:

        pay_sub = payload

        data_json_sub = json.dumps(pay_sub)
        response_sub = requests.post(urls.subnet_url, data_json_sub,
                                     headers=hed)
        logging.debug(response_sub)
        res_subnet = requests.get(urls.subnet_url,
                                  headers=hed)

        data_subnet = res_subnet.json()
        subnet_id = data_subnet["subnets"][0]["id"]
    logging.debug("subnet_id- %s", subnet_id)
    return subnet_id


#####################################################################
def get_img_id(hed):
    res_img = requests.get(urls.img_url,
                           headers=hed)

    data_img = res_img.json()

    logging.debug("-----")
    img_id = "r134-6a8861e0-654a-4cfc-b09d-b25f5cee1d9c"
    logging.debug("img_id- %s", img_id)
    return img_id


#####################################################################
def get_vol_id(hed):
    res_vol = requests.get(urls.vol_url,
                           headers=hed)

    data_vol = res_vol.json()
    logging.debug("-----")
    vol_name = data_vol["profiles"][0]["name"]
    logging.debug("vol_name- %s", vol_name)
    return vol_name


#####################################################################
def get_ins_id(hed, payload):
    header = {"Content-Type": "application/json"}
    pay_ins = payload
    data_json_ins = json.dumps(pay_ins)
    response_ins = requests.post(urls.ins_url, data_json_ins,
                                 headers=header)

    logging.debug(response_ins)
    data_ins = response_ins.json()

    ins_id = data_ins["id"]

    logging.debug("instance_id- %s", ins_id)

    return ins_id

def instance_delete():
    del_instance = requests.delete(urls.ins_url_del)
