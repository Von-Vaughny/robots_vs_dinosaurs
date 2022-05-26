from battlefield import Battlefield
from replay import Replay


user_input = True
times_played = 0
wins = [0, 0]

while user_input:
    battlefield_one = Battlefield()
    winner = battlefield_one.run_game()
    replay = Replay()
    user_input = replay.replay()
    times_played += 1
    if winner == "robots":
        wins[0] = int(wins[0]) + 1
    elif winner == "dinosaurs":
        wins[1] = int(wins[1]) + 1

print(f"\nYou have played a total of {times_played} games!")
print(f"The Destructive Robots wins: {wins[0]}")
print(f"The Raging Dinosaurs wins: {wins[1]}\n")


