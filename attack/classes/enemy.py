import random

# class Enemy:
#     def __init__(self, hp, mp):
#         self.max_hp = hp
#         self.hp = hp
#         self.max_mp = mp
#         self.mp = mp

class Enemy:
    def __init__(self, atkl, atkh): # pass variables/objects in parenthesis
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self): # self creates instance
        print(self.atkl) 

enemy1 = Enemy(40, 49) # instantiates the enemy class to its own obj
enemy1.getAtk() # calls getAtk

enemy2 = Enemy(75, 90)
enemy2.getAtk()