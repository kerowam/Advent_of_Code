#!/usr/bin/env python

import re

def find_second(robots_info):
	tree_found = False
	second = 1
	while not tree_found:
		robots_positions = set()
		repeated_position = False
		for robot in robots_info:
			if not repeated_position:
				x = int(robot[0])
				y = int(robot[1])
				vx = int(robot[2])
				vy = int(robot[3])
				end_x = (x + second * vx) % 101
				end_y = (y + second * vy) % 103
				if end_x < 0:
					end_x = 101 + end_x
				if end_y < 0:
					end_y = 103 + end_y
				if (end_x, end_y) in robots_positions:
					repeated_position = True
				else:
					robots_positions.add((end_x, end_y))
		if not repeated_position:
			return second
		second += 1
	return 0

def calculate_safety_factor():
	robots_info = []
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			match = re.search(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
			robots_info.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
	second = find_second(robots_info)
	print(second)
	return 0

if __name__ == '__main__':
	calculate_safety_factor()