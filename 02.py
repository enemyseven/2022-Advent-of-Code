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
planned = 0

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
        
def get_win(letter):
    if letter == 'a':
        return 'y'
    elif letter == 'b':
        return 'z'
    elif letter == 'c':
        return 'x'

def get_lose(letter):
    if letter == 'a':
        return 'z'
    elif letter == 'b':
        return 'x'
    elif letter == 'c':
        return 'y'
        
def get_draw(letter):
    if letter == 'a':
        return 'x'
    elif letter == 'b':
        return 'y'
    elif letter == 'c':
        return 'z'

def choose_response(opponent, wld):
    wld_value = 0
    letter = '0'
    
    if wld == 'x':
        wld_value = 0
        letter = get_lose(opponent)
    elif wld == 'y':
        wld_value = 3
        letter = get_draw(opponent)
    elif wld == 'z':
        wld_value = 6
        letter = get_win(opponent)
        
    return wld_value + get_value(letter)

with open('02-input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        opponent, player = line.lower().split()
        win_outcome = score_round(opponent, player)
        play_value = get_value(player)
        total += win_outcome + play_value
        planned += choose_response(opponent, player)

print(f"Value: {total}")
print(f"Planned: {planned}")
