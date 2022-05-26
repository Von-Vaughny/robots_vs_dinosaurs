class Fleet:
    def __init__(self):
        self.fleet_list = [] 

    def add_robot(self, robot):
        self.fleet_list.append(robot)     

    def display_robots_stats(self):
        print("\nThe Destructive Robots Roster\n")
        for i in range(len(self.fleet_list)):
            print(f"{i + 1}. {self.fleet_list[i].name}, HP: {self.fleet_list[i].health}, Weapon: {self.fleet_list[i].active_weapon.name}, "\
                f"ATT: {self.fleet_list[i].active_weapon.attack_power}")

    def display_robot_selection(self):
        print("\nSelect your attacking robot:")
        for i in range(len(self.fleet_list)):
            print(f"Input {i} to select robot {self.fleet_list[i].name} (W_ATT: {self.fleet_list[i].active_weapon.attack_power}, HP:",\
                f"{self.fleet_list[i].health})")

    def remove_robot(self):
        for i, robot in enumerate(self.fleet_list):
            if self.fleet_list[i].health <= 0:
                print(f"Robot {self.fleet_list[i].name} has been ELIMINATED!")
                self.fleet_list.remove(robot)