#!/usr/bin/env python

def get_trails(map, x, y, visited_positions, height_position):
	if x > 0 and map[x - 1][y] == str(height_position + 1):
		if height_position + 1 < 9:
			get_trails(map, x - 1, y, visited_positions, height_position + 1)
		else:
			if (x - 1, y) not in visited_positions:
				visited_positions.add((x - 1, y))
	if y > 0 and map[x][y - 1] == str(height_position + 1):
		if height_position + 1 < 9:
			get_trails(map, x, y - 1, visited_positions, height_position + 1)
		else:
			if (x, y - 1) not in visited_positions:
				visited_positions.add((x, y - 1))
	if x < len(map) - 1 and map[x + 1][y] == str(height_position + 1):
		if height_position + 1 < 9:
			get_trails(map, x + 1, y, visited_positions, height_position + 1)
		else:
			if (x + 1, y) not in visited_positions:
				visited_positions.add((x + 1, y))
	if y < len(map[x]) - 1 and map[x][y + 1] == str(height_position + 1):
		if height_position + 1 < 9:
			get_trails(map, x, y + 1, visited_positions, height_position + 1)
		else:
			if (x, y + 1) not in visited_positions:
				visited_positions.add((x, y + 1))
	return 0

def get_trailhead_score(map, x, y, height_position):
	visited_positions = set()
	get_trails(map, x, y, visited_positions, height_position)
	score = len(visited_positions)
	return score

def get_sum_trailheads_scores():
	map = []
	sum_scores = 0
	with open('input.txt')as f:
		lines = f.readlines()
		for line in lines:
			map.append(line.strip())
	#for i in range(len(map)):
	#	print(map[i])
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == '0':
				sum_scores += get_trailhead_score(map, i, j, 0)
	print(sum_scores)
	return 0

if __name__ == '__main__':
	get_sum_trailheads_scores()