class Herd:
    def __init__(self):
        self.herd_list = []

    def add_dinosaur(self, dinosaur):
        self.herd_list.append(dinosaur)

    def display_dinosaurs_stats(self):
        print("The Raging Dinosaurs Roster\n")
        for i in range(len(self.herd_list)):
            print(f"{i + 1}. {self.herd_list[i].name}, HP: {self.herd_list[i].health}, ATT: {self.herd_list[i].attack_power}")

    def display_dinosaur_selection(self):
        print("\nSelect a dinosaur to attack:")
        for i in range(len(self.herd_list)):
            print(f"Input {i} to select dinosaur {self.herd_list[i].name} (ATT: {self.herd_list[i].attack_power}, HP: {self.herd_list[i].health})")

    def remove_dinosaur(self):
        for i, dinosaur in enumerate(self.herd_list):
            if self.herd_list[i].health <= 0:
                print(f"Dinosaur {self.herd_list[i].name} has been ELIMINATED!")
                self.herd_list.remove(dinosaur)