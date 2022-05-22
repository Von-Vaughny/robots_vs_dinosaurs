from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
import random


class Battlefield:
    def __init__(self):
        self.robot = Robot('Terminator')
        self.dinosaur = Dinosaur('T-Rex', random.randint(10, 25))

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Robot vs Dinosaur\n\nWelcome to the battle of the ages! There can only be one! Which side will win?")

    # def coin_toss(self):
    #     random.choice(['heads', 'tails'])

    # Add if statement to exit immediately when hp < 0 and to show hp as 0 remaining.
    def battle_phase(self):
        while self.robot.health > 0 or self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            print(f"\nRobot {self.robot.name} attacks {self.dinosaur.name} with {self.robot.active_weapon.name} for "\
                  f"{self.robot.active_weapon.attack_power} damage!")
            print(f"Dinosaur {self.dinosaur.name} has {self.dinosaur.health} health remaining!\n")
            self.dinosaur.attack(self.robot)
            print(f"\nDinosaur {self.dinosaur.name} attacks {self.robot.name} for {self.dinosaur.attack_power} damage!")
            print(f"Robot {self.robot.name} has {self.robot.health} health remaining!\n")


    def display_winner(self):
        pass