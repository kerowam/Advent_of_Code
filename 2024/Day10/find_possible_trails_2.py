#!/usr/bin/env python

def get_trails_score(map, x, y, height_position):
	score = 0
	if x > 0 and map[x - 1][y] == str(height_position + 1):
		if height_position + 1 < 9:
			score += get_trails_score(map, x - 1, y, height_position + 1)
		else:
			score += 1
	if y > 0 and map[x][y - 1] == str(height_position + 1):
		if height_position + 1 < 9:
			score += get_trails_score(map, x, y - 1, height_position + 1)
		else:
			score += 1
	if x < len(map) - 1 and map[x + 1][y] == str(height_position + 1):
		if height_position + 1 < 9:
			score += get_trails_score(map, x + 1, y, height_position + 1)
		else:
			score += 1
	if y < len(map[x]) - 1 and map[x][y + 1] == str(height_position + 1):
		if height_position + 1 < 9:
			score += get_trails_score(map, x, y + 1, height_position + 1)
		else:
			score += 1
	return score

def get_sum_trailheads_scores():
	map = []
	sum_scores = 0
	with open('input.txt')as f:
		lines = f.readlines()
		for line in lines:
			map.append(line.strip())
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == '0':
				sum_scores += get_trails_score(map, i, j, 0)
	print(sum_scores)
	return 0

if __name__ == '__main__':
	get_sum_trailheads_scores()