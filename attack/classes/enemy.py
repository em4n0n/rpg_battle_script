import random

# class Enemy:
#     def __init__(self, hp, mp):
#         self.max_hp = hp
#         self.hp = hp
#         self.max_mp = mp
#         self.mp = mp

class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self): # self creates instance
        print(self.atkl) 

enemy1 = Enemy() # instantiates the class to its own obj
enemy1.getAtk() # calls getAtk

enemy2 = Enemy()
enemy2.getAtk()