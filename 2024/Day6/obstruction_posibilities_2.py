#!/usr/bin/env python

import copy

def get_initial_position_guard(map):
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == '^' or map[x][y] == 'v' or map[x][y] == '<' or map[x][y] == '>':
				return x, y, map[x][y]
	return -1, -1

def check_obstruction(map, x, y, direction):
	visited_positions = set()
	while (x, y, direction) not in visited_positions:
		visited_positions.add((x, y, direction))
		if direction == '^':
			if x == 0:
				return False
			elif map[x - 1][y] != '#':
				x -= 1
			else:
				direction = '>'
		elif direction == '>':
			if y == len(map[x]) - 1:
				return False
			elif map[x][y + 1] != '#':
				y += 1
			else:
				direction = 'v'
		elif direction == 'v':
			if x == len(map) - 1:
				return False
			elif map[x + 1][y] != '#':
				x += 1
			else:
				direction = '<'
		elif direction == '<':
			if y == 0:
				return False
			elif map[x][y - 1] != '#':
				y -= 1
			else:
				direction = '^'
	return True

def count_obstruction_posibilities():
	map = []
	with open('test.txt') as f:
		for line in f:
			map.append(line.strip())
	x0, y0, direction = get_initial_position_guard(map)
	count = 0
	for x in range(len(map)):
		for y in range(len(map[x])):
			test_map = copy.deepcopy(map)
			if map[x][y] != '#' and not (x == x0 and y == y0):
				test_map[x] = test_map[x][:y] + '#' + test_map[x][y + 1:]
				#for i in range(len(test_map)):
				#	print(test_map[i])
				#print()
				if check_obstruction(test_map, x0, y0, direction):
					count += 1
	print(count)
	return 0

if __name__ == '__main__':
	count_obstruction_posibilities()