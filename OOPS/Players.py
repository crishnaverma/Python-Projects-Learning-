class Players:
    count = 0
    def __init__(self,player,level):
        self.player = player
        self.level = level
        Players.count +=1

    def update_player(self,player):
        self.player=player
    
    def update_level(self,level):
        self.level=level

    def get_det(self):
        return self.player,self.level
    
    @classmethod
    def get_count(cls):
        print (cls.count)


p1 = Players("Krishna", 5)
p2 = Players("Arjun", 2)

Players.get_count()
print(p1.get_det())
print(p2.get_det())