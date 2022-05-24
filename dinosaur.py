import random
import math

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randint(50, 100)

    # Add block - 50% damage, and dodge capability.
    def attack(self, robot):
        n = random.randint(1, 100)
        if n == 1:
            robot.health -= (3 * self.attack_power)
        elif n in range(1, 10):
            robot.health -= (2 * self.attack_power)
        elif n == 100:
            robot.health += random.randint(10, 25)
        elif n in range(96, 99):
            robot.health += random.randint(1, 10)  
        elif n in range (86, 95):
            pass
        elif n in range(53, 85):         
            robot.health -= math.ceil(0.5 * self.attack_power)
        elif n == 50:
            self.health -= self.attack_power
        else:
            robot.health -= self.attack_power
        return n