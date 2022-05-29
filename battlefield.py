from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaur
import random
import math
import time
import sys
import re


# CONSIDER adding different damage values to dinosaur's 'slashes', 'bites', 'rams'. Could update herd.select_dinosaur to find the highest value for 
# each attack for each dinosaur, and then randomly choose amongst them and use highest attack or a randomly selected attack from that dinosaur. May
# add game modes with environmental damage, random assistance from the hosts, combined attack damage from fellow robot/dinosaur, and even a one hit
# Death Match in which being first is a strong advantage. Could unlock these gameplay modes by the count of wins for the robots on main.py like
# winner = Battlefield().run_game(int(win[0])), and in battlefield.py def run_game(self, unlock), self.select_game_mode(unlock), def 
# select_game_mode(self, unlock) and having multiple if statements to show each different unlocked game_mode. Because I use 
# re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode "), it may be easier to have two lists, one list games with the initial two, second list
# game_modes = [], [games_modes.append(mode) for mode in games if mode not in games_modes] to avoid duplication in the case the next result is a 
# lost for the robots and the if statement reapplied.
class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.player_turn = 1    
        self.user_selected_mode = ""        
        self.turn = random.choice([True, False])

    def run_game(self):
        self.display_welcome()
        self.select_game_mode()
        self.select_units()
        self.display_players_stats()
        self.coin_toss()
        self.battle_phase()
        return self.display_winner()

    def display_welcome(self):
        print("Robots vs Dinosaurs\n\nRUFF MCGREE: Welcome to the battle of the ages, folks! I am your co-host RUFF MCGREE and this bumhead is "
            "your co-host DEADMAN, and we have gathered here for yet another night of mayhem in the arena.\n\nDEADMAN: That's right Ruff. And we have "
            "no shortage of robots and dinosaurs ready to fight for the title of Top Predator. The big question is, \"which side will winit?\" "
            "\n\nRUFF MCGREE: The big question indeed. But as we both know, only one team can win it, so let's waste no time and see who we have "
            "competing tonight!")

    def select_game_mode(self):
        while not(self.user_selected_mode):
            print("\nSelect game mode:\n1. Robot vs Dinosaur\n2. Fleet (3 Robots) vs Herd (3 Dinosaurs)")
            self.user_selected_mode = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode "))

    def select_units(self):
        self.robot_list = random.sample(['Exerminator', 'Destroyer', 'Annihilator', 'Executioner', 'Assassin', 'Eradicator', 'Demolisher'],
            int(f"{1 if int(self.user_selected_mode) == 1 else 3}"))
        self.dinosaur_list = random.sample(['T-Rex', 'Pterodactyl', 'Helicoprion', 'Stegasauri', 'Haopterus', 'Plesiosaur', 'Triseratopsu'], 
            int(f"{1 if int(self.user_selected_mode) == 1 else 3}"))
        for robot in self.robot_list:
            self.fleet.add_robot(Robot(robot, "Blast", 0))
        for dinosaur in self.dinosaur_list:
            self.herd.add_dinosaur(Dinosaur(dinosaur, random.randint(10, 25)))

    def display_players_stats(self):
        self.herd.display_dinosaurs_stats()
        self.select_robot_weapon()
        self.fleet.display_robots_stats()

    def select_robot_weapon(self):
        self.fleet.equip_robot()

    def coin_toss(self):
        self.coin_toss_status = f"\n{'RUFF MCGREE' if self.turn else 'DEADMAN'}: And now the coin toss. Its. . . "
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
            self.robot_turn() if self.turn else self.dinosaur_turn()
            self.display_att_status()
            self.fleet.remove_robot()
            self.herd.remove_dinosaur()
            self.turn = not(self.turn)        
            self.player_turn += 1
            
    def robot_turn(self):
        self.robo = self.fleet.display_robot_selection_menu()
        self.dino = self.herd.display_dinosaur_selection_menu()
        self.d20 = self.robo.attack(self.dino)

    def dinosaur_turn(self):
        self.dino = self.herd.select_dinosaur() 
        self.robo = self.fleet.select_robot()
        self.d20 = self.dino.attack(self.robo)

    def display_att_status(self):
        print(f"\nTurn {self.current_round}: {'Robots' if self.turn else 'Dinosaurs'}")       
        if self.turn: 
            print(f"{self.display_att_result(self.d20, self.robo, self.dino)[0]} Robot {self.robo.name} attacks {self.dino.name} with " 
              f"{self.robo.active_weapon.name} for {self.display_att_result(self.d20, self.robo, self.dino)[1]}\nDEADMAN: "
              f"Dinosaur {self.dino.name} has {self.dino.health if self.dino.health > 0 else 0} health remaining!")
        else:
            print(f"{self.display_att_result(self.d20, self.robo, self.dino)[0]} Dinosaur {self.dino.name} "
                f"{random.choice(['slashes', 'bites', 'rams'])} {self.robo.name} for {self.display_att_result(self.d20, self.robo, self.dino)[1]}"
                f"\nRUFF MCGREE: Robot {self.robo.name} has {self.robo.health if self.robo.health > 0 else 0} health remaining!")    

    def display_att_result(self, d20, robot, dinosaur):
        self.host_name = 'RUFF MCGREE' if self.turn else 'DEADMAN'
        self.attack_power = robot.active_weapon.attack_power if self.turn else dinosaur.attack_power
        self.defender = dinosaur.name if self.turn else robot.name
        self.hit = f"{self.host_name}: HIT!"
        self.status = f"{self.attack_power} damage!"
        if int(d20) in range(19, 20):
            self.hit = f"{self.host_name}: 3x CRITCAL HIT!"
            self.status = f"triple damage ({3 * self.attack_power} dmg)!"
        elif int(d20) in range(15, 18):
            self.hit = f"{self.host_name}: 2x CRITICAL HIT!"
            self.status = f"double damage ({2 * self.attack_power} dmg)!"
        elif int(d20) in range(7, 10):
            self.hit = f"{self.host_name}: WEAK HIT!"
            self.status= f"half the damage ({math.ceil(0.5 * self.attack_power)} dmg) as {self.defender} blocked the "\
                f"attack!"
        elif int(d20) in range(5, 7):
            self.hit = f"{self.host_name}: MISS!"
            self.status = f"0 damage as {self.defender} dodged the attack!"
        elif int(d20) in range(3, 5):
            self.hit = f"{self.host_name}: MISS!"
            self.status = f"0 damage as {self.defender} dodged the attack and healed a little bit!"
        elif int(d20) == 2:
            self.hit = f"{self.host_name}: MISS!"
            self.status = f"0 damage as {self.defender} dodged the attacked and healed quite a bit!"
        elif int(d20) == 1:
            self.hit = f"{self.host_name}: HIT REFLECTED!"
            self.status = f"{self.attack_power} damage but it was deflected back at "\
                f"{f'Robot {robot.name}' if self.turn else f'Dinosaur {dinosaur.name}'}!\n{'DEADMAN' if self.turn else 'RUFF MCGREE'}: "\
                f"{f'Robot {robot.name}' if self.turn else f'Dinosaur {dinosaur.name}'} "\
                f"has {(robot.health if robot.health > 0 else 0) if self.turn else (dinosaur.health if dinosaur.health > 0 else 0)} health remaining!"
        return self.hit, self.status

    def display_winner(self): 
        if len(self.fleet.fleet_list) == 0:
            print("\nDEADMAN: GAME OVERRRRR! THE RAGING DINOSAURS WIN!")
            return "dinosaurs"
        elif len(self.herd.herd_list) == 0: 
            print("\nRUFF MCGREE: GAME OVERRRRR! THE DESTRUCTIVE ROBOTS WIN!")
            return "robots"