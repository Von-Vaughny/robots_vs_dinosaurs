from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.herd_list = []

    def add_dinosaur(self, dinosaur):
        self.herd_list.append(dinosaur)

    def display_dinosaur_selection(self):
        for i in range(len(self.herd_list)):
            print(f"Input {i} to select dinosaur {self.herd_list[i].name} (ATT: {self.herd_list[i].attack_power}, HP: {self.herd_list[i].health})")
        print()

    def remove_dinosaur(self):
        for i, j in enumerate(self.herd_list):
            if self.herd_list[i].health <= 0:
                self.herd_list.remove(j)