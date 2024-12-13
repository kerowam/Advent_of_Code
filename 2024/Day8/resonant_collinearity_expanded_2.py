#!/usr/bin/env python

def add_antinode_location(map, x, y, antinodes_locations):
	frecuency = map[x][y]
	antinodes_locations.add((x, y))
	for y1 in range(y + 1, len(map[x])):
		if map[x][y1] == frecuency:
			antinode_dist_y = (y1 - y)
			i = 1
			while y - antinode_dist_y * i >= 0:
				if (x, y - antinode_dist_y * i) not in antinodes_locations:
					antinodes_locations.add((x, y - antinode_dist_y * i))
				i += 1
			i = 1
			while y1 + antinode_dist_y * i < len(map[x]):
				if (x, y1 + antinode_dist_y * i) not in antinodes_locations:
					antinodes_locations.add((x, y1 + antinode_dist_y * i))
				i += 1
	for x1 in range(x + 1, len(map)):
		for y1 in range(len(map[x1])):
			if map[x1][y1] == frecuency:
				antinode_dist_x = (x1 - x)
				antinode_dist_y = (y1 - y)
				i = 1
				while x - antinode_dist_x * i >= 0 and y - antinode_dist_y * i >= 0 and y - antinode_dist_y * i < len(map[x]):
					if (x - antinode_dist_x * i, y - antinode_dist_y * i) not in antinodes_locations:
						antinodes_locations.add((x - antinode_dist_x * i, y - antinode_dist_y * i))
					i += 1
				i = 1
				while x + antinode_dist_x * i < len(map) and y + antinode_dist_y * i < len(map[x]) and y + antinode_dist_y * i >= 0:
					if (x + antinode_dist_x * i, y + antinode_dist_y * i) not in antinodes_locations:
						antinodes_locations.add((x + antinode_dist_x * i, y + antinode_dist_y * i))
					i += 1
				i = 1
	return 0


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