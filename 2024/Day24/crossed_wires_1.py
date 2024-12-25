#!/usr/bin/env python

def check_z_gates_getted(gates, z_gates):
	for gate in z_gates:
		if gate not in gates:
			return False
	return True

def find_z_decimal_number():
	gates = dict()
	gates_and_wires = list()
	z_gates = list()
	with open('input.txt') as f:
		lines = f.readlines()
	for line in lines:
		if ":" in line:
			gate = line.strip().split(":")
			gates[gate[0]] = int(gate[1].strip())
		elif "->" in line:
			input = line.strip().split("->")
			gate = input[1].strip()
			if gate[0] == "z":
				z_gates.append(gate)
			wires = input[0].strip().split(" ")
			gates_and_wires.append((wires[0], wires[1], wires[2], gate))
	while not check_z_gates_getted(gates, z_gates):
		for gate in gates_and_wires:
			if gate[0] in gates and gate[2] in gates:
				if gate[1] == "AND":
					gates[gate[3]] = gates[gate[0]] & gates[gate[2]]
				elif gate[1] == "OR":
					gates[gate[3]] = gates[gate[0]] | gates[gate[2]]
				elif gate[1] == "XOR":
					gates[gate[3]] = gates[gate[0]] ^ gates[gate[2]]
	z_gates.sort(reverse=True)
	binary_result = ""
	for gate in z_gates:
		binary_result += str(gates[gate])
	#print(gates)
	#print(gates_and_wires)
	#print(z_gates)
	print(int(binary_result, 2))
	return 0

if __name__ == '__main__':
	find_z_decimal_number()