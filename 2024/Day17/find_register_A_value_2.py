#!/usr/bin/env python

import re

def calculate_register_A_value(registers, program):
	possible_A_values = []
	for i in range(8):
		registers["A"] = i
		registers["B"] = registers["A"] % 8
		registers["B"] = registers["B"] ^ 5
		registers["C"] = registers["A"] // 2**registers["B"]
		registers["B"] = registers["B"] ^ 6
		registers["B"] = registers["B"] ^ registers["C"]
		if registers["B"] % 8 == 0:
			possible_A_values.append(i)
	for i in range(1, 16):
		round_A_values = []
		for value in possible_A_values:
			registers["A"] = value
			for j in range(8):
				registers["B"] = j
				registers["B"] = registers["B"] ^ 5
				registers["C"] = (registers["A"] * 8 + j) // 2**registers["B"]
				registers["B"] = registers["B"] ^ 6
				registers["B"] = registers["B"] ^ registers["C"]
				if registers["B"] % 8 == int(program[i]):
					round_A_values.append(registers["A"] * 8 + j)
		possible_A_values = round_A_values
	return possible_A_values

def find_register_A_value():
	registers = dict()
	program = []
	with open("input.txt") as f:
		lines = f.readlines()
		for line in lines:
			match = re.search(r'(Register A:|Register B:|Register C:|Program:) (.*)', line)
			if match:
				if match.group(1) == "Register A:":
					registers["A"] = int(match.group(2))
				elif match.group(1) == "Register B:":
					registers["B"] = int(match.group(2))
				elif match.group(1) == "Register C:":
					registers["C"] = int(match.group(2))
				elif match.group(1) == "Program:":
					instructions = match.group(2).split(',')
					for instruction in instructions:
						program.append(instruction)
	inverted_program = program[::-1]
	a_values = calculate_register_A_value(registers, inverted_program)
	print(a_values)
	return 0

if __name__ == '__main__':
	find_register_A_value()