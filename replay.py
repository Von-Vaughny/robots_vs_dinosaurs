import re


class Replay:
    def __init__(self):
        self.cor_user_input = ""

    def replay(self):
        while len(self.cor_user_input) == 0:
            self.cor_user_input = re.sub(r"[^0-1]", "", input("\nPlay again? (Input 0 for no, 1 for yes) "))
        return True if int(self.cor_user_input) == 1 else False