#!/usr/bin/env python

def get_position_guard(map):
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == '^' or map[x][y] == 'v' or map[x][y] == '<' or map[x][y] == '>':
				return x, y, map[x][y]
	return -1, -1

def count_positions_visited_by_guard():
	map = []
	visited_positions = set()
	with open('input.txt') as f:
		for line in f:
			map.append(line.strip())
	x, y, direction = get_position_guard(map)
	visited_positions.add((x, y))
	count = 1
	guard_in_map = True
	while guard_in_map:
		if direction == '^':
			if x == 0:
				guard_in_map = False
				break
			elif map[x - 1][y] != '#':
				x -= 1
			else:
				direction = '>'
		elif direction == '>':
			if y == len(map[x]) - 1:
				guard_in_map = False
				break
			elif map[x][y + 1] != '#':
				y += 1
			else:
				direction = 'v'
		elif direction == 'v':
			if x == len(map) - 1:
				guard_in_map = False
				break
			elif map[x + 1][y] != '#':
				x += 1
			else:
				direction = '<'
		elif direction == '<':
			if y == 0:
				guard_in_map = False
				break
			elif map[x][y - 1] != '#':
				y -= 1
			else:
				direction = '^'
		if (x, y) not in visited_positions:
			visited_positions.add((x, y))
			count += 1
	print(count)
	#for i in range(len(map)):
	#	print(map[i])
	return 0

if __name__ == '__main__':
	count_positions_visited_by_guard()