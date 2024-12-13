#!/usr/bin/env python

def get_possible_results(number, results):
	result_list = []
	for result in results[-1]:
		result_list.append(number + result)
		result_list.append(number * result)
		str_result = str(result) + str(number)
		result_list.append(int(str_result))
	return result_list

def possible_calibration(input):
	results = []
	str_result = str(input[1][0]) + str(input[1][1])
	results.append([input[1][0] + input[1][1], input[1][0] * input[1][1], int(str_result)])

	for i in range(2, len(input[1])):
		results.append(get_possible_results(input[1][i], results))
	if input[0] in results[-1]:
		return True

def total_calibration_result():
	calibration = 0
	inputs = []
	with open('input.txt') as f:
		for line in f:
			data = line.strip().split(':')
			numbers = list(map(int, data[1].strip().split(' ')))
			inputs.append((int(data[0]), numbers))
	for input in inputs:
		if possible_calibration(input):
			calibration += input[0]
	print(calibration)
	return 0

if __name__ == '__main__':
	total_calibration_result()