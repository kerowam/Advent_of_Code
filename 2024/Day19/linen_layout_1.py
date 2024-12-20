#!/usr/bin/env python

from sys import argv

def is_posible_design(avalible_towels, design, possible_designs):
	if len(design) == 0:
		return True
	if design in possible_designs:
		return True
	for i in range(0, len(design)):
		patchwork = design[:i + 1]
		if patchwork in avalible_towels:
			if is_posible_design(avalible_towels, design[i + 1:], possible_designs):
				possible_designs.append(design[i + 1:])
				return True
	return False


def count_ways_to_make_designs():
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
	possible_designs = list()
	for design in desired_designs:
		if is_posible_design(avalible_towels, design, possible_designs):
			possible_designs_counter += 1
	print(possible_designs_counter)
	return 0

if __name__ == '__main__':
	count_ways_to_make_designs()