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

    def getAtk(self):
        print(self.atkl)

enemy2 = Enemy()
enemy2.getAtk()