#!/usr/bin/env python

def xmas_counter():
	matrix = []
	counter = 0
	with open('./input.txt') as f:
		for line in f:
			matrix.append(line.strip())
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 'X':
				if i > 2:
					if matrix[i - 1][j] == 'M' and matrix[i - 2][j] == 'A' and matrix[i - 3][j] == 'S':
						counter += 1
					if j > 2:
						if matrix[i - 1][j - 1] == 'M' and matrix[i - 2][j - 2] == 'A' and matrix[i - 3][j - 3] == 'S':
							counter += 1
					if j < len(matrix[i]) - 3:
						if matrix[i - 1][j + 1] == 'M' and matrix[i - 2][j + 2] == 'A' and matrix[i - 3][j + 3] == 'S':
							counter += 1
				if j > 2:
					if matrix[i][j - 1] == 'M' and matrix[i][j - 2] == 'A' and matrix[i][j - 3] == 'S':
						counter += 1
				if j < len(matrix[i]) - 3:
					if matrix[i][j + 1] == 'M' and matrix[i][j + 2] == 'A' and matrix[i][j + 3] == 'S':
						counter += 1
				if i < len(matrix) - 3:
					if j > 2:
						if matrix[i + 1][j - 1] == 'M' and matrix[i + 2][j - 2] == 'A' and matrix[i + 3][j - 3] == 'S':
							counter += 1
					if matrix[i + 1][j] == 'M' and matrix[i + 2][j] == 'A' and matrix[i + 3][j] == 'S':
						counter += 1
					if j < len(matrix[i]) - 3:
						if matrix[i + 1][j + 1] == 'M' and matrix[i + 2][j + 2] == 'A' and matrix[i + 3][j + 3] == 'S':
							counter += 1
	print(counter)
	return 0

if __name__ == '__main__':
	xmas_counter()