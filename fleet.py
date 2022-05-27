from robot import Robot
from weapon import Weapon
import random
import re

class Fleet:
    def __init__(self):
        self.fleet_list = [] 
        self.weapons = []

    def add_robot(self, robot):
        self.fleet_list.append(robot)     

    def get_weapons(self):
        for i in range(3):
            self.weapon_name = random.choice(['Canon Launcher', 'Laser Blaster', 'Star Crusher'])
            self.weapons.append(Weapon(self.weapon_name, random.randint(10, 25)))   
         
    def equip_robot(self, robot_no):
        self.weapon_no = "9"
        while int(self.weapon_no) not in range(len(self.weapons)):
            print(f"\nSelect a weapon for robot {self.fleet_list[int(robot_no)].name}:")
            for n in range(len(self.weapons)):
                print(f"Input {n} to select: {self.weapons[n].name}, ATT: {self.weapons[n].attack_power}")
            self.weapon_no = re.sub(rf"[^0-{len(self.weapons) - 1}]", "9", input(f"\nPlayer selects to equip weapon "))
        print(f"Robot {self.fleet_list[int(robot_no)].name} has been equipped w/{self.weapons[int(self.weapon_no)].name} (ATT: " 
            f"{self.weapons[int(self.weapon_no)].attack_power})")
        return self.weapons.pop(int(self.weapon_no))

    def display_robots_stats(self):
        print(f"\nRUFF MCGREE: And in this corner the Destructive Robots. Looks like {self.select_robot().name} came to destroy!\n\n"
            f"The Destructive Robots Roster")
        for i in range(len(self.fleet_list)):
            print(f"{i + 1}. {self.fleet_list[i].name}, HP: {self.fleet_list[i].health}, Weapon: {self.fleet_list[i].active_weapon.name}, "\
                f"W_ATT: {self.fleet_list[i].active_weapon.attack_power}")

    def display_robot_selection_menu(self):
        self.robo_no = ""
        while len(self.robo_no) == 0:
            print("\nSelect an attacker:")
            for i in range(len(self.fleet_list)):
                print(f"Input {i} to select robot {self.fleet_list[i].name} (W_ATT: {self.fleet_list[i].active_weapon.attack_power}, HP:",\
                    f"{self.fleet_list[i].health})")
            self.robo_no = re.sub(rf"[^0-{len(self.fleet_list) - 1}]", "", input("\nPlayer selects Robot "))  
        print(f"You've selected {self.fleet_list[int(self.robo_no)].name}!") 
        return self.fleet_list[int(self.robo_no)]

    def select_robot(self):
        self.robot_attack_max = 0
        for n in range(len(self.fleet_list)):       
            if self.fleet_list[n].active_weapon.attack_power > self.robot_attack_max:
                self.robot_attack_max = self.fleet_list[n].active_weapon.attack_power
                self.robo_no = str(n)
        return self.fleet_list[int(self.robo_no)]

    def remove_robot(self):
        for i, robot in enumerate(self.fleet_list):
            if self.fleet_list[i].health <= 0:
                print(f"DEADMAN: Robot {self.fleet_list[i].name} has been ELIMINATED! The fleet has {len(self.fleet_list)-1} "
                    f"{'contender' if len(self.herd_list) - 1 == 1 else 'contenders'} remaining!")
                self.fleet_list.remove(robot)