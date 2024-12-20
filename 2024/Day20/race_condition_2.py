#!/usr/bin/env python

from sys import argv

def calculate_dist(pos_a, pos_b, x_len):
	return abs(pos_a % x_len - pos_b % x_len) + abs(pos_a // x_len - pos_b // x_len)

def calculate_saved_time(map, current_pos, x_len):
	count = 0
	for pos in range(x_len + 1, len(map)):
		if isinstance(map[pos], int):
			dist = calculate_dist(current_pos, pos, x_len)
			if dist < 21:
				if map[pos] - (map[current_pos] + dist) > 99:
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
	path = list()
	path.append(start)
	while map[end] == "E":
		for move in moves:
			if map[current_pos + move] == "." or map[current_pos + move] == "E":
				map[current_pos + move] = map[current_pos] + 1
				current_pos += move
				path.append(current_pos)
				break
	for pos in path:
		counter += calculate_saved_time(map, pos, x_len)
		map[pos] = "."
	print(counter)
	return 0

if __name__ == '__main__':
	cheats_counter()