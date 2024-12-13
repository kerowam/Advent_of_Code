#!/usr/bin/env python

import re

def calculate_cheapest_button(game):
	cheapest_button = ''
	x_A = game['Prize'][0] // game['Button A'][0]
	y_A = game['Prize'][1] // game['Button A'][1]
	x_B = game['Prize'][0] // game['Button B'][0]
	y_B = game['Prize'][1] // game['Button B'][1]
	if min(x_A, y_A) < 3 * min(x_B, y_B):
		cheapest_button = 'Button A'
		value = min(x_A, y_A)
	else:
		cheapest_button = 'Button B'
		value = min(x_B, y_B)
	if value > 100:
		value = 100
	return cheapest_button, value

def calculate_fewest_tokens_per_game(game):
	fewest_tokens = 0
	cheapest_button, value = calculate_cheapest_button(game)
	if cheapest_button == 'Button A':
		other_button = 'Button B'
	elif cheapest_button == 'Button B':
		other_button = 'Button A'

	for i in range(value, 0, -1):
		if game[cheapest_button][0] * i == game['Prize'][0] and game[cheapest_button][1] * i == game['Prize'][1]:
			if cheapest_button == 'Button A':
				fewest_tokens = i * 3
			else:
				fewest_tokens = i
			break
		elif game[other_button][0] * i == game['Prize'][0] and game[other_button][1] * i == game['Prize'][1]:
			if cheapest_button == 'Button A':
				fewest_tokens = i
			else:
				fewest_tokens = i * 3
			break
		elif game[cheapest_button][0] * i < game['Prize'][0] and game[cheapest_button][1] * i < game['Prize'][1]:
			for j in range(1, 101):
				if game[other_button][0] * j + game[cheapest_button][0] * i == game['Prize'][0] and game[other_button][1] * j + game[cheapest_button][1] * i == game['Prize'][1]:
					if cheapest_button == 'Button A':
						game_tokens = i * 3 + j
					else:
						game_tokens = i + j * 3
					if fewest_tokens == 0 or game_tokens < fewest_tokens:
						fewest_tokens = game_tokens
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
				game['Prize'] = (int(values[0]), int(values[1]))
			elif line == '\n':
				fewest_tokens_needed += calculate_fewest_tokens_per_game(game)
	print(fewest_tokens_needed)
	return 0

if __name__ == '__main__':
	calculate_fewest_tokens_needed()