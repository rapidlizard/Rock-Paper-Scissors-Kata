
def is_input_valid(input, options):
    if input in options:
        return True
    return False


def who_wins(player, bot):
    options = ["rock", "paper", "scissors"]
    if not is_input_valid(player, options):
        return "Your choice is invalid. Please type: rock, paper or scissors"

    if player == bot:
        return "its a draw"

    if player == "paper" and bot == "rock":
        return "player wins"

    if player == "rock" and bot == "scissors":
        return "player wins"

    if player == "scissors" and bot == "paper":
        return "player wins"

    return "bot wins"
