def rpsWinner(player_1_choice, player_2_choice):
    valid_choices = ['rock', 'paper', 'scissors']

    if player_1_choice not in valid_choices or player_2_choice not in valid_choices:
        return 'Not a valid choice by one of the players!'

    if player_1_choice == player_2_choice:
        return 'tie'
    elif player_1_choice == 'rock' and player_2_choice == 'paper':
        return 'player two'
    elif player_1_choice == 'paper' and player_2_choice == 'rock':
        return 'player one'
    elif player_1_choice == 'paper' and player_2_choice == 'scissors':
        return 'player two'
    elif player_1_choice == 'scissors' and player_2_choice == 'paper':
        return 'player one'
    elif player_1_choice == 'scissors' and player_2_choice == 'rock':
        return 'player two'
    elif player_1_choice == 'rock' and player_2_choice == 'scissors':
        return 'player one'


assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'

