from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_list = []

    def add_robot(self, robot):
        self.fleet_list.append(robot)

    def display_robot_selection(self):
        for i in range(len(self.fleet_list)):
            print(f"Input {i} to select robot {self.fleet_list[i].name} (ATT: {self.fleet_list[i].active_weapon.attack_power}, HP:",\
                f"{self.fleet_list[i].health})")
        print()

    def remove_robot(self):
        for i, j in enumerate(self.fleet_list):
            if self.fleet_list[i].health <= 0:
                self.fleet_list.remove(j)