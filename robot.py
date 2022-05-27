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
 
    def display_att_result(self, d20, robot, dinosaur):
        self.hit = "RUFF MCGREE: HIT!"
        self.status = f"{robot.active_weapon.attack_power} damage!"
        if int(d20) in range(19, 20):
            self.hit = "RUFF MCGREE: 3x CRITCAL HIT!"
            self.status = f"triple damage ({3 * robot.active_weapon.attack_power} dmg)!"
        elif int(d20) in range(15, 18):
            self.hit = "RUFF MCGREE: 2x CRITICAL HIT!"
            self.status = f"double damage ({2 * robot.active_weapon.attack_power} dmg)!"
        elif int(d20) in range(7, 10):
            self.hit = "RUFF MCGREE: WEAK HIT!"
            self.status= f"half the damage ({math.ceil(0.5 * robot.active_weapon.attack_power)} dmg) as "\
                f"{dinosaur.name} blocked the attack!"
        elif int(d20) in range(5, 7):
            self.hit = "RUFF MCGREE: MISS!"
            self.status = f"0 damage as {dinosaur.name} dodged the attack!"
        elif int(d20) in range(3, 5):
            self.hit = "RUFF MCGREE: MISS!"
            self.status = f"0 damage as {dinosaur.name} dodged the attack and healed a little bit!"
        elif int(d20) == 2:
            self.hit = "RUFF MCGREE: MISS!"
            self.status = f"0 damage as {dinosaur.name} dodged the attacked and healed quite a bit!"
        elif int(d20) == 1:
            self.hit = "RUFF MCGREE: HIT REFLECTED!"
            self.status = f"{robot.active_weapon.attack_power} damage but it was deflected back at Robot {robot.name}!\nDEADMAN: Robot {robot.name} "\
                f"has {robot.health if robot.health > 0 else 0} health remaining!"
        return self.hit, self.status