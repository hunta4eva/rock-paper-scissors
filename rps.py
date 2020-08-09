import random
choices = (('r', 'rock'), ('p', 'paper'), ('s', 'scissors'))
results = 'Draw', 'Win', 'Lose'
while True:
    comp = random.randint(0,2)
    player = input("\nRock, Paper or Scissors?  ").lower()[0]
    player_int = [i for i, j in enumerate(choices) if j[0] == player][0]
    print(f'\nComputer: {choices[comp][1].title()} \nPlayer: {choices[player_int][1].title()} \nResult: {results[(player_int-comp)%3]}')
