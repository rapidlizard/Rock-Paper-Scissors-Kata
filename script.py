from game import who_wins
import random

options = ["scissors", "rock", "paper"]

print("choose rock, paper or scissors")

player_input = input()
bot_input = random.choice(options)

print(bot_input)
print(who_wins(player_input, bot_input))
