from math import cosh
import numpy

def equation(a, b, x):
	y = a * cosh(x / a) + b * (x ** 2) - a
	return y

coordinates = []

with open('coordinates.txt', 'r') as f:
	for line in f.read().split('\n'):
		clean_coord = line.split('(')[1][:-1]
		x = float(clean_coord.split(',')[0])
		y = float(clean_coord.split(',')[1])
		coordinates.append([x, y])

min_y_dif = 1000
min_constants = []
break_bool = True

for b in numpy.arange(0.001, 1, 0.001):
	a_start = round(1 / b, 3) + 0.001
	a_end = a_start + 1000

	for a in numpy.arange(a_start, a_end, 0.001):
		y_dif_list = []

		for i in coordinates:
			y_cal = equation(a, b, i[0])
			y_val = i[1]
			y_abs = abs(y_cal - y_val)
			y_dif_list.append(y_abs)

		y_dif_avg = sum(y_dif_list) / len(y_dif_list)

		if y_dif_avg <= min_y_dif:
			break_bool = False
			min_y_dif = y_dif_avg
			min_constants = [a, b]
		else:
			break
			

	if break_bool:
		break

print min_constants[0]
print min_constants[1]
