# Random Team Generator (40 points)

import random

players = input("Enter the names of the players, separated by commas: ").split(",")

random.shuffle(players)

team1 = players[:len(players)//2]
team2 = players[len(players)//2:]

print(f"Team 1: {team1}")
print(f"Team 2: {team2}")