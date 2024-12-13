#!/usr/bin/env python

import copy

def get_sides_nbr(map_garden):
	sides_nbr = 0
	for x in range(len(map_garden)):
		for y in range(len(map_garden[x])):
			if map_garden[x][y] == '.':
				if y == 0 or (y > 0 and map_garden[x][y - 1] != '.'):
					if x == 0 or (x > 0 and map_garden[x - 1][y] != '.'):
						sides_nbr += 1
					if x == len(map_garden) - 1 or (x < len(map_garden) - 1 and map_garden[x + 1][y] != '.'):
						sides_nbr += 1
				elif (y > 0 and map_garden[x][y - 1] == '.'):
					if x > 0 and map_garden[x - 1][y - 1] == '.' and map_garden[x - 1][y] != '.':
						sides_nbr += 1
					if x < len(map_garden) - 1 and map_garden[x + 1][y - 1] == '.' and map_garden[x + 1][y] != '.':
						sides_nbr += 1
	for y in range(len(map_garden[0])):
		for x in range(len(map_garden)):
			if map_garden[x][y] == '.':
				if x == 0 or (x > 0 and map_garden[x - 1][y] != '.'):
					if y == 0 or (y > 0 and map_garden[x][y - 1] != '.'):
						sides_nbr += 1
					if y == len(map_garden[x]) - 1 or (y < len(map_garden[x]) - 1 and map_garden[x][y + 1] != '.'):
						sides_nbr += 1
				elif (x > 0 and map_garden[x - 1][y] == '.'):
					if y > 0 and map_garden[x - 1][y - 1] == '.' and map_garden[x][y - 1] != '.':
						sides_nbr += 1
					if y < len(map_garden[x]) - 1 and map_garden[x - 1][y + 1] == '.' and map_garden[x][y + 1] != '.':
						sides_nbr += 1
	return sides_nbr

def calculate_region_price(map_garden):
	count_plots = sum(row.count('.') for row in map_garden)
	sides_nbr = get_sides_nbr(map_garden)
	region_price = count_plots * sides_nbr
	return region_price

def flood_fill_region(map_garden, x, y, plant_type, coord_counted_plots):
	coord_counted_plots.add((x, y))
	map_garden[x][y] = '.'
	if y < len(map_garden[x]) - 1 and map_garden[x][y + 1] == plant_type and (x, y + 1) not in coord_counted_plots:
		map_garden = flood_fill_region(map_garden, x, y + 1, plant_type, coord_counted_plots)
	if x < len(map_garden) - 1 and map_garden[x + 1][y] == plant_type and (x + 1, y) not in coord_counted_plots:
		map_garden = flood_fill_region(map_garden, x + 1, y, plant_type, coord_counted_plots)
	if x > 0 and map_garden[x - 1][y] == plant_type and (x - 1, y) not in coord_counted_plots:
		map_garden = flood_fill_region(map_garden, x - 1, y, plant_type, coord_counted_plots)
	if y > 0 and map_garden[x][y - 1] == plant_type and (x, y - 1) not in coord_counted_plots:
		map_garden = flood_fill_region(map_garden, x, y - 1, plant_type, coord_counted_plots)
	return map_garden

def calculate_total_price(map_garden):
	coord_counted_plots = set()
	total_price = 0
	for x in range(len(map_garden)):
		for y in range(len(map_garden[x])):
			if (x, y) not in coord_counted_plots:
				coord_counted_plots.add((x, y))
				map_copy = copy.deepcopy(map_garden)
				map_flood_filled = flood_fill_region(map_copy, x, y, map_garden[x][y], coord_counted_plots)
				total_price += calculate_region_price(map_flood_filled)
	return total_price
				

def get_total_price():
	map_garden = []
	total_price = 0
	with open('input.txt') as f:
		for line in f:
			map_garden.append(list(line.strip()))
	#for line in map_garden:
	#	print(line)
	total_price = calculate_total_price(map_garden)
	print(total_price)
	return 0

if __name__ == '__main__':
	get_total_price()