#!/usr/bin/env python

import re

def get_quadrant(line):
	match = re.search(r'^p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
	x = int(match.group(1))
	y = int(match.group(2))
	vx = int(match.group(3))
	vy = int(match.group(4))
	end_x = (x + 100 * vx) % 101
	end_y = (y + 100 * vy) % 103
	if end_x < 0:
		end_x = 101 + end_x
	if end_y < 0:
		end_y = 103 + end_y
	if end_x < 50 and end_y < 51:
		return 1
	elif end_x > 50 and end_y < 51:
		return 2
	elif end_x < 50 and end_y > 51:
		return 3
	elif end_x > 50 and end_y > 51:
		return 4
	else:
		return 0

def calculate_safety_factor():
	quadrant_robot_counter_1 = 0
	quadrant_robot_counter_2 = 0
	quadrant_robot_counter_3 = 0
	quadrant_robot_counter_4 = 0
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			quadrant = get_quadrant(line)
			if quadrant == 1:
				quadrant_robot_counter_1 += 1
			elif quadrant == 2:
				quadrant_robot_counter_2 += 1
			elif quadrant == 3:
				quadrant_robot_counter_3 += 1
			elif quadrant == 4:
				quadrant_robot_counter_4 += 1
	#print(quadrant_robot_counter_1)
	#print(quadrant_robot_counter_2)
	#print(quadrant_robot_counter_3)
	#print(quadrant_robot_counter_4)
	safety_factor = quadrant_robot_counter_1 * quadrant_robot_counter_2 * quadrant_robot_counter_3 * quadrant_robot_counter_4
	print(safety_factor)
	return 0

if __name__ == '__main__':
	calculate_safety_factor()