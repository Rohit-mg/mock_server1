import pdb



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         self.fullname = {"fname": self.firstname, "lname": self.lastname}
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#     def printfullname(self):
#         print(self.fullname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.firstname = fname
#         self.lastname = lname
#         # self.fullname = {"fname": self.firstname, "lname": self.lastname}
#
#     def change(self):
#         self.firstname = "bohit"
#         self.fullname['fname'] = self.firstname
#         print(self.firstname)
#
#     def printfull(self):
#         print(self.fullname)
#
#
# pdb.set_trace()
# x = Student("Mike", "Olsen")

# x.change()
# x.printfull()

# def f1():
#     a = []
#     for i in range(5):
#         print(i)
#         x = i * i
#         a.append(x)
#     return a
#
# pdb.set_trace()
# x = f1()
# print(x)

a = {
  "boot_volume_attachment": {
    "delete_volume_on_instance_delete": True,
    "name": "volume-attachment",
    "volume": {
      "capacity": 100,
      "name": "my-instance-template-boot",
      "profile": {
        "name": "general-purpose"
      }
    }
  },
  "created_at": "2020-10-01T13:37:00Z",
  "crn": "crn:crn:v1:staging:public:is:us-south-1:a/f3bad5305cff47af940f9ac4350cdb68::volume:r134-f7e7c038-aab0-47f8-bf41-58931e682cac",
  "href": "https://us-south.iaas.cloud.ibm.com/v1/instance/templates/07a7-eca9fd45-e086-4400-a799-77b09ec5be84",
  "id": "07a7-eca9fd45-e086-4400-a799-77b09ec5be84",
  "image": {
    "id": "r018-6f153a5d-6a9a-496d-8063-5c39932f6ded"
  },
  "keys": [
    {
      "id": "r018-176f38a6-5d21-4cfb-ac20-f20d90d9e888"
    }
  ],
  "name": "my-instance-template",
  "primary_network_interface": {
    "security_groups": [
      {
        "id": "r018-f4793b96-4fc1-4a57-a18d-ff50d8001566"
      }
    ],
    "subnet": {
      "id": "07a7-3162c0fc-178f-46da-b4ca-d9448824056c"
    }
  },
  "profile": {
    "name": "bx2-2x8"
  },
  "resource_group": {
    "href": "https://resource-controller.cloud.ibm.com/v2/resource_groups/4bbce614c13444cd8fc5e7e878ef8e21",
    "id": "4bbce614c13444cd8fc5e7e878ef8e21",
    "name": "Default"
  },
  "vpc": {
    "id": "r018-d6979555-bf41-4755-ab78-f1f753a939e0"
  },
  "zone": {
    "name": "us-south-3"
  }
}