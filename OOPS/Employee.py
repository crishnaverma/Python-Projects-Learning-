from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def cal_salary(self):
        pass

class inter(Employee):
    def __init__ (self, salary):
        self.salary = salary
    def cal_salary(self):
        return self.salary


class Fulltime_employe(Employee):
    def __init__ (self, salary):
        self.salary = salary
    def cal_salary(self):
        return self.salary


class Contract_emply(Employee):
    def __init__ (self, salary):
        self.salary = salary
    def cal_salary(self):
        return self.salary
    


i = inter(10000)
f = Fulltime_employe(50000)
c = Contract_emply(30000)

print(i.cal_salary())
print(f.cal_salary())
print(c.cal_salary())