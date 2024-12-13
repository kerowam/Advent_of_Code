#!/usr/bin/env python

import re

def mull_it_over():
	with open('./input.txt') as f:
		total = 0
		enable = True
		for line in f:
			line = line.strip()
			pattern = r'(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))'
			matches = re.findall(pattern, line)
			for match in matches:
				if 'do()' in match:
					enable = True
				elif 'don\'t()' in match:
					enable = False
				elif enable and 'mul' in match[0]:
					total += int(match[1]) * int(match[2])
	print(total)
	return 0

if __name__ == '__main__':
	mull_it_over()