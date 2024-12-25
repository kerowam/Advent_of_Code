#!/usr/bin/env python

def find_wires_swaped():
	gates = dict()
	operations = list()
	nbr_z_gates = 0
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
				nbr_z_gates += 1
			wires = input[0].strip().split(" ")
			operations.append((wires[0], wires[1], wires[2], gate))
	max_z_gate = "z" + str(nbr_z_gates - 1)
	wrong_wires = set()
	for wire1, op, wire2, gate in operations:
		if gate[0] == 'z' and op != 'XOR' and gate != max_z_gate:
			wrong_wires.add(gate)
		if op == 'XOR' and wire1[0] not in ['x', 'y', 'z'] and wire2[0] not in ['x', 'y', 'z'] and gate[0] not in ['x', 'y', 'z']:
			wrong_wires.add(gate)
		if op == 'AND' and 'x00' not in [wire1, wire2] and 'x12' not in [wire1, wire2]:
			for wire3, op2, wire4, gate2 in operations:
				if (gate == wire3 or gate == wire4) and op2 != 'OR':
					wrong_wires.add(gate)
		if op == 'XOR':
			for wire3, op2, wire4, gate2 in operations:
				if (gate == wire3 or gate == wire4) and op2 == 'OR':
					wrong_wires.add(gate)
	print(",".join(sorted(wrong_wires)))

if __name__ == '__main__':
	find_wires_swaped()