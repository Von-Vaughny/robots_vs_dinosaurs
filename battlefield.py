from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaur
import random
import math
import sys
import time

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.turn = random.choice([True, False])
        self.player_turn = 1    
       
    def run_game(self):
        self.display_welcome()
        self.select_units()
        self.display_players_stats()
        self.coin_toss()
        self.battle_phase()
        return self.display_winner()

    def display_welcome(self):
        print("Robots vs Dinosaurs\n\nRUFF MCGREE: Welcome to the battle of the ages, folks! I am your co-host RUFF MCGREE and this bumhead is "
            "your co-host DEADMAN, and we have gathered here for yet another night of mayhem in the arena.\n\nDEADMAN: That's right Ruff. And we have "
            "no shortage of robots and dinosaurs ready to fight for the title of Top Predator. The big question is, \"which side will win it?\" "
            "\n\nRUFF MCGREE: The big question indeed. But as we both know, only one team can win it, so let's waste no time and see who we have "
            "competing tonight!\n")

    def select_units(self):
        for i in range(len(['T-Rex', 'Pterodactyl', 'Helicoprion'])):
            self.herd.add_dinosaur(Dinosaur(['T-Rex', 'Pterodactyl', 'Helicoprion'][i], random.randint(10, 25)))
        for i in range(len(['Terminator', 'Destroyer', "Annihilator"])):
            self.fleet.add_robot(Robot(['Terminator', 'Destroyer', "Annihilator"][i], "Blast", 0))

    def display_players_stats(self):
        self.herd.display_dinosaurs_stats()
        self.select_robot_weapon()
        self.fleet.display_robots_stats()

    def select_robot_weapon(self):
        self.fleet.get_weapons()
        for i, robot in enumerate(self.fleet.fleet_list):
            self.weapon = self.fleet.equip_robot(i)
            robot.active_weapon.name = self.weapon.name
            robot.active_weapon.attack_power = self.weapon.attack_power

    def coin_toss(self):
        self.coin_toss_status = f"\n{'DEADMAN' if self.turn else 'RUFF MCGREE'}: And now the coin toss. Its. . . "
        self.end = f" {'HEADS! The Destructive Robots will start the battle!' if self.turn else 'TAILS! The Raging Dinosaurs will start the battle!'}\n"
        for i, letter in enumerate(self.coin_toss_status):
            if not i: 
                sys.stdout.write(self.coin_toss_status[0:-6])
            elif i in range(len(self.coin_toss_status)-6, len(self.coin_toss_status) -1):
                sys.stdout.write(letter)
                sys.stdout.flush()
                time.sleep(2)
            elif i == len(self.coin_toss_status)-1:
                sys.stdout.write(self.end)

    def battle_phase(self):
        while len(self.fleet.fleet_list) and len(self.herd.herd_list):
            self.current_round = math.ceil(self.player_turn/2)
            self.robots_turn() if self.turn else self.dinosaurs_turn()
            self.display_att_status()
            self.fleet.remove_robot()
            self.herd.remove_dinosaur()
            self.turn = not(self.turn)        
            self.player_turn += 1
            
    def robots_turn(self):
        self.robo = self.fleet.display_robot_selection_menu()
        self.dino = self.herd.display_dinosaur_selection_menu()
        self.d20 = self.robo.attack(self.dino)

    def dinosaurs_turn(self):
        self.dino = self.herd.select_dinosaur() 
        self.robo = self.fleet.select_robot()
        self.d20 = self.dino.attack(self.robo)

    def display_att_status(self):
        print(f"\nTurn {self.current_round}: {'Robots' if self.turn else 'Dinosaurs'}")       
        if self.turn: 
            print(f"{self.robo.display_att_result(self.d20, self.robo, self.dino)[0]} Robot {self.robo.name} attacks {self.dino.name} with " 
              f"{self.robo.active_weapon.name} for {self.robo.display_att_result(self.d20, self.robo, self.dino)[1]}\nDEADMAN: "
              f"Dinosaur {self.dino.name} has {self.dino.health if self.dino.health > 0 else 0} health remaining!")
        else:
            print(f"{self.dino.display_att_result(self.d20, self.dino, self.robo)[0]} Dinosaur {self.dino.name} attacks {self.robo.name} for "
                f"{self.dino.display_att_result(self.d20, self.dino, self.robo)[1]}\nRUFF MCGREE: Robot {self.robo.name} has "
                f"{self.robo.health if self.robo.health > 0 else 0} health remaining!")    

    def display_winner(self): 
        if len(self.fleet.fleet_list) == 0:
            print("\nTHE RAGING DINOSAURS WIN!")
            return "dinosaurs"
        elif len(self.herd.herd_list) == 0: 
            print("\nTHE DESTRUCTIVE ROBOTS WIN!")
            return "robots"