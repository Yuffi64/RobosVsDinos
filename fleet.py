#As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur/
#objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).

from robot import Robot

import random

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):    
        self.robots(self.robot_one)
        self.robots(self.robot_two)
        self.robots(self.robot_three)
