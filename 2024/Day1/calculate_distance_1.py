#!/usr/bin/env python

def get_groups():
	group1 = []
	group2 = []
	with open('./input.txt') as f:
		for line in f:
			line = line.strip()
			groups = line.split('   ')
			group1.append(groups[0])
			group2.append(groups[1])
	print(group1)
	print(group2)
	return group1, group2

def calculate_distance():
	group1, group2 = get_groups()
	result = 0
	group1.sort()
	group2.sort()
	for i in range(len(group1)):
		distance = abs(int(group1[i]) - int(group2[i]))
		result += distance
	print(result)
	return 0

if __name__ == '__main__':
	calculate_distance()