from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd
    
    def run_game(self):
        self.display_welcome()

        pass


    def display_welcome(self):
        pass

    #As a developer, I want a Robot to have the ability to /
    #attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield.
    
    
    def battle(self):
        pass


#As a developer, I want a Robot/Dinosaur to lose health points /
#(loss based on attack power) when another Robot/Dinosaur successfully attacks it.
    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass


    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def show_winners(self):
        pass 
