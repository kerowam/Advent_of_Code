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
	return filesystem, id

def move_file_blocks(filesystem, last_id):
	i = len(filesystem) - 1
	current_id = last_id
	while i > 0 and current_id > 0:
		if filesystem[i] != '.' and filesystem[i] == current_id:
			count = 1
			while filesystem[i - count] == current_id:
				count += 1
			for j in range(len(filesystem)):
				if filesystem[j] == '.' and j < i:
					count_space = 1
					while filesystem[j + count_space] == '.' and count_space < count and j + count_space < i:
						count_space += 1
					if count_space == count and j + count_space <= i:
						for k in range(count):
							filesystem[j + k] = current_id
						for k in range(count):
							filesystem[i - k] = '.'
						break
			current_id -= 1
		i -= 1
	return filesystem

def get_checksum(filesystem):
	result = 0
	for i in range(len(filesystem)):
		if filesystem[i] != '.':
			result += filesystem[i] * i
	return result

def get_filesystem_checksum():
	checksum = 0
	filesystem = []
	last_id = 0
	with open('input.txt') as f:
		line = f.readline().strip()
		filesystem, last_id = get_filesystem(line)
	filesystem = move_file_blocks(filesystem, last_id)
	#print(filesystem)
	checksum = get_checksum(filesystem)
	print(checksum)
	return 0

if __name__ == '__main__':
	get_filesystem_checksum()