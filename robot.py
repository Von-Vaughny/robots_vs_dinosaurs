from weapon import Weapon
import random
import math


class Robot:
    def __init__(self, name, weapon, attack_power):
        self.name = name
        self.health = random.randint(50, 100)
        self.active_weapon = Weapon(weapon, attack_power)

    def attack(self, dinosaur):
        self.d20 = random.randint(1, 20)
        if self.d20 in range(19, 20):
            dinosaur.health -= (3 * self.active_weapon.attack_power)
        elif self.d20 in range(15, 18):
            dinosaur.health -= (2 * self.active_weapon.attack_power)
        elif self.d20 in range(7, 10):
            dinosaur.health -= math.ceil(0.5 * self.active_weapon.attack_power)
        elif self.d20 in range(5, 7):
            pass
        elif self.d20 in range(3, 5):
            dinosaur.health += random.randint(1, 10) 
        elif self.d20 == 2:
            dinosaur.health += random.randint(10, 25)        
        elif self.d20 == 1:
            self.health -= self.active_weapon.attack_power           
        else: 
            dinosaur.health -= self.active_weapon.attack_power
        return self.d20