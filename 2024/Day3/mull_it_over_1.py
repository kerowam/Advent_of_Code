#!/usr/bin/env python

import re

def mull_it_over():
	with open('./input.txt') as f:
		total = 0
		for line in f:
			line = line.strip()
			pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
			matches = re.findall(pattern, line)
			for match in matches:
				total += int(match[0]) * int(match[1])
	print(total)
	return 0

if __name__ == '__main__':
	mull_it_over()