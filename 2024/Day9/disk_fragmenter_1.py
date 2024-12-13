#!/usr/bin/env python

def get_filesystem(line):
	filesystem = []
	id = -1
	for i in range(len(line)):
		nbr = int(line[i])
		if i % 2 == 0:
			id += 1
			for j in range(nbr):
				filesystem.append(id)
		else:
			for j in range(nbr):
				filesystem.append('.')
	return filesystem

def move_file_blocks(filesystem):
	for i in range(len(filesystem) -1, 0, -1):
		if filesystem[i] != '.':
			id = filesystem[i]
			j = 0
			while filesystem[j] != '.' and j < i:
				j += 1
			if filesystem[j] == '.' and j < i:
				filesystem[j] = id
				filesystem[i] = '.'
	return filesystem

def get_checksum(filesystem):
	result = 0
	i = 0
	while filesystem[i] != '.':
		result += filesystem[i] * i
		i += 1
	return result

def get_filesystem_checksum():
	checksum = 0
	filesystem = []
	with open('input.txt') as f:
		line = f.readline().strip()
		filesystem = get_filesystem(line)
	filesystem = move_file_blocks(filesystem)
	#print(filesystem)
	checksum = get_checksum(filesystem)
	print(checksum)
	return 0

if __name__ == '__main__':
	get_filesystem_checksum()