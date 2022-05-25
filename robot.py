from weapon import Weapon
import random
import math


class Robot:
    def __init__(self, name, weapon, attack_power):
        self.name = name
        self.health = random.randint(50, 100)
        self.active_weapon = Weapon(weapon, attack_power)

    def attack(self, dinosaur):
        n = random.randint(1, 100)
        if n == 1:
            dinosaur.health -= (3 * self.active_weapon.attack_power)
        elif n in range(2, 10):
            dinosaur.health -= (2 * self.active_weapon.attack_power)
        elif n == 100:
            dinosaur.health += random.randint(10, 25)
        elif n in range(96, 99):
            dinosaur.health += random.randint(1, 10)      
        elif n in range (86, 95):
            pass        
        elif n in range(53, 85):
            dinosaur.health -= math.ceil(0.5 * self.active_weapon.attack_power)
        elif n == 50:
            self.health -= self.active_weapon.attack_power
        else: 
            dinosaur.health -= self.active_weapon.attack_power
        return n