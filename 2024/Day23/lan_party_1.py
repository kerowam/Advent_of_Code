#!/usr/bin/env python

def find_t_connections():
	connections = dict()
	computers_list = list()
	with open('input.txt') as f:
		lines = f.readlines()
	for line in lines:
		computers = line.strip().split("-")
		if computers[0] not in connections:
			connections[computers[0]] = set()
			connections[computers[0]].add(computers[1])
			computers_list.append(computers[0])
		elif computers[0] in connections:
			connections[computers[0]].add(computers[1])
		if computers[1] not in connections:
			connections[computers[1]] = set()
			connections[computers[1]].add(computers[0])
			computers_list.append(computers[1])
		elif computers[1] in connections:
			connections[computers[1]].add(computers[0])
	computer_groups = set()
	for computer1 in computers_list:
		for computer2 in connections[computer1]:
			for computer3 in connections[computer1]:
				if computer3 != computer2 and computer3 in connections[computer2]:
					if computer1[0] == "t" or computer2[0] == "t" or computer3[0] == "t":
						computer_groups.add(frozenset([computer1, computer2, computer3]))
	print(len(computer_groups))
	return 0

if __name__ == '__main__':
	find_t_connections()