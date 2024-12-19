#!/usr/bin/env python

from sys import argv
import copy

def flood_fill(map, x, y):
	moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
	map[y][x] = "X"
	for move in moves:
		new_x = x + move[0]
		new_y = y + move[1]
		if 0 <= new_x < 71 and 0 <= new_y < 71 and map[new_y][new_x] == ".":
			flood_fill(map, new_x, new_y)
	return map

def find_byte_cutting_path_off():
	map = list()
	input_positions = list()
	for y in range(71):
		line = list()
		for x in range(71):
			line.append(".")
		map.append(line)
	with open(argv[1]) as f:
		lines = f.readlines()
		for line in lines:
			position = line.split(",")
			x = int(position[0])
			y = int(position[1])
			input_positions.append((x, y))
			map[y][x] = "#"
	inverted_positions = input_positions[::-1]
	print(len(inverted_positions))
	for position in inverted_positions:
		x = position[0]
		y = position[1]
		map[y][x] = "."
		filled_map = copy.deepcopy(map)
		filled_map = flood_fill(filled_map, 0, 0)
		if filled_map[70][70] == "X":
			print(x, y)
			return 0
	return 0

if __name__ == '__main__':
	find_byte_cutting_path_off()