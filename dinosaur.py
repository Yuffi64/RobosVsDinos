#As a developer, I want a Dinosaur to have a name, health, and attack power

#As a developer, I want to instantiate three Robot objects/
#and three Dinosaur objects and assign the appropriate values to all the objects



class Dinosaur:

    def __init__(self, name, attack_power, attacks):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.energy_level = 100
        self.attack_options = attacks 
    
    def attack(self, robot):
        self.choose_attack()    
        if self.energy_level < self.attack_power:   
          pass
