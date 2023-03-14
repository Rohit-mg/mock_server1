class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fullname = {"fname": self.firstname, "lname": self.lastname}

    def printname(self):
        print(self.firstname, self.lastname)

    def printfullname(self):
        print(self.fullname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.firstname = fname
        self.lastname = lname
        # self.fullname = {"fname": self.firstname, "lname": self.lastname}

    def change(self):
        self.firstname = "bohit"
        self.fullname['fname'] = self.firstname
        print(self.firstname)

    def printfull(self):
        print(self.fullname)



x = Student("Mike", "Olsen")
x.change()
x.printfull()
