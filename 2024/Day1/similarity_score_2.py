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

def calculate_similarity_score():
	group1, group2 = get_groups()
	result = 0
	for i in range(len(group1)):
		counter = group2.count(group1[i])
		result += int(group1[i]) * counter
	print(result)
	return 0

if __name__ == '__main__':
	calculate_similarity_score()