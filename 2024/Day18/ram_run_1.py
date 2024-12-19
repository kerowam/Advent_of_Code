#!/usr/bin/env python

from sys import argv
from heapq import heappop, heappush
from math import inf

def get_map_filled(map):
	with open(argv[1]) as f:
		lines = f.readlines()
		count = 0
		for line in lines:
			if count > 1023:
				break
			position = line.split(",")
			x = int(position[0])
			y = int(position[1])
			map[y][x] = "#"
			count += 1
	return map

def calculate_minimun_step_number():
	map = list()
	for y in range(71):
		line = list()
		for x in range(71):
			line.append(".")
		map.append(line)
	map = get_map_filled(map)
	for line in map:
		for char in line:
			print(char, end="")
		print()
	start = (0, 0)
	end = (70, 70)
	moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
	visited_positions = dict()
	min_steps = inf
	heap = list()
	heappush(heap, (0, start))
	while heap:
		steps, position = heappop(heap)
		if steps > min_steps:
			break
		if position in visited_positions and steps >= visited_positions[position]:
			continue
		if position == end:
			min_steps = steps
			break
		visited_positions[position] = steps
		for move in moves:
			new_pos = (position[0] + move[0], position[1] + move[1])
			if 0 <= new_pos[0] < 71 and 0 <= new_pos[1] < 71 and map[new_pos[1]][new_pos[0]] != "#":
				heappush(heap, (steps + 1, new_pos))
	print(min_steps)
	return 0

if __name__ == '__main__':
	calculate_minimun_step_number()