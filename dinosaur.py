import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randint(50, 100)

    # Add block - 50% damage, and dodge capability.
    def attack(self, robot):
        robot.health -= self.attack_power