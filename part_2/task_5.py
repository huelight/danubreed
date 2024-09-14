# Random Name Selector (15 Points)

import random

friends = input("Enter the names of 5 friends, separated by commas: ").split(",")

# Randomly select a winner
winner = random.choice(friends)
print(f"The winner is: {winner}")
