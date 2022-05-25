from fleet import Fleet
from herd import Herd
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
import random
import math
import re


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
        self.herd.add_dinosaur(Dinosaur('T-Rex', random.randint(10, 25)))
        self.herd.add_dinosaur(Dinosaur('Pterodactyl', random.randint(10, 25)))
        self.herd.add_dinosaur(Dinosaur('Helicoprion', random.randint(10, 25)))    
        # Can probably minimize this. Just need to randomly choose name and atack power.   
        self.weapon_1 = Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25))
        self.weapon_2 = Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25))
        self.weapon_3 = Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25))
        self.weapons = [self.weapon_1, self.weapon_2, self.weapon_3]
        self.player_turn = 1
           
    def run_game(self):
        self.display_welcome()
        self.display_players_stats()
        self.coin_toss()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Robot vs Dinosaur\n\nWelcome to the battle of the ages! There can only be one! Which side will win?\n")

    def display_players_stats(self):
        print("The Raging Dinosaurs Roster\n")
        for i in range(len(self.herd.herd_list)):
            print(f"{i + 1}. {self.herd.herd_list[i].name}, HP: {self.herd.herd_list[i].health}, ATT: {self.herd.herd_list[i].attack_power}")
        self.select_robot_weapon()
        print("\nThe Destructive Robots Roster\n")
        for i in range(len(self.fleet.fleet_list)):
            print(f"{i + 1}. {self.fleet.fleet_list[i].name}, HP: {self.fleet.fleet_list[i].health}, Weapon: "\
                f"{self.fleet.fleet_list[i].active_weapon.name}, ATT: {self.fleet.fleet_list[i].active_weapon.attack_power}")
        print()

    def select_robot_weapon(self):
        self.robot_names = ['Terminator', 'Destroyer', "Annihilator"]
        for i in range(len(self.robot_names)):
            print(f"\nSelect a weapon for robot {self.robot_names[i]}:")
            for n in range(len(self.weapons)):
                print(f"Input {n} to select: {self.weapons[n].name}, ATT: {self.weapons[n].attack_power}")
            self.m = input("\nWeapon ")
            self.n = re.sub(r"[^0-9]", "", self.m)
            while len(self.n) == 0 or int(self.n) not in range(len(self.weapons)):
                print(f"\nSelect a weapon for robot {self.robot_names[i]}\n")
                for n in range(len(self.weapons)):
                    print(f"Input {n} to select: {self.weapons[n].name}, ATT: {self.weapons[n].attack_power}")
                self.m = input("\nWeapon ")
                self.n = re.sub(r"[^0-9]", "", self.m)
            if int(self.n) in range(len(self.weapons)):
                print(f"You've selected {self.weapons[int(self.n)].name} (ATT: {self.weapons[int(self.n)].attack_power})")
                self.fleet.add_robot(Robot(self.robot_names[i], self.weapons[int(self.n)].name, self.weapons[int(self.n)].attack_power))
                self.weapons.remove(self.weapons[int(self.n)])

    def coin_toss(self):
        # Can probably simplify this.
        self.coin = random.choice(['heads', 'tails'])
        self.turn = True
        if self.coin == 'tails':
            self.turn = not(self.turn)
        print("Coin Toss Results")
        if self.turn == True:
            print(f"The coin toss result is in and its... {self.coin.upper()}! The Destructive Robots will be starting this battle!")
        elif self.turn == False:
            print(f"The coin toss result is in and its... {self.coin.upper()}! The Raging Dinosaurs will be starting this battle!")

    # Consider reducing lines of code: initializing variables in the init(), creating a battle_phase_battle_status() for status, fix the 
    # "has been ELIMINATED" as a reflect could knock out a player on the player's own turn - probably need to use different variables in
    # the (current_player)_turn().  
    def battle_phase(self):
        while len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) > 0:
            self.current_turn = math.ceil(self.player_turn/2)
            i, j = 0, 0
            if self.turn == True:
                i, j = self.robots_turn()
                n = int(self.fleet.fleet_list[i].attack(self.herd.herd_list[j]))
                print(f"\nTurn {self.current_turn}: Robots")
                print(f"{self.display_robot_attack(n, i, j)[0]} Robot {self.fleet.fleet_list[i].name} attacks {self.herd.herd_list[j].name} with "\
                    f"{self.fleet.fleet_list[i].active_weapon.name} for", self.display_robot_attack(n, i, j)[1])
                print(f"Dinosaur {self.herd.herd_list[j].name} has {self.herd.herd_list[j].health if self.herd.herd_list[j].health > 0 else 0} "\
                    f"health remaining! ")
                if self.herd.herd_list[j].health <= 0:
                    print(f"Dinosaur {self.herd.herd_list[j].name} has been ELIMINATED!")
                    self.herd.remove_dinosaur()
                self.turn = False
            elif self.turn == False:
                i, j = self.dinosaurs_turn()
                n = int(self.herd.herd_list[i].attack(self.fleet.fleet_list[j]))
                print(f"\nTurn {self.current_turn}: Dinosaurs")
                print(f"{self.display_dinosaur_attack(n, i, j)[0]} Dinosaur {self.herd.herd_list[i].name} attacks {self.fleet.fleet_list[j].name} for",\
                    self.display_dinosaur_attack(n, i, j)[1])
                print(f"Robot {self.fleet.fleet_list[j].name} has {self.fleet.fleet_list[j].health if self.fleet.fleet_list[j].health > 0 else 0} "\
                    f"health remaining!")
                if self.fleet.fleet_list[j].health <= 0:
                    print(f"Robot {self.fleet.fleet_list[j].name} has been ELIMINATED!")
                    self.fleet.remove_robot()
                self.turn = True            
            self.player_turn += 1
            
    # Consider reducing lines of code
    def robots_turn(self):
        print("\nSelect your attacking robot:")
        self.fleet.display_robot_selection()
        self.h = input("Robot ")
        self.i = re.sub(r"[^0-9]", "", self.h)
        while len(self.i) == 0 or int(self.i) not in range(len(self.fleet.fleet_list)):
            print("\nSelect your attacking robot:")
            self.fleet.display_robot_selection()
            self.h = input("Robot ")
            self.i = re.sub(r"[^0-9]", "", self.h)
        if int(self.i) in range(len(self.fleet.fleet_list)):
            print(f"You've selected {self.fleet.fleet_list[int(self.i)].name}!")
            print("\nSelect a dinosaur to attack:")
            self.herd.display_dinosaur_selection()
            self.k = input("Dinosaur ")
            self.j = re.sub(r"[^0-9]", "", self.k)
            while len(self.j) == 0 or int(self.j) not in range(len(self.herd.herd_list)):
                print("\nSelect a dinosaur to attack:")
                self.herd.display_dinosaur_selection()
                self.k = input("Dinosuar ")
                self.j = re.sub(r"[^0-9]", "", self.k)
            print(f"You've selected to attack {self.herd.herd_list[int(self.j)].name}")
        self.turn = False
        return int(self.i), int(self.j)
    
    # Consider reducing lines of code, intializing variables in init(), Reconfigure the conditions. Maybe include another if/else 
    # clause after "if int(self.herd.herd_list[n-1].attack_power) >= int(self.herd.herd_list[n].attack_power):" to check if it
    # the value is bigger than self.dinosaur_attack_max, self.robot_attack_max to select max.
    def dinosaurs_turn(self):
        self.dinosaur_attack_max, self.robot_attack_max = 0, 0
        i, j = 0, 0
        for n in range(1, len(self.herd.herd_list)-1):
            if int(self.herd.herd_list[n-1].attack_power) >= int(self.herd.herd_list[n].attack_power):
                self.dinosaur_attack_max = int(self.herd.herd_list[n-1].attack_power)
            else:
                self.dinosaur_attack_max = int(self.herd.herd_list[n].attack_power)
        for n in range(len(self.herd.herd_list)):
            if self.herd.herd_list[n].attack_power == self.dinosaur_attack_max:
                i = n
        for n in range(1, len(self.fleet.fleet_list)-1):
            if int(self.fleet.fleet_list[n-1].active_weapon.attack_power) >= int(self.fleet.fleet_list[n].active_weapon.attack_power):
                self.robot_attack_max = int(self.fleet.fleet_list[n-1].active_weapon.attack_power)
            else:
                self.robot_attack_max = int(self.fleet.fleet_list[n].active_weapon.attack_power)
        for n in range(len(self.fleet.fleet_list)):
            if self.fleet.fleet_list[n].active_weapon.attack_power == self.robot_attack_max:
                j = n
        return i, j
    
    # Consider moving hit to its own function and/or combining display_(player)_attack by the self.turn booleaan to determine statements.
    def display_robot_attack(self, n, i, j):
        hit = "HIT!"
        statement = f"{self.fleet.fleet_list[int(i)].active_weapon.attack_power} damage!"
        if n == 1: 
            hit = "3x CRITCAL HIT!"
            statement = f"triple damage ({3 * self.fleet.fleet_list[int(i)].active_weapon.attack_power} dmg)!"
        elif n in range(2, 10):
            hit = "2x CRITICAL HIT!"
            statement = f"double damage ({2 * self.fleet.fleet_list[int(i)].active_weapon.attack_power} dmg)!"
        elif n == 100:
            hit = "MISS!"
            statement = f"0 damage as {self.herd.herd_list[int(j)].name} dodged the attacked and healed quite a bit!"
        elif n in range(96, 99):
            hit = "MISS!"
            statement = f"0 damage as {self.herd.herd_list[int(j)].name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            hit = "MISS!"
            statement = f"0 damage as {self.herd.herd_list[int(j)].name} dodged the attack!"
        elif n in range(53, 85):
            hit = "WEAK HIT!"
            statement = f"half the damage ({math.ceil(0.5 * self.fleet.fleet_list[int(i)].active_weapon.attack_power)} dmg) as "\
                f"{self.herd.herd_list[int(j)].name} blocked the attack!"
        elif n == 50:
            hit = "HIT REFLECTED!"
            statement = f"{self.fleet.fleet_list[int(i)].active_weapon.attack_power} damage but it was deflected back at Robot "\
                        f"{self.fleet.fleet_list[int(i)].name}!"
        return hit, statement

    def display_dinosaur_attack(self, n, i, j):
        hit = "HIT!"
        statement = f"{self.herd.herd_list[int(i)].attack_power} damage!"
        if n == 1:
            hit = "3x CRITICAL HIT!"
            statement = f"triple damage ({3 * self.herd.herd_list[int(i)].attack_power} dmg)!"
        elif n in range(2, 10):
            hit = "2x CRITICAL HIT!"
            statement = f"double damage ({2 * self.herd.herd_list[int(i)].attack_power} dmg)!"
        elif n == 100:
            hit = "MISS!"
            statement = f"0 damage as {self.fleet.fleet_list[int(j)].name} dodged the attack and healed quite a bit!"
        elif n in range(96, 99):
            hit = "MISS!"
            statement = f"0 damage as {self.fleet.fleet_list[int(j)].name} dodged the attack and healed a little bit!"
        elif n in range(86, 95):
            hit = "MISS!"
            statement = f"0 damage as {self.fleet.fleet_list[int(j)].name} dodged the attack!"     
        elif n in range(53, 85):
            hit = "WEAK HIT!"
            statement = f"half the damage ({math.ceil(0.5 * self.herd.herd_list[int(i)].attack_power)} dmg) as {self.fleet.fleet_list[int(j)].name} "\
                f"blocked the attack!"    
        elif n == 50:
            hit = "HIT REFLECTED!"    
            statement = f"{self.herd.herd_list[int(i)].attack_power} damage but it was deflected back at dinosaur {self.herd.herd_list[int(i)].name}!"   
        return hit, statement

    def display_winner(self): 
        if len(self.fleet.fleet_list) == 0:
            print("\nTHE RAGING DINOSAURS WIN!")
        elif len(self.herd.herd_list) == 0: 
            print("\nTHE DESTRUCTIVE ROBOTS WIN!")
