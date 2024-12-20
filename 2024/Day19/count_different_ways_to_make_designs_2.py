#!/usr/bin/env python

from sys import argv

def is_posible_design(avalible_towels, design, possible_designs):
	if len(design) == 0:
		return 1
	if design in possible_designs:
		return possible_designs[design]
	count_ways = 0
	for i in range(0, len(design)):
		patchwork = design[:i + 1]
		if patchwork in avalible_towels:
			count_ways += is_posible_design(avalible_towels, design[i + 1:], possible_designs)
	possible_designs[design] = count_ways
	return count_ways


def count_possible_designs():
	avalible_towels = list()
	desired_designs = list()
	with open(argv[1]) as f:
		lines = f.readlines()
		for line in lines:
			if "," in line:
				towels = line.strip().split(", ")
				for towel in towels:
					avalible_towels.append(towel)
			elif line.strip() != "":
				desired_designs.append(line.strip())
	possible_designs_counter = 0
	possible_designs = dict()
	for design in desired_designs:
		possible_designs_counter += is_posible_design(avalible_towels, design, possible_designs)
	print(possible_designs_counter)
	return 0

if __name__ == '__main__':
	count_possible_designs()