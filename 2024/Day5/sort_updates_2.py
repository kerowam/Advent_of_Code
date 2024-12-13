#!/usr/bin/env python

def parse_input_file(file_path):
	rules = []
	updates = []
	with open(file_path, 'r') as f:
		lines = f.readlines()
	for line in lines:
		if "|" in line:
			rule = line.strip().split("|")
			rules.append((int(rule[0]), int(rule[1])))
		elif "," in line:
			updates.append(line.strip().split(","))
	updates = [[int(nbr) for nbr in update] for update in updates]
	return rules, updates

def check_update(rules, update):
	for rule in rules:
		if rule[0] in update and rule[1] in update \
		and update.index(rule[0]) > update.index(rule[1]):
			return False
	return True

def get_middle_number(update):
	middle = len(update) // 2
	return update[middle]

def sort_update(update, rules):
	for rule in rules:
		if rule[0] in update and rule[1] in update \
		and update.index(rule[0]) > update.index(rule[1]):
			update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
	while not check_update(rules, update):
		update = sort_update(update, rules)
	return update

def sort_updates():
	rules = []
	updates = []
	result = 0
	rules, updates = parse_input_file("input.txt")
	for update in updates:
		if not check_update(rules, update):
			update = sort_update(update, rules)
			result += get_middle_number(update)
	print(result)
	return 0

if __name__ == '__main__':
	sort_updates()