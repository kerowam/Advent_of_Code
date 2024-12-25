#!/usr/bin/env python


def get_pin(schema, k_or_l):
	pin = set()
	positions = [0, 0, 0, 0, 0]
	for line in schema[1:]:
		for i in range(len(line)):
			if k_or_l == "lock":
				if line[i] == "#":
					positions[i] += 1
			elif k_or_l == "key":
				if line[i] == ".":
					positions[i] += 1
	if k_or_l == "key":
		positions = [5 - x for x in positions]
	pin = tuple(positions)
	return pin


def count_lock_key_fit():
	keys = list()
	locks = list()
	input = list()
	with open('input.txt') as f:
		lines = f.readlines()
	for line in lines:
		input.append(line.strip())
	count = 0
	schema = list()
	k_or_l = ""
	for line in input:
		if line != "":
			schema.append(line.strip())
			count += 1
		if count == 7:
			count = 0
			k_or_l = "lock" if schema[0][0] == "#" else "key"
			pin = get_pin(schema, k_or_l)
			if k_or_l == "lock":
				locks.append(pin)
			elif k_or_l == "key":
				keys.append(pin)
			schema = list()
	fit_count = 0
	for lock in locks:
		for key in keys:
			for i in range(5):
				fit = True
				if lock[i] + key[i] > 5:
					fit = False
					break
			if fit:
				fit_count += 1
	print(fit_count)
	return 0

if __name__ == '__main__':
	count_lock_key_fit()