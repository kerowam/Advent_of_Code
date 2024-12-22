#!/usr/bin/env python

def calculate_secret_number(number, limit, total_changes):
	secret_number = number
	last_number = number % 10
	sequence = list()
	changes = set()
	for i in range(limit):
		mix_number = secret_number * 64
		secret_number = secret_number ^ mix_number
		if secret_number >= 16777216:
			secret_number = secret_number % 16777216
		mix_number = secret_number // 32
		secret_number = secret_number ^ mix_number
		if secret_number >= 16777216:
			secret_number = secret_number % 16777216
		mix_number = secret_number * 2048
		secret_number = secret_number ^ mix_number
		if secret_number >= 16777216:
			secret_number = secret_number % 16777216
		current_number = secret_number % 10
		if len(sequence) < 4:
			sequence.append(current_number - last_number)
		else:
			sequence.pop(0)
			sequence.append(current_number - last_number)
		if len(sequence) == 4 and tuple(sequence) not in changes:
			changes.add(tuple(sequence))
			if tuple(sequence) not in total_changes:
				total_changes[tuple(sequence)] = current_number
			else:
				total_changes[tuple(sequence)] += current_number
		last_number = current_number
	return total_changes

def sum_secret_numbers():
	bananas = 0
	total_changes = dict()
	with open('input.txt') as f:
		lines = f.readlines()
	firsts_numbers = list()
	for line in lines:
		firsts_numbers.append(int(line))
	for number in firsts_numbers:
		total_changes = calculate_secret_number(number, 2000, total_changes)
	bananas = max(total_changes.values())
	print(bananas)
	return 0

if __name__ == '__main__':
	sum_secret_numbers()