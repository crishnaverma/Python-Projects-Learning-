class Vehicle:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
   
class Bike(Vehicle):
    def __init__(self,engine_cc,brand,model):
        self.engine_cc = engine_cc
        super().__init__(brand,model)
        
class Car(Vehicle):
    def __init__(self,seat,brand,model):
        self.seat = seat
        super().__init__(brand,model)


b1 = Bike(313,"bmw","s100rr")
c1 = Car(2,"audi","r8")

print(b1.model,b1.brand,b1.engine_cc, sep ="\n")
print(c1.model,c1.brand,c1.seat,sep="\n")
    
        