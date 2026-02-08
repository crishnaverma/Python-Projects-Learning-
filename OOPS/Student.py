class Student:
    def __init__(self,attributes_name, roll_no, marks):
        self.__attributes_name=attributes_name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_name (self,name):
        if name !="":
            self.__attributes_name=name
        else:
            print("Name cannot be empty")
    
    def name(self):
        return self.__attributes_name

    def roll(self,oll_no):
        if 1<= oll_no >=100:
            self.__roll_no=oll_no
        else:
            print("Number should be in between 1 to 100")
    
    def get_roll_no(self):
        return self.__roll_no
    
    def mar(self,mark):
        if mark>=0:
            self.__marks=mark
        else:
            print("Marks cannot be negative")

    def get_marks(self):
        return self.__marks
    
s = Student("Krishna", 10, 85)

print(s.name())
print(s.get_roll_no())
print(s.get_marks())

