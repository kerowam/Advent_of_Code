#!/usr/bin/env python

def get_robot_position(map):
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == '@':
				return (x, y)

def find_next_space(map, x_robot, y_robot, direction):
	if direction == '>':
		for y in range(y_robot + 1, len(map[x_robot]) - 1):
			if map[x_robot][y] == '.':
				return y
			elif map[x_robot][y] == '#':
				return 0
	elif direction == '<':
		for y in range(y_robot - 1, 0, -1):
			if map[x_robot][y] == '.':
				return y
			elif map[x_robot][y] == '#':
				return 0
	elif direction == '^':
		for x in range(x_robot - 1, 0, -1):
			if map[x][y_robot] == '.':
				return x
			elif map[x][y_robot] == '#':
				return 0
	elif direction == 'v':
		for x in range(x_robot + 1, len(map) - 1):
			if map[x][y_robot] == '.':
				return x
			elif map[x][y_robot] == '#':
				return 0
	return 0

def robot_movement_predictor(map, instructions):
	x_robot, y_robot = get_robot_position(map)
	for instruction in instructions:
		if instruction == '>':
			if map[x_robot][y_robot + 1] != '#':
				if map[x_robot][y_robot + 1] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot][y_robot + 1] = '@'
					y_robot += 1
				elif map[x_robot][y_robot + 1] == 'O':
					next_space = find_next_space(map, x_robot, y_robot, '>')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot][y_robot + 1] = '@'
						map[x_robot][next_space] = 'O'
						y_robot += 1
		elif instruction == '<':
			if map[x_robot][y_robot - 1] != '#':
				if map[x_robot][y_robot - 1] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot][y_robot - 1] = '@'
					y_robot -= 1
				elif map[x_robot][y_robot - 1] == 'O':
					next_space = find_next_space(map, x_robot, y_robot, '<')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot][y_robot - 1] = '@'
						map[x_robot][next_space] = 'O'
						y_robot -= 1
		elif instruction == '^':
			if map[x_robot - 1][y_robot] != '#':
				if map[x_robot - 1][y_robot] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot - 1][y_robot] = '@'
					x_robot -= 1
				elif map[x_robot - 1][y_robot] == 'O':
					next_space = find_next_space(map, x_robot, y_robot, '^')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot - 1][y_robot] = '@'
						map[next_space][y_robot] = 'O'
						x_robot -= 1
		elif instruction == 'v':
			if map[x_robot + 1][y_robot] != '#':
				if map[x_robot + 1][y_robot] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot + 1][y_robot] = '@'
					x_robot += 1
				elif map[x_robot + 1][y_robot] == 'O':
					next_space = find_next_space(map, x_robot, y_robot, 'v')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot + 1][y_robot] = '@'
						map[next_space][y_robot] = 'O'
						x_robot += 1
	return map

def get_gps_coordinates(map):
	total = 0
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == 'O':
				total += x * 100 + y
	return total

def calculate_sum_gps_boxes():
	total = 0
	map = []
	instructions = ''
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			if line[0] == '#':
				map.append(list(line.strip()))
			elif line[0] == '\n':
				continue
			else:
				instructions += line.strip()
	final_map = robot_movement_predictor(map, instructions)
	total = get_gps_coordinates(final_map)
	print(total)
	return 0

if __name__ == '__main__':
	calculate_sum_gps_boxes()