class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)

        print("------------------")



p1 = Person("Krishna")
p1.display()


p2 = Person("Krishna", 19)
p2.display()


p3 = Person("Krishna", 19, "Assam")
p3.display()
