import sys
sys.path.append('../utils')
from utils import input

'''
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors

A > C
C > B
B > A

The score for a single round is the score for the shape you selected
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
 (0 if you lost, 3 if the round was a draw, and 6 if you won).
 '''

scenarios = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3},
}
value = {"X": 1, "Y": 2, "Z": 3 }

# part 1
sum = 0
for line in input():
    choices = line.strip().split(" ")
    sum += value[choices[1]] + scenarios[choices[1]][choices[0]]

print(sum)


# part 2
# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win"

scenarios = {
    "A": {3: "A", 6: "B", 0: "C"},
    "B": {0: "A", 3: "B", 6: "C"},
    "C": {6: "A", 0: "B", 3: "C"},
}
goals = {"X": 0, "Y": 3, "Z": 6 }
value = {"A": 1, "B": 2, "C": 3 }

sum = 0
for line in input():
    choices = line.strip().split(" ")
    goal = goals[choices[1]]
    choice = scenarios[choices[0]][goal]
    sum += goal + value[choice]

print(sum)

