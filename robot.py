from weapon import Weapon
import random


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.active_weapon = Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25))

    # Add block - 50% damage, and dodge capability.
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power