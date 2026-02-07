class product:
    count =0
   
    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count +=1
    
    def get_info(self):
        print(f"Product name {self.name} price is {self.price}")


    @classmethod
    def get_count(cls):
        print(f"total product ={cls.count}")

    @staticmethod
    def get_dis_price(price,discount):
        print(f"Discounted Price = {price -(price*discount)/100}")


p1 = product("asus",2000)
p2 = product("hp",40_000)

p1.get_info()
product.get_count()
p2.get_dis_price(p2.price,12)
