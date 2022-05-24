from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
import random
import math


class Battlefield:
    def __init__(self):
        self.robot = Robot('Terminator')
        self.dinosaur = Dinosaur('T-Rex', random.randint(10, 25))

    def run_game(self):
        self.display_welcome()
        self.coin_toss()
        self.display_players_stats()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Robot vs Dinosaur\n\nWelcome to the battle of the ages! There can only be one! Which side will win?\n")

    def coin_toss(self):
        self.coin = random.choice(['heads', 'tails'])
        self.turn = 0
        if self.coin == 'tails':
            self.turn = 1

    def display_players_stats(self):
        print(f"Robot - Name: {self.robot.name}, HP: {self.robot.health}, Weapon: {self.robot.active_weapon.name}, ATT: "\
            f"{self.robot.active_weapon.attack_power}")
        print(f"Dinosaur - Name: {self.dinosaur.name}, HP: {self.dinosaur.health}, ATT: {self.dinosaur.attack_power}\n")
        print("Coin Toss Results Are In")
        if self.turn == 0:
            print("TAILS! The Robots take the coin toss and will be starting this battle!\n")
        elif self.turn == 1:
            print("HEADS! The Dinosaur take the coin toss and will be starting this battle!\n")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.turn == 0:
                n = self.robot.attack(self.dinosaur)
                print(f"{self.display_robot_attack(n)[0]} Robot {self.robot.name} attacks {self.dinosaur.name} with {self.robot.active_weapon.name}"\
                    f"for", self.display_robot_attack(n)[1])
                print(f"Dinosaur {self.dinosaur.name} has {self.dinosaur.health if self.dinosaur.health > 0 else 0} health remaining!\n")
                self.turn = 1
                if self.dinosaur.health <= 0:
                    break
            elif self.turn == 1:
                n = self.dinosaur.attack(self.robot)
                print(f"{self.display_dinosaur_attack(n)[0]} Dinosaur {self.dinosaur.name} attacks {self.robot.name} for",\
                     self.display_dinosaur_attack(n)[1])
                print(f"Robot {self.robot.name} has {self.robot.health if self.robot.health > 0 else 0} health remaining!\n")
                self.turn = 0

    def display_robot_attack(self, n):
        hit = "HIT!"
        statement = f"{self.robot.active_weapon.attack_power} damage!"
        if n == 1: 
            hit = "3x CRITCAL HIT!"
            statement = f"triple damage ({3 * self.robot.active_weapon.attack_power} dmg)!"
        elif n in range(2, 10):
            hit = "2x CRITICAL HIT!"
            statement = f"double damage ({2 * self.robot.active_weapon.attack_power} dmg)!"
        elif n == 100:
            hit = "MISS!"
            statement = f"0 damage as {self.dinosaur.name} dodged the attacked and healed quite a bit!"
        elif n in range(96, 99):
            hit = "MISS!"
            statement = f"0 damage as {self.dinosaur.name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            hit = "MISS!"
            statement = f"0 damage as {self.dinosaur.name} dodged the attack!"
        elif n in range(53, 85):
            hit = "WEAK HIT!"
            statement = f"half the damage ({math.ceil(0.5 * self.robot.active_weapon.attack_power)} dmg) as {self.dinosaur.name} blocked "\
                        f"the attack!"
        elif n == 50:
            hit = "HIT REFLECTED!"
            statement = f"{self.robot.active_weapon.attack_power} damage but it was deflected back at Robot {self.robot.name}!"
        return hit, statement

    def display_dinosaur_attack(self, n):
        hit = "HIT!"
        statement = f"{self.dinosaur.attack_power} damage!"
        if n == 1:
            hit = "3x CRITICAL HIT!"
            statement = f"triple damage ({3 * self.dinosaur.attack_power} dmg)!"
        elif n in range(2, 10):
            hit = "2x CRITICAL HIT!"
            statement = f"double damage ({2 * self.dinosaur.attack_power} dmg)!"
        elif n == 100:
            hit = "MISS!"
            statement = f"0 damage as {self.robot.name} dodged the attack and healed quite a bit!"
        elif n in range(96, 99):
            hit = "MISS!"
            statement = f"0 damage as {self.robot.name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            hit = "MISS!"
            statement = f"0 damage as {self.robot.name} dodged the attack!"     
        elif n in range(53, 85):
            hit = "WEAK HIT!"
            statement = f"half the damage ({math.ceil(0.5 * self.dinosaur.attack_power)} dmg) as {self.robot.name} blocked "\
                        f"the attack!"    
        elif n == 50:
            hit = "HIT REFLECTED!"    
            statement = f"{self.dinosaur.attack_power} damage but it was deflected back at Dinosaur {self.dinosaur.name}!"   
        return hit, statement

    def display_winner(self):
        if self.robot.health <= 0:
            print("Dinosaurs win!")
        elif self.dinosaur.health <= 0: 
            print("Robots win!")