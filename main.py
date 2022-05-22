from robot import Robot
from dinosaur import Dinosaur
import random


robot_1 = Robot('Terminator')
print(f"Robot A is named {robot_1.name}. It has {robot_1.health} health points and it's active weapon {robot_1.active_weapon.name} deals "\
      f"{robot_1.active_weapon.attack_power} damage.\n")

dinosaur_1 = Dinosaur('T-Rex', random.randint(10, 25))
print(f"Dinosaur A is named {dinosaur_1.name}. It has {dinosaur_1.health} health points and it deals {dinosaur_1.attack_power}")


