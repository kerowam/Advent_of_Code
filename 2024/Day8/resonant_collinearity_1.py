#!/usr/bin/env python

def add_antinode_location(map, x, y, antinodes_locations):
	frecuency = map[x][y]
	for y1 in range(y + 1, len(map[x])):
		if map[x][y1] == frecuency:
			antinode_dist_y = (y1 - y)
			if y - antinode_dist_y >= 0:
				if (x, y - antinode_dist_y) not in antinodes_locations:
					antinodes_locations.add((x, y - antinode_dist_y))
			if y1 + antinode_dist_y < len(map[x]):
				if (x, y1 + antinode_dist_y) not in antinodes_locations:
					antinodes_locations.add((x, y1 + antinode_dist_y))
	for x1 in range(x + 1, len(map)):
		for y1 in range(len(map[x1])):
			if map[x1][y1] == frecuency:
				antinode_dist_x = (x1 - x)
				antinode_dist_y = (y1 - y)
				if x - antinode_dist_x >= 0:
					if y - antinode_dist_y >= 0 and y - antinode_dist_y < len(map[x]):
						if (x - antinode_dist_x, y - antinode_dist_y) not in antinodes_locations:
							antinodes_locations.add((x - antinode_dist_x, y - antinode_dist_y))
					
				if x1 + antinode_dist_x < len(map):
					if y1 + antinode_dist_y < len(map[x1]) and y1 + antinode_dist_y >= 0:
						if (x1 + antinode_dist_x, y1 + antinode_dist_y) not in antinodes_locations:
							antinodes_locations.add((x1 + antinode_dist_x, y1 + antinode_dist_y))
					


def count_resonant_collinearities():
	map = []
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			map.append(line.strip())
	antinodes_locations = set()
	for x in range(len(map)):
		for y in range(len(map[x])):
			if map[x][y] != '.':
				add_antinode_location(map, x, y, antinodes_locations)
	print(len(antinodes_locations))
	return 0

if __name__ == '__main__':
	count_resonant_collinearities()