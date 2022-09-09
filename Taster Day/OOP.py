from tkinter import *
import random
import time

class character():
    def __init__(self,name,inventory):
        self._name=name
        self._inventory=inventory
        self._health=random.randint(0,100)
        self._strength=random.randint(0,100)

    def getname(self):
        return self._name

    def getcharacter(self):
        print("Name: ",self._name,"\nInventory: ",self._inventory,"\nHealth: ",self._health,"\nStrength: ",self._strength)

    def addinventory(self,items,weight,damage):
        if item=="Gold":
            self._inventory[item]+=value
        else:
            self._inventory[item]=weitgh,damage

    def damage(self):
        self._damage=random.randint(1-100)

hero=character("Bob",{"Gold":20})
##print(hero.getcharacter())

monsters = []
monsters.append(character("Goblin",{"Gold":20,"Dagger":1}))
monsters.append(character("Dragon",{"Gold":20,"Magic Amulet":100}))
##print(monsters[0].getcharacter())
##print(monsters[1].getcharacter())

def FoundChest():
    answer = input("You have stumbled apon a chest. Would you like to open it?\nPlease select Y|N")
    if answer == "Y" or answer == "y":
        
        tempval = random.randint(1,100)
        print("Opening")
        
    elif answer == "N" or answer == "n":
        return false

def FoundEnemy():
    answer = input("You have stumbled apon a enemy. Would you like to attack it?\nPlease select Y|N")                  
    if answer == "Y" or answer == "y":
        
        tempval = random.randint(1,100)
        print("Attacking")
        
    elif answer == "N" or answer == "n":
        return false



##MakeRandomTimeLoop
FoundChest()
