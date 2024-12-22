#!/usr/bin/env python

from math import inf
from functools import cache

num_keypad = {
	'7': (0, 0), '8': (0, 1), '9': (0, 2),
	'4': (1, 0), '5': (1, 1), '6': (1, 2),
	'1': (2, 0), '2': (2, 1), '3': (2, 2),
				 '0': (3, 1), 'A': (3, 2)
}

dir_keypad = {
				 '^': (0, 1), 'A': (0, 2),
	'<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def get_char_sequences(current_pos, next_pos, sequences, keypad):
	y_dist = next_pos[0] - current_pos[0]
	x_dist = next_pos[1] - current_pos[1]
	sequence_x = ""
	sequence_y = ""
	if x_dist > 0:
		sequence_x += ">" * x_dist
	elif x_dist < 0:
		sequence_x += "<" * abs(x_dist)
	if y_dist > 0:
		sequence_y += "v" * y_dist
	elif y_dist < 0:
		sequence_y += "^" * abs(y_dist)
	if keypad == num_keypad:
		if current_pos[1] == 0 and next_pos[0] == 3:
			sequences.append(sequence_x + sequence_y + 'A')
		elif current_pos[0] == 3 and next_pos[1] == 0:
			sequences.append(sequence_y + sequence_x + 'A')
		else:
			sequences.append(sequence_x + sequence_y + 'A')
			sequences.append(sequence_y + sequence_x + 'A')
	elif keypad == dir_keypad:
		if current_pos == (1, 0) and next_pos[0] == 0:
			sequences.append(sequence_x + sequence_y + 'A')
		elif current_pos[0] == 0 and next_pos == (1, 0):
			sequences.append(sequence_y + sequence_x + 'A')
		else:
			sequences.append(sequence_x + sequence_y + 'A')
			sequences.append(sequence_y + sequence_x + 'A')
	return sequences

@cache
def get_first_sequences(code):
	sequences = list()
	current_pos = -1
	for char in code:
		if current_pos == -1:
			current_pos = num_keypad['A']
		next_pos = num_keypad[char]
		sequences = get_char_sequences(current_pos, next_pos, sequences)
		current_pos = next_pos
	return sequences

@cache
def calculate_complexity(sequence, level):
	complexity = 0
	keypad = dir_keypad
	for i in range(len(sequence)):
		if sequence[i].isdigit() or (i > 0 and sequence[i - 1].isdigit()):
			if i == 0:
				start = num_keypad['A']
			else:
				start = num_keypad[sequence[i - 1]]
			end = num_keypad[sequence[i]]
			keypad = num_keypad
		else:
			if i == 0:
				start = dir_keypad['A']
			else:
				start = dir_keypad[sequence[i - 1]]
			end = dir_keypad[sequence[i]]
			keypad = dir_keypad
		paths = get_char_sequences(start, end, [], keypad)
		if level == 0:
			if paths:
				lenght = min(len(path) for path in paths)
			else:
				lenght = 1
			complexity += lenght
			continue
		if not paths:
			complexity += 1
			continue
		lenghts = set()
		for path in paths:
			lenght = calculate_complexity(path, level - 1)
			lenghts.add(lenght)
		complexity += min(lenghts)
	return complexity

def get_complexity(code, part):
	number = int(code[:-1])
	if part == 1:
		complexity = calculate_complexity(code, 2)
	elif part == 2:
		complexity = calculate_complexity(code, 25)
	return number * complexity

def calculate_sum_of_complexity():
	codes = list()
	result1 = 0
	result2 = 0
	with open('input.txt') as f:
		lines = f.readlines()
		for line in lines:
			code = line.strip()
			codes.append(code)
	for code in codes:
		result1 += get_complexity(code, 1)
		result2 += get_complexity(code, 2)
	print("1st star: {}".format(result1))
	print("2nd star: {}".format(result2))
	return 0

if __name__ == '__main__':
	calculate_sum_of_complexity()