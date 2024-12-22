#!/usr/bin/env python

def calculate_secret_number(number, limit):
	secret_number = number
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
	return secret_number

def sum_secret_numbers():
	sum = 0
	with open('input.txt') as f:
		lines = f.readlines()
	firsts_numbers = list()
	for line in lines:
		firsts_numbers.append(int(line))
	for number in firsts_numbers:
		sum += calculate_secret_number(number, 2000)
	#print(firsts_numbers)
	print(sum)
	return 0

if __name__ == '__main__':
	sum_secret_numbers()