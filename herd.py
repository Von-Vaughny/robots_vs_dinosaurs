import re

class Herd:
    def __init__(self):
        self.herd_list = []

    def add_dinosaur(self, dinosaur):
        self.herd_list.append(dinosaur)

    def display_dinosaurs_stats(self):
        print(f"DEADMAN: In this corner the Raging Dinosaurs! And look at the power on {self.select_dinosaur().name}, Ruff! He did not come to play.  "
            f"He came to WIN!\n\nThe Raging Dinosaurs Roster")
        for i in range(len(self.herd_list)):
            print(f"{i + 1}. {self.herd_list[i].name}, HP: {self.herd_list[i].health}, ATT: {self.herd_list[i].attack_power}")

    def display_dinosaur_selection_menu(self):
        self.dino_no = ""
        while len(self.dino_no) == 0:
            print("\nSelect a dinosaur to attack:")
            for i in range(len(self.herd_list)):
                print(f"Input {i} to select dinosaur {self.herd_list[i].name} (ATT: {self.herd_list[i].attack_power}, HP: {self.herd_list[i].health})")
            self.dino_no = re.sub(rf"[^0-{len(self.herd_list) - 1}]", "", input("\nPlayer selects Dinosuar "))
        print(f"You've selected to attack {self.herd_list[int(self.dino_no)].name}")
        return self.herd_list[int(self.dino_no)]

    def select_dinosaur(self):
        self.dinosaur_attack_max = 0
        for n in range(len(self.herd_list)):
            if self.herd_list[n].attack_power > self.dinosaur_attack_max:
                self.dinosaur_attack_max = self.herd_list[n].attack_power
                self.dino_no = str(n)
        return self.herd_list[int(self.dino_no)]

    def remove_dinosaur(self):
        for i, dinosaur in enumerate(self.herd_list):
            if self.herd_list[i].health <= 0:
                print(f"RUFF MCGREE: Dinosaur {self.herd_list[i].name} has been ELIMINATED! The herd has {len(self.herd_list)-1} "
                    f"{'contender' if len(self.herd_list) - 1 == 1 else 'contenders'} remaining!")
                self.herd_list.remove(dinosaur)