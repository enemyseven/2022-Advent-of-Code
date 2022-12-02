#!/usr/bin/env python3

# 2022 Advent of Code - Day 02

#   Opponent
#   A   Rock        1
#   B   Paper       2
#   C   Scissors    3
#   Player
#   X   Rock        1
#   Y   Paper       2
#   Z   Scissors    3
#   Outcome
#   Lose    0
#   Draw    3
#   Win     6

total = 0

def score_round(opponent, player):
    if opponent == 'a': # Rock
        if player == 'x':   # Rock
            return 3    # Draw
        elif player == 'y': # Paper
            return 6    # Win
        elif player == 'z': # Scissors
            return 0    # Lose
    elif opponent == 'b':   # Paper
        if player == 'x':   # Rock
            return 0    # Lose
        elif player == 'y': # Paper
            return 3    # Draw
        elif player == 'z': # Scissors
            return 6    # Win
    elif opponent == 'c':   # Scissors
        if player == 'x':   # Rock
            return 6    # Win
        elif player == 'y': # Paper
            return 0    # Lose
        elif player == 'z': # Scissors
            return 3    # Draw
    else:
        return -1
    
def get_value(letter):
    if letter == 'a':
        return 1
    elif letter == 'b':
        return 2
    elif letter == 'c':
        return 3
    elif letter == 'x':
        return 1
    elif letter == 'y':
        return 2
    elif letter == 'z':
        return 3
    

with open('02-input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        opponent, player = line.lower().split()
        win_outcome = score_round(opponent, player)
        play_value = get_value(player)
        total += win_outcome + play_value

print(f"Value: {total}")
