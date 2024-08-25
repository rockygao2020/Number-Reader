'''For Testing symbol.py; Check one-on-one reading symbols; Note some of this code is re-used in main.py in
   MainWindow.save_image() method to classify an input digit'''
import numpy as np
import numpy.linalg as npla

from symbol import Symbol, categorize_img, vectorize_img

'''============================== SET UP ALL 10 DIGITS WITH THEIR COMPLETED BASES =============================='''
zero = Symbol('0')
one = Symbol('1')
two = Symbol('2')
three = Symbol('3')
four = Symbol('4')
five = Symbol('5')
six = Symbol('6')
seven = Symbol('7')
eight = Symbol('8')
nine = Symbol('9')

test_size = 15
zero_path = 'tests\\0_cases'
one_path = 'tests\\1_cases'
two_path = 'tests\\2_cases'
three_path = 'tests\\3_cases'
four_path = 'tests\\4_cases'
five_path = 'tests\\5_cases'
six_path = 'tests\\6_cases'
seven_path = 'tests\\7_cases'
eight_path = 'tests\\8_cases'
nine_path = 'tests\\9_cases'

zero.readTestCases(test_size, zero_path)
one.readTestCases(test_size, one_path)
two.readTestCases(test_size, two_path)
three.readTestCases(test_size, three_path)
four.readTestCases(test_size, four_path)
five.readTestCases(test_size, five_path)
six.readTestCases(test_size, six_path)
seven.readTestCases(test_size, seven_path)
eight.readTestCases(test_size, eight_path)
nine.readTestCases(test_size, nine_path)



'''============================== TESTING (10 test cases per digit) =============================='''
digits = list(range(0,10))
cases = list(range(1,11))
symbol_list = [zero, one, two, three, four, five, six, seven, eight, nine]

for digit in digits:
	counter = 0
	fails = []
	print(f"TESTING DIGIT {digit}: ")
	for case in cases:
		image_path = f"input\\{digit}.{case}.png"
		closest_symbol, min_res, residuals = categorize_img(vectorize_img(image_path), symbol_list)
		if closest_symbol.getName() == str(digit):
			counter += 1
		else:
			fails.append(f"{digit}.{case}.png")
	print(f"\tSuccess Rate: {counter / 10}")
	print(f"\tFailed Cases: {fails}")


