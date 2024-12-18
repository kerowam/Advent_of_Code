#!/usr/bin/env python

import sys
import re

def adv(registers, operand):
	registers["A"] = registers["A"] // 2 ** operand
	return 0

def bxl(registers, operand):
	registers["B"] = registers["B"] ^ operand
	return 0

def bst(registers, operand):
	registers["B"] = operand % 8
	return 0

def jnz(registers, operand, i):
	if registers["A"] == 0:
		return i + 2
	return operand

def bxc(registers):
	registers["B"] = registers["B"] ^ registers["C"]
	return 0

def out(operand, output):
	if output == "":
		output = str(operand % 8)
	else:
		output += "," + str(operand % 8)
	return output

def bdv(registers, operand):
	registers["B"] = registers["A"] // 2 ** operand
	return 0

def cdv(registers, operand):
	registers["C"] = registers["A"] // 2 ** operand
	return 0

def run_program(registers, program):
	i = 0
	output = ""
	while i < len(program):
		combo_operand = [0, 1, 2, 3, registers["A"], registers["B"], registers["C"], None]
		opcode = program[i]
		operand = int(program[i + 1])
		combo_op = combo_operand[operand]
		if opcode == "0":
			adv(registers, combo_op)
		elif opcode == "1":
			bxl(registers, operand)
		elif opcode == "2":
			bst(registers, combo_op)
		elif opcode == "3":
			i = jnz(registers, operand, i)
		elif opcode == "4":
			bxc(registers)
		elif opcode == "5":
			output = out(combo_op, output)
		elif opcode == "6":
			bdv(registers, combo_op)
		elif opcode == "7":
			cdv(registers, combo_op)
		if opcode != "3":
			i += 2
	print(registers)
	return output

def get_output():
	registers = dict()
	program = []
	with open(sys.argv[1]) as f:
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
	output = run_program(registers, program)
	print(output)
	return 0

if __name__ == '__main__':
	get_output()