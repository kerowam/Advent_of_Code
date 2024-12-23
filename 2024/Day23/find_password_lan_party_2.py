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
	max_computer_group = set()
	checked_computers = set()
	for computer1 in computers_list:
		computers_connected = set()
		for computer2 in connections[computer1]:
			if computer2 not in checked_computers:
				computer_subgroup = list()
				computer_subgroup.append(computer2)
				for computer3 in connections[computer1]:
					if computer3 != computer2 and computer3 not in checked_computers:
						all_connected = True
						for computer4 in computer_subgroup:
							if computer3 not in connections[computer4]:
								all_connected = False
								break
						if all_connected:
							computer_subgroup.append(computer3)
				computer_subgroup.append(computer1)
				if len(computer_subgroup) > len(computers_connected):
					computers_connected = set(computer_subgroup)
		if max_computer_group == set() or len(computers_connected) > len(max_computer_group):
			max_computer_group = set(computers_connected)
		checked_computers.add(computer1)
	result = list(max_computer_group)
	result.sort()
	solution = ""
	for computer in result:
		solution += computer + ","
	print(solution[:-1])
	return 0

if __name__ == '__main__':
	find_t_connections()