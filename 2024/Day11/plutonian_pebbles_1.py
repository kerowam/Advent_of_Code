#!/usr/bin/env python

import copy

def blink_stones(stones):
	for i in range(25):
		blinked_stones = []
		for stone in stones:
			if stone == '0':
				blinked_stones.append('1')
			elif len(stone) % 2 == 0:
				first_half = stone[:len(stone) // 2]
				second_half = stone[len(stone) // 2:]
				blinked_stones.append(str(int(first_half)))
				blinked_stones.append(str(int(second_half)))
			else:
				blinked_stones.append(str(int(stone) * 2024))
		stones = copy.deepcopy(blinked_stones)
	print(stones)
	return stones


def count_stones():
	count = 0
	stones = []
	with open('input.txt') as f:
		line = f.readline().strip()
	stones = line.split(' ')
	print(stones)
	blinked_stones = blink_stones(stones)
	count = len(blinked_stones)
	print(count)
	return 0

if __name__ == '__main__':
	count_stones()