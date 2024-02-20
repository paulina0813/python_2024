import random

players = ['Paulina', 'Ibra', 'Maggie']
exercises = [1,2,3,4,5,6,7,8,9,10,11,12]
winners = []

'''
for index, exercises in enumerate(exercises):
    winner = random.choice(players)
    winners.append(winner)

for index, winner in enumerate(winners):
    print(index + 1, winner)
'''

for index in range(1,13):
    winner = random.choice(players)
    winners.append(winner)
print(winners)

for index, winner in enumerate(winners):
    winners  = index + 1, winner
    print(winners)
    file = open('list_winners.txt', 'a')
    file.write(winners)
