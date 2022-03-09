#As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur/
#objects to be stored in a Herd (the Fleet and Herd must use a List to store the objects).

from dinosaur import Dinosaur

import random

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):  
        self.dinosaurs(self.dino_one)
        self.dinosaurs(self.dino_two)
        self.dinosaurs(self.dino_three)

