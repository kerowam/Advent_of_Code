#!/usr/bin/env python

import re

def calculate_fewest_tokens_per_game(game):
	fewest_tokens = 0
	a = (game['Prize'][0] * game['Button B'][1] - game['Prize'][1] * game['Button B'][0]) / (game['Button A'][0] * game['Button B'][1] - game['Button A'][1] * game['Button B'][0])
	b = (game['Prize'][1] * game['Button A'][0] - game['Prize'][0] * game['Button A'][1]) / (game['Button A'][0] * game['Button B'][1] - game['Button A'][1] * game['Button B'][0])
	if a.is_integer() and b.is_integer():
		fewest_tokens = 3 * a + b
	return fewest_tokens

def calculate_fewest_tokens_needed():
	fewest_tokens_needed = 0
	with open('input.txt') as f:
		lines = f.readlines()
		game = {}
		for line in lines:
			if re.match(r'^Button A:.+', line):
				values = re.findall(r'\d+', line)
				game['Button A'] = (int(values[0]), int(values[1]))
			elif re.match(r'^Button B:.+', line):
				values = re.findall(r'\d+', line)
				game['Button B'] = (int(values[0]), int(values[1]))
			elif re.match(r'^Prize:.+', line):
				values = re.findall(r'\d+', line)
				game['Prize'] = (int(values[0]) + 10000000000000, int(values[1]) + 10000000000000)
			elif line == '\n':
				fewest_tokens_needed += calculate_fewest_tokens_per_game(game)
	print(int(fewest_tokens_needed))
	return 0

if __name__ == '__main__':
	calculate_fewest_tokens_needed()