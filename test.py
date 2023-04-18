from payload import payload_c

from api_call import access_token, auth, get_key_id, get_vpc_id, get_vpc_cidr, get_subnet_id, get_vol_id, get_img_id, \
    get_ins_id


class create_ids(payload_c):

    def __init__(self):
        super().__init__()
        self.hed = None
        self.baseUrl = None
        self.access_token = None

    def create_access_token(self):
        self.access_token = access_token(self.data)

    def create_auth(self):
        self.baseUrl, self.hed = auth(self.data)

    def create_key_id(self):
        self.key_id = get_key_id(self.hed, self.pay_key)

    def create_vpc_id(self):
        self.vpc_id = get_vpc_id(self.hed, self.pay_vpc)

    def create_cidr(self):
        self.cidr = get_vpc_cidr(self.hed, self.vpc_id)

    def create_subnet_id(self):
        self.print_sub_id()
        self.subnet_id = get_subnet_id(self.hed, self.pay_sub)

    def create_vol_name(self):
        self.vol_name = get_vol_id(self.hed)

    def create_img_id(self):
        self.img_id = get_img_id(self.hed)

    def create_ins_id(self,name="demo"):
        self.print_ins_id(name)
        self.ins_id = get_ins_id(self.hed, self.pay_ins)


new_id = create_ids()
new_id.create_auth()
new_id.create_key_id()
new_id.create_vpc_id()
new_id.create_cidr()
new_id.create_subnet_id()
new_id.create_vol_name()
new_id.create_img_id()
new_id.create_ins_id()

