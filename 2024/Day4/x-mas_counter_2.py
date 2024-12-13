#!/usr/bin/env python

def xmas_counter():
	matrix = []
	counter = 0
	with open('./input.txt') as f:
		for line in f:
			matrix.append(line.strip())
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 'A':
				if i > 0 and i < len(matrix) - 1 and j > 0 and j < len(matrix[i]) - 1:
					if ((matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S') \
						or (matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M')) \
						and ((matrix[i - 1][j + 1] == 'M' and matrix[i + 1][j - 1] == 'S') \
						or (matrix[i - 1][j + 1] == 'S' and matrix[i + 1][j - 1] == 'M')):
							counter += 1
	print(counter)
	return 0

if __name__ == '__main__':
	xmas_counter()