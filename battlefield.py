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
        self.display_players_stats()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Robot vs Dinosaur\n\nWelcome to the battle of the ages! There can only be one! Which side will win?\n")

    # Add function to determine which player/group of players should go first.
    # def coin_toss(self):
    #     random.choice(['heads', 'tails'])

    def display_players_stats(self):
        print(f"Robot - NAME: {self.robot.name}, HP: {self.robot.health}, WEAPON: {self.robot.active_weapon.name}, ATT: "\
            f"{self.robot.active_weapon.attack_power}")
        print(f"Dinosaur - NAME: {self.dinosaur.name}, HP: {self.dinosaur.health}, ATT: {self.dinosaur.attack_power}\n")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            n = self.robot.attack(self.dinosaur)
            print(f"Robot {self.robot.name} attacks {self.dinosaur.name} with {self.robot.active_weapon.name} for",\
                self.display_robot_attack(n))
            print(f"Dinosaur {self.dinosaur.name} has {self.dinosaur.health if self.dinosaur.health > 0 else 0} health remaining!\n")
            if self.dinosaur.health <= 0:
                break
            n = self.dinosaur.attack(self.robot)
            print(f"Dinosaur {self.dinosaur.name} attacks {self.robot.name} for", self.display_dinosaur_attack(n))
            print(f"Robot {self.robot.name} has {self.robot.health if self.robot.health > 0 else 0} health remaining!\n")

    def display_robot_attack(self, n):
        statement = f"{self.robot.active_weapon.attack_power} damage!"
        if n == 1: 
            statement = f"triple damage ({3 * self.robot.active_weapon.attack_power} dmg)!"
        elif n in range(2, 10):
            statement = f"double damage ({2 * self.robot.active_weapon.attack_power} dmg)!"
        elif n == 100:
            statement = f"0 damage as {self.dinosaur.name} dodged the attacked and healed quite a bit!"
        elif n in range(96, 99):
            statement = f"0 damage as {self.dinosaur.name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            statement = f"0 damage as {self.dinosaur.name} dodged the attack!"
        elif n in range(53, 85):
            statement = f"half the damage ({math.ceil(0.5 * self.robot.active_weapon.attack_power)} dmg) as {self.dinosaur.name} blocked "\
                        f"the attack!"
        return statement

    def display_dinosaur_attack(self, n):
        statement = f"{self.dinosaur.attack_power} damage!"
        if n == 1:
            statement = f"triple damage ({3 * self.dinosaur.attack_power} dmg)!"
        elif n in range(2, 10):
            statement = f"double damage ({2 * self.dinosaur.attack_power} dmg)!"
        elif n == 100:
            statement = f"0 damage as {self.robot.name} dodged the attack and healed quite a bit!"
        elif n in range(96, 99):
            statement = f"0 damage as {self.robot.name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            statement = f"0 damage as {self.robot.name} dodged the attack!"     
        elif n in range(53, 85):
            statement = f"half the damage ({math.ceil(0.5 * self.dinosaur.attack_power)} dmg) as {self.robot.name} blocked "\
                        f"the attack!"           
        return statement

    def display_winner(self):
        if self.robot.health <= 0:
            print("Dinosaurs win!")
        elif self.dinosaur.health <= 0: 
            print("Robots win!")