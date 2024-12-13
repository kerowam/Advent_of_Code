#!/usr/bin/env python

memory = {}

def blink_stones(stone, blink_count):
	if blink_count == 0:
		return 1
	elif (stone, blink_count) in memory:
		return memory[(stone, blink_count)]
	elif stone == 0:
		count = blink_stones(1, blink_count - 1)
	elif len(str(stone)) % 2 == 0:
		left_half = int(str(stone)[:len(str(stone)) // 2])
		right_half = int(str(stone)[len(str(stone)) // 2:])
		count = blink_stones(left_half, blink_count - 1) + blink_stones(right_half, blink_count - 1)
	else:
		count = blink_stones(stone * 2024, blink_count - 1)
	memory[(stone, blink_count)] = count
	return count


def count_stones():
	count = 0
	with open('input.txt') as f:
		line = f.readline().strip()
	stones = list(map(int, line.split(' ')))
	print(stones)
	for stone in stones:
		count += blink_stones(stone, 75)
	#print(len(memory))
	print(count)
	return 0

if __name__ == '__main__':
	count_stones()