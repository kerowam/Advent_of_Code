#!/usr/bin/env python

def get_plot_perimeter(map_garden, x, y, plant_type, perimeter):
	if y == len(map_garden[x]) - 1 or (y < len(map_garden[x]) - 1 and map_garden[x][y + 1] != plant_type):
		perimeter += 1
	if x == len(map_garden) - 1 or (x < len(map_garden) - 1 and map_garden[x + 1][y] != plant_type):
		perimeter += 1
	if x == 0 or (x > 0 and map_garden[x - 1][y] != plant_type):
		perimeter += 1
	if y == 0 or (y > 0 and map_garden[x][y - 1] != plant_type):
		perimeter += 1
	return perimeter

def get_plots_region_info(map_garden, x, y, plant_type, coord_counted_plots, perimeter, count_plots_region):
	perimeter = get_plot_perimeter(map_garden, x, y, plant_type, perimeter)
	if y < len(map_garden[x]) - 1 and map_garden[x][y + 1] == plant_type and (x, y + 1) not in coord_counted_plots:
		count_plots_region += 1
		coord_counted_plots.add((x, y + 1))
		count_plots_region, perimeter = get_plots_region_info(map_garden, x, y + 1, plant_type, coord_counted_plots, perimeter, count_plots_region)
	if x < len(map_garden) - 1 and map_garden[x + 1][y] == plant_type and (x + 1, y) not in coord_counted_plots:
		count_plots_region += 1
		coord_counted_plots.add((x + 1, y))
		count_plots_region, perimeter = get_plots_region_info(map_garden, x + 1, y, plant_type, coord_counted_plots, perimeter, count_plots_region)
	if x > 0 and map_garden[x - 1][y] == plant_type and (x - 1, y) not in coord_counted_plots:
		count_plots_region += 1
		coord_counted_plots.add((x - 1, y))
		count_plots_region, perimeter = get_plots_region_info(map_garden, x - 1, y, plant_type, coord_counted_plots, perimeter, count_plots_region)
	if y > 0 and map_garden[x][y - 1] == plant_type and (x, y - 1) not in coord_counted_plots:
		count_plots_region += 1
		coord_counted_plots.add((x, y - 1))
		count_plots_region, perimeter = get_plots_region_info(map_garden, x, y - 1, plant_type, coord_counted_plots, perimeter, count_plots_region)
	return count_plots_region, perimeter

def calculate_region_price(map_garden, x, y, coord_counted_plots):
	region_price = 0
	count_plots = 1
	perimeter = 0
	count_plots, perimeter = get_plots_region_info(map_garden, x, y, map_garden[x][y], coord_counted_plots, perimeter, count_plots)
	region_price = count_plots * perimeter
	return region_price

def calculate_total_price(map_garden):
	coord_counted_plots = set()
	total_price = 0
	for x in range(len(map_garden)):
		for y in range(len(map_garden[x])):
			if (x, y) not in coord_counted_plots:
				coord_counted_plots.add((x, y))
				total_price += calculate_region_price(map_garden, x, y, coord_counted_plots)
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