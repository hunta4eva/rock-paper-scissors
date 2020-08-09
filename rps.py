import random
choices = 'Rock', 'Paper', 'Scissors'
results = 'Draw', 'Win', 'Lose'
while True:
    comp = random.randint(0,2)
    player = int(input("\n1: Rock  2: Paper  3: Scissors   :"))
    print(f'\nComputer: {choices[comp]} \nPlayer: {choices[player]} \nResult: {results[(player-comp)%3]}')
