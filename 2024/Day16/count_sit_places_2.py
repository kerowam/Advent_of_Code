#!/usr/bin/env python

from heapq import heappop, heappush
from math import inf
import re

def calculate_score_cheapest_path():
	with open('input.txt') as f:
		lines = [line.strip() for line in f]
	x_len = len(lines[0])
	map = list("".join(lines))
	start, end = (map.index("S"), map.index("E"))
	moves = [-x_len, 1, x_len, -1]
	visited_positions = dict()
	min_score = inf
	heap = list()
	paths = list()

	heappush(heap, (0, start, 1, ""))
	while heap:
		score, pos, dir, path = heappop(heap)
		if score > min_score:
			break
		if (pos, dir) in visited_positions and score > visited_positions[(pos, dir)]:
			continue
		visited_positions[(pos, dir)] = score
		if pos == end:
			min_score = score
			paths.append(path)
		if map[pos + moves[dir]] != "#":
			heappush(heap, (score + 1, pos + moves[dir], dir, path + "^"))
		heappush(heap, (score + 1000, pos, (dir + 1) % 4, path + ">"))
		heappush(heap, (score + 1000, pos, (dir - 1) % 4, path + "<"))
	
	paths_positions = set()
	paths_positions.add(start)
	for path in paths:
		current_pos = start
		dir = 1
		for move in path:
			if move == "^":
				current_pos += moves[dir]
				paths_positions.add(current_pos)
			elif move == ">":
				dir = (dir + 1) % 4
			elif move == "<":
				dir = (dir - 1) % 4
	print(min_score)
	print(len(paths_positions))
	return 0

if __name__ == '__main__':
	calculate_score_cheapest_path()