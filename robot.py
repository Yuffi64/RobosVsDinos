#As a developer, I want a Robot to have a name, health, and a Weapon/
#(this needs to be its own class and object) with a name (i.e. sword) and attack power.

#As a developer, I want to instantiate three Robot objects/
#and three Dinosaur objects and assign the appropriate values to all the objects


import random

from weapons import Weapons

class Robot:
    def __init__(self, name, weapon_list):
        self.name = name
        self.weapon = None  
        self.health = 100
        self.power_level = 100
        self.weapon_options = weapon_list
      
    
    def attack(self, dino):
        print(f"{self.name} has attacked {dino.name} with {self.weapon.name}")
        
        if self.weapon.name == "Heat Blaze":
            print(f"{self.name} is using its Heat Blaze on {dino.name}! That's gotta hurt!")  
            dino.health -= dino.attack_power  
            dino.energy_level -= dino.attack_power 
        else:
            dino.health -= self.weapon.attack_power    
        self.power_level -= self.weapon.attack_power   
       
            
    def choose_weapon(self):
        pass