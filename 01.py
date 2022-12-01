#!/usr/bin/env python3

totals = []

with open('01-input.txt') as f:
	lines = f.readlines()
	running_total = 0
	for line in lines:
		line = line.strip()
		if '' != line:
			running_total += int(line)
		else:
			totals.append(running_total)
			running_total = 0

print(max(totals))




