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
	return 0

def possible_move(map, x_robot, y_robot, direction, box_positions, obstacles):
	#obstacles = 0
	if direction == '^':
		if map[x_robot - 1][y_robot] == '.' and map[x_robot - 1][y_robot + 1] == '.':
			return 0
		elif map[x_robot - 1][y_robot] == '[':
			box_positions.add((x_robot - 1, y_robot))
			obstacles += possible_move(map, x_robot - 1, y_robot, '^', box_positions, obstacles)
		elif map[x_robot - 1][y_robot] == ']' and map[x_robot - 1][y_robot + 1] != '#':
			box_positions.add((x_robot - 1, y_robot - 1))
			obstacles += possible_move(map, x_robot - 1, y_robot - 1, '^', box_positions, obstacles)
			if map[x_robot - 1][y_robot + 1] == '[':
				box_positions.add((x_robot - 1, y_robot + 1))
				obstacles += possible_move(map, x_robot - 1, y_robot + 1, '^', box_positions, obstacles)
		elif map[x_robot - 1][y_robot] == '.' and map[x_robot - 1][y_robot + 1] == '[':
			box_positions.add((x_robot - 1, y_robot + 1))
			obstacles += possible_move(map, x_robot - 1, y_robot + 1, '^', box_positions, obstacles)
		elif map[x_robot - 1][y_robot] == '#' or map[x_robot - 1][y_robot + 1] == '#':
			return 1
	elif direction == 'v':
		if map[x_robot + 1][y_robot] == '.' and map[x_robot + 1][y_robot + 1] == '.':
			return 0
		elif map[x_robot + 1][y_robot] == '[':
			box_positions.add((x_robot + 1, y_robot))
			obstacles += possible_move(map, x_robot + 1, y_robot, 'v', box_positions, obstacles)
		elif map[x_robot + 1][y_robot] == ']' and map[x_robot + 1][y_robot + 1] != '#':
			box_positions.add((x_robot + 1, y_robot - 1))
			obstacles += possible_move(map, x_robot + 1, y_robot - 1, 'v', box_positions, obstacles)
			if map[x_robot + 1][y_robot + 1] == '[':
				box_positions.add((x_robot + 1, y_robot + 1))
				obstacles += possible_move(map, x_robot + 1, y_robot + 1, 'v', box_positions, obstacles)
		elif map[x_robot + 1][y_robot] == '.' and map[x_robot + 1][y_robot + 1] == '[':
			box_positions.add((x_robot + 1, y_robot + 1))
			obstacles += possible_move(map, x_robot + 1, y_robot + 1, 'v', box_positions, obstacles)
		elif map[x_robot + 1][y_robot] == '#' or map[x_robot + 1][y_robot + 1] == '#':
			return 1
	return obstacles

def move(map, box_positions, direction):
	if direction == '^':
		for box in box_positions:
			map[box[0]][box[1]] = '.'
			map[box[0]][box[1] + 1] = '.'
		for box in box_positions:
			map[box[0] - 1][box[1]] = '['
			map[box[0] - 1][box[1] + 1] = ']'
	elif direction == 'v':
		for box in box_positions:
			map[box[0]][box[1]] = '.'
			map[box[0]][box[1] + 1] = '.'
		for box in box_positions:
			map[box[0] + 1][box[1]] = '['
			map[box[0] + 1][box[1] + 1] = ']'	
	return map

def robot_movement_predictor(map, instructions):
	x_robot, y_robot = get_robot_position(map)
	for instruction in instructions:
		if instruction == '>':
			if map[x_robot][y_robot + 1] != '#':
				if map[x_robot][y_robot + 1] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot][y_robot + 1] = '@'
					y_robot += 1
				elif map[x_robot][y_robot + 1] == '[':
					next_space = find_next_space(map, x_robot, y_robot, '>')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot][y_robot + 1] = '@'
						for y in range(y_robot + 2, next_space + 1, 2):
							map[x_robot][y] = '['
							map[x_robot][y + 1] = ']'
						y_robot += 1
		elif instruction == '<':
			if map[x_robot][y_robot - 1] != '#':
				if map[x_robot][y_robot - 1] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot][y_robot - 1] = '@'
					y_robot -= 1
				elif map[x_robot][y_robot - 1] == ']':
					next_space = find_next_space(map, x_robot, y_robot, '<')
					if next_space:
						map[x_robot][y_robot] = '.'
						map[x_robot][y_robot - 1] = '@'
						for y in range(y_robot - 2, next_space - 1, -2):
							map[x_robot][y] = ']'
							map[x_robot][y - 1] = '['
						y_robot -= 1
		elif instruction == '^':
			if map[x_robot - 1][y_robot] != '#':
				if map[x_robot - 1][y_robot] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot - 1][y_robot] = '@'
					x_robot -= 1
				elif map[x_robot - 1][y_robot] == '[' or map[x_robot - 1][y_robot] == ']':
					box_positions = set()
					obstacles = 0
					if map[x_robot - 1][y_robot] == '[':
						obstacles = possible_move(map, x_robot, y_robot, '^', box_positions, obstacles)
					elif map[x_robot - 1][y_robot] == ']':
						obstacles = possible_move(map, x_robot, y_robot - 1, '^', box_positions, obstacles)
					if obstacles == 0:
						map = move(map, box_positions, '^')
						map[x_robot][y_robot] = '.'
						map[x_robot - 1][y_robot] = '@'
						x_robot -= 1
		elif instruction == 'v':
			if map[x_robot + 1][y_robot] != '#':
				if map[x_robot + 1][y_robot] == '.':
					map[x_robot][y_robot] = '.'
					map[x_robot + 1][y_robot] = '@'
					x_robot += 1
				elif map[x_robot + 1][y_robot] == '[' or map[x_robot + 1][y_robot] == ']':
					box_positions = set()
					obstacles = 0
					if map[x_robot + 1][y_robot] == '[':
						obstacles = possible_move(map, x_robot, y_robot, 'v', box_positions, obstacles)
					elif map[x_robot + 1][y_robot] == ']':
						obstacles = possible_move(map, x_robot, y_robot - 1, 'v', box_positions, obstacles)
					if obstacles == 0:
						map = move(map, box_positions, 'v')
						map[x_robot][y_robot] = '.'
						map[x_robot + 1][y_robot] = '@'
						x_robot += 1
	return map

def get_gps_coordinates(map):
	total = 0
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] == '[':
				total += x * 100 + y
	return total

def scale_map(map):
	scaled_map = []
	for line in map:
		scaled_line = []
		for char in line:
			if char == '#':
				scaled_line.append('#')
				scaled_line.append('#')
			elif char == '.':
				scaled_line.append('.')
				scaled_line.append('.')
			elif char == '@':
				scaled_line.append('@')
				scaled_line.append('.')
			elif char == 'O':
				scaled_line.append('[')
				scaled_line.append(']')
		scaled_map.append(scaled_line)
	return scaled_map

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
	print(len(instructions))
	scaled_map = scale_map(map)
	print(len(scaled_map))
	print(len(scaled_map[0]))
	for line in scaled_map:
		for char in line:
			print(char, end='')
		print()
	print()
	final_map = robot_movement_predictor(scaled_map, instructions)
	#for line in final_map:
	#	for char in line:
	#		print(char, end='')
	#	print()
	total = get_gps_coordinates(final_map)
	print(total)
	return 0

if __name__ == '__main__':
	calculate_sum_gps_boxes()