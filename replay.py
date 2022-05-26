import re


class Replay:
    def __init__(self):
        self.raw_user_input = ""
        self.cor_user_input = ""

    def replay(self):
        while len(self.cor_user_input) == 0 or int(self.cor_user_input) not in range(2):
            self.raw_user_input = input("\nPlay again? (Input 0 for yes, 1 for no) ")
            self.cor_user_input = re.sub(r"[^0-1]", "", self.raw_user_input)
        if int(self.cor_user_input) == 0:
            return True
        else:
            return False