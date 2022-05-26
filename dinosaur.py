import random
import math

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randint(50, 100)

    def attack(self, robot):
        d20 = random.randint(1, 20)
        if d20 in range(19, 20):       
            robot.health -= (3 * self.attack_power)
        elif d20 in range(15, 18):
            robot.health -= (2 * self.attack_power)
        elif d20 in range(7, 10):        
            robot.health -= math.ceil(0.5 * self.attack_power)        
        elif d20 in range(5, 7):
            pass
        elif d20 in range(3, 5):
            robot.health += random.randint(1, 10)
        elif d20 == 2:
            robot.health += random.randint(10, 25)  
        elif d20 == 1:
            self.health -= self.attack_power
        else:
            robot.health -= self.attack_power
        return d20