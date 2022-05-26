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
        self.weapons = [Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25)),
                        Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25)),
                        Weapon(random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher']), random.randint(10, 25))]
        self.robot_names = ['Terminator', 'Destroyer', "Annihilator"]   
        self.turn = random.choice([True, False])
        self.user_input, self.robo_no, self.dino_no = "", "", ""
        self.player_turn, self.robo_wins, self.dino_wins  = 1, 0, 0 
           
    def run_game(self):
        self.display_welcome()
        self.display_players_stats()
        self.coin_toss()
        self.battle_phase()
        self.winner = self.display_winner()
        return self.winner

    def display_welcome(self):
        print("Robots vs Dinosaurs\n\nWelcome to the battle of the ages! There can only be one! Which side will win?\n")

    def display_players_stats(self):
        self.herd.display_dinosaurs_stats()
        self.select_robot_weapon()
        self.fleet.display_robots_stats()

    def select_robot_weapon(self):
        for i in range(len(self.robot_names)):
            while len(self.user_input) == 0 or int(self.user_input) not in range(len(self.weapons)):
                print(f"\nSelect a weapon for robot {self.robot_names[i]}:")
                for n in range(len(self.weapons)):
                    print(f"Input {n} to select: {self.weapons[n].name}, ATT: {self.weapons[n].attack_power}")
                self.raw_user_input = input("\nPlayer equips weapon ")
                self.user_input = re.sub(r"[^0-2]", "", self.raw_user_input)
            print(f"You've selected {self.weapons[int(self.user_input)].name} (ATT: {self.weapons[int(self.user_input)].attack_power})")
            self.fleet.add_robot(Robot(self.robot_names[i], self.weapons[int(self.user_input)].name, self.weapons[int(self.user_input)].attack_power))
            self.weapons.remove(self.weapons[int(self.user_input)])
            self.user_input = ""

    def coin_toss(self):
        print("\nCoin Toss Results")
        if self.turn:
            print(f"The coin toss result is in and its... HEADS! The Destructive Robots will be starting this battle!")
        elif not(self.turn):
            print(f"The coin toss result is in and its... TAILS! The Raging Dinosaurs will be starting this battle!")

    def battle_phase(self):
        while len(self.fleet.fleet_list) > 0 and len(self.herd.herd_list) > 0:
            self.current_round = math.ceil(self.player_turn/2)
            if self.turn:
                self.robots_turn()
            else:
                self.dinosaurs_turn()
            self.fleet.remove_robot()
            self.herd.remove_dinosaur()
            self.turn = not(self.turn)        
            self.player_turn += 1
            
    def robots_turn(self):
        self.robo_no, self.dino_no = "", ""
        while len(self.robo_no) == 0 or int(self.robo_no) not in range(len(self.fleet.fleet_list)):
            self.fleet.display_robot_selection()
            self.robo_no = re.sub(r"[^0-2]", "", input("\nRobot "))
        print(f"You've selected {self.fleet.fleet_list[int(self.robo_no)].name}!")
        while len(self.dino_no) == 0 or int(self.dino_no) not in range(len(self.herd.herd_list)):
            self.herd.display_dinosaur_selection()
            self.dino_no = re.sub(r"[^0-2]", "", input("\nDinosuar "))
        print(f"You've selected to attack {self.herd.herd_list[int(self.dino_no)].name}")
        self.d20 = int(self.fleet.fleet_list[int(self.robo_no)].attack(self.herd.herd_list[int(self.dino_no)]))
        print(f"\nTurn {self.current_round}: Robots")
        print(f"{self.display_robot_attack(self.d20, self.robo_no, self.dino_no)[0]} Robot {self.fleet.fleet_list[int(self.robo_no)].name} attacks " 
              f"{self.herd.herd_list[int(self.dino_no)].name} with {self.fleet.fleet_list[int(self.robo_no)].active_weapon.name} for", 
              f"{self.display_robot_attack(self.d20, self.robo_no, self.dino_no)[1]}")
        print(f"Dinosaur {self.herd.herd_list[int(self.dino_no)].name} has "
              f"{self.herd.herd_list[int(self.dino_no)].health if self.herd.herd_list[int(self.dino_no)].health > 0 else 0} health remaining!")

    def display_robot_attack(self, d20, robo_no, dino_no):
        hit = "HIT!"
        status = f"{self.fleet.fleet_list[int(robo_no)].active_weapon.attack_power} damage!"
        if int(d20) in range(19, 20):
            hit = "3x CRITCAL HIT!"
            status = f"triple damage ({3 * self.fleet.fleet_list[int(robo_no)].active_weapon.attack_power} dmg)!"
        elif int(d20) in range(15, 18):
            hit = "2x CRITICAL HIT!"
            status = f"double damage ({2 * self.fleet.fleet_list[int(robo_no)].active_weapon.attack_power} dmg)!"
        elif int(d20) in range(7, 10):
            hit = "WEAK HIT!"
            status= f"half the damage ({math.ceil(0.5 * self.fleet.fleet_list[int(robo_no)].active_weapon.attack_power)} dmg) as "\
                f"{self.herd.herd_list[int(dino_no)].name} blocked the attack!"
        elif int(d20) in range(5, 7):
            hit = "MISS!"
            status = f"0 damage as {self.herd.herd_list[int(dino_no)].name} dodged the attack!"
        elif int(d20) in range(3, 5):
            hit = "MISS!"
            status = f"0 damage as {self.herd.herd_list[int(dino_no)].name} dodged the attack and healed a little bit!"
        elif int(d20) == 2:
            hit = "MISS!"
            status = f"0 damage as {self.herd.herd_list[int(dino_no)].name} dodged the attacked and healed quite a bit!"
        elif int(d20) == 1:
            hit = "HIT REFLECTED!"
            status = f"{self.fleet.fleet_list[int(robo_no)].active_weapon.attack_power} damage but it was deflected back at Robot "\
                        f"{self.fleet.fleet_list[int(robo_no)].name}!\nRobot {self.fleet.fleet_list[int(robo_no)]} has "\
                        f"{self.fleet.fleet_list[int(robo_no)]} health remaining!"
        return hit, status

    def dinosaurs_turn(self):
        self.dinosaur_attack_max, self.robot_attack_max = 0, 0
        for n in range(len(self.herd.herd_list)):
            if self.herd.herd_list[n].attack_power > self.dinosaur_attack_max:
                self.dinosaur_attack_max = self.herd.herd_list[n].attack_power
                self.dino_no = str(n)
        for n in range(len(self.fleet.fleet_list)):       
            if self.fleet.fleet_list[n].active_weapon.attack_power > self.robot_attack_max:
                self.robot_attack_max = self.fleet.fleet_list[n].active_weapon.attack_power
                self.robo_no = str(n)
        self.d20 = int(self.herd.herd_list[int(self.dino_no)].attack(self.fleet.fleet_list[int(self.robo_no)]))
        print(f"\nTurn {self.current_round}: Dinosaurs")
        print(f"{self.display_dinosaur_attack(self.d20, self.dino_no, self.robo_no)[0]} Dinosaur {self.herd.herd_list[int(self.dino_no)].name} "
            f"attacks {self.fleet.fleet_list[int(self.robo_no)].name} for", self.display_dinosaur_attack(self.d20, self.dino_no, self.robo_no)[1])
        print(f"Robot {self.fleet.fleet_list[int(self.robo_no)].name} has "
            f"{self.fleet.fleet_list[int(self.robo_no)].health if self.fleet.fleet_list[int(self.robo_no)].health > 0 else 0} health remaining!")       

    def display_dinosaur_attack(self, d20, dino_no, robo_no):
        hit = "HIT!"
        status = f"{self.herd.herd_list[int(dino_no)].attack_power} damage!"
        if int(d20) in range(19, 20):
            hit = "3x CRITICAL HIT!"
            status = f"triple damage ({3 * self.herd.herd_list[int(dino_no)].attack_power} dmg)!"
        elif int(d20) in range(15, 18):
            hit = "2x CRITICAL HIT!"
            status = f"double damage ({2 * self.herd.herd_list[int(dino_no)].attack_power} dmg)!"
        elif int(d20) in range(7, 10):
            hit = "WEAK HIT!"
            status = f"half the damage ({math.ceil(0.5 * self.herd.herd_list[int(dino_no)].attack_power)} dmg) as "\
                f"{self.fleet.fleet_list[int(robo_no)].name} blocked the attack!"   
        elif int(d20) in range(5, 7):
            hit = "MISS!"
            status = f"0 damage as {self.fleet.fleet_list[int(robo_no)].name} dodged the attack!"
        elif int(d20) in range(3, 5):
            hit = "MISS!"
            status = f"0 damage as {self.fleet.fleet_list[int(robo_no)].name} dodged the attack and healed a little bit!"    
        elif int(d20) == 2:
            hit = "MISS!"
            status = f"0 damage as {self.fleet.fleet_list[int(robo_no)].name} dodged the attack and healed quite a bit!"  
        elif int(d20) == 1:
            hit = "HIT REFLECTED!"    
            status = f"{self.herd.herd_list[int(dino_no)].attack_power} damage but it was deflected back at dinosaur "\
                f"{self.herd.herd_list[int(dino_no)].name}!\nDinosaur {self.herd.herd_list[int(dino_no)].name} has "\
                f"{self.herd.herd_list[int(dino_no)].health} remaining!"   
        return hit, status

    def display_winner(self): 
        if len(self.fleet.fleet_list) == 0:
            print("\nTHE RAGING DINOSAURS WIN!")
            return "dinosaurs"
        elif len(self.herd.herd_list) == 0: 
            print("\nTHE DESTRUCTIVE ROBOTS WIN!")
            return "robots"
