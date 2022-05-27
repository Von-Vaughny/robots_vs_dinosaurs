import random
import math

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = random.randint(50, 100)

    def attack(self, robot):
        self.d20 = random.randint(1, 20)
        if self.d20 in range(19, 20):       
            robot.health -= (3 * self.attack_power)
        elif self.d20 in range(15, 18):
            robot.health -= (2 * self.attack_power)
        elif self.d20 in range(7, 10):        
            robot.health -= math.ceil(0.5 * self.attack_power)        
        elif self.d20 in range(5, 7):
            pass
        elif self.d20 in range(3, 5):
            robot.health += random.randint(1, 10)
        elif self.d20 == 2:
            robot.health += random.randint(10, 25)  
        elif self.d20 == 1:
            self.health -= self.attack_power
        else:
            robot.health -= self.attack_power
        return self.d20

    def display_att_result(self, d20, dinosaur, robot):
        self.hit = "DEADMAN: HIT!"
        self.status = f"{dinosaur.attack_power} damage!"
        if int(d20) in range(19, 20):
            self.hit = "DEADMAN: 3x CRITICAL HIT!"
            self.status = f"triple damage ({3 * dinosaur.attack_power} dmg)!"
        elif int(d20) in range(15, 18):
            self.hit = "DEADMAN: 2x CRITICAL HIT!"
            self.status = f"double damage ({2 * dinosaur.attack_power} dmg)!"
        elif int(d20) in range(7, 10):
            self.hit = "DEADMAN: WEAK HIT!"
            self.status = f"half the damage ({math.ceil(0.5 * dinosaur.attack_power)} dmg) as "\
                f"{robot.name} blocked the attack!"   
        elif int(d20) in range(5, 7):
            self.hit = "DEADMAN: MISS!"
            self.status = f"0 damage as {robot.name} dodged the attack!"
        elif int(d20) in range(3, 5):
            self.hit = "DEADMAN: MISS!"
            self.status = f"0 damage as {robot.name} dodged the attack and healed a little bit!"    
        elif int(d20) == 2:
            self.hit = "DEADMAN: MISS!"
            self.status = f"0 damage as {robot.name} dodged the attack and healed quite a bit!"  
        elif int(d20) == 1:
            self.hit = "DEADMAN: HIT REFLECTED!"    
            self.status = f"{dinosaur.attack_power} damage but it was deflected back at dinosaur {dinosaur.name}!\nRUFF MCGREE: Dinosaur "\
                f"{dinosaur.name} has {dinosaur.health if dinosaur.health > 0 else 0} remaining!"   
        return self.hit, self.status