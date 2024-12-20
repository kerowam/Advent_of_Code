#!/usr/bin/env python

from sys import argv

def possible_cheat(map, current_pos, moves):
	for move in moves:
		if 0 <= current_pos + move * 2 < len(map) and 0 <= current_pos + move < len(map):
			if map[current_pos + move] == "#" and isinstance(map[current_pos + move * 2], int):
				return True
	return False

def calculate_saved_time(map, current_pos, moves):
	count = 0
	for move in moves:
		if 0 <= current_pos + move * 2 < len(map) and 0 <= current_pos + move < len(map):
			if map[current_pos + move] == "#" and isinstance(map[current_pos + move * 2], int):
				if map[current_pos] - (map[current_pos + move * 2] + 2) > 99:
					count += 1
	return count

def cheats_counter():
	counter = 0
	with open(argv[1]) as f:
		lines = [line.strip() for line in f]
	x_len = len(lines[0])
	map = list("".join(lines))
	start, end = (map.index("S"), map.index("E"))
	moves = [-x_len, 1, x_len, -1]
	map[start] = 0
	current_pos = start
	while map[end] == "E":
		if possible_cheat(map, current_pos, moves):
			counter += calculate_saved_time(map, current_pos, moves)
		for move in moves:
			if map[current_pos + move] == "." or map[current_pos + move] == "E":
				map[current_pos + move] = map[current_pos] + 1
				current_pos += move
				break
	if possible_cheat(map, current_pos, moves):
		counter += calculate_saved_time(map, current_pos, moves)
	print(counter)
	return 0

if __name__ == '__main__':
	cheats_counter()