#!/usr/bin/env python

def safe_report(line):
	char_report = line.split()
	report = [int (x) for x in char_report]
	increase = True
	safe = True
	if report[0] > report[1]:
		increase = False
	for i in range(0, len(report) - 1):
		if increase:
			if report[i] > report[i + 1] or report[i] == report[i + 1] or report[i + 1] - report[i] > 3:
				safe = False
				break
		else:
			if report[i] < report[i + 1] or report[i] == report[i + 1] or report[i] - report[i + 1] > 3:
				safe = False
				break
	return safe

def count_safe_reports():
	safe_count = 0
	with open('./input.txt') as f:
		for line in f:
			line = line.strip()
			if safe_report(line):
				safe_count += 1
	print(safe_count)
	return 0

if __name__ == '__main__':
	count_safe_reports()