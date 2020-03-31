#!/usr/bin/python


import sys
import  getopt


def readArgs():
	try:
		(opts,args) =  getopt.getopt(sys.argv[1:], 'm:n:o:', [])
	except getopt.GetoptError as error:
		print("\nError, ", str(error))
		return
	if len(opts) > 3:
		x = 1
		print("\nEntered more options than 3:\n")
		for opt, arg in opts:
			print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
			x += 1
		return
	elif len(opts) < 3:
		x = 1
		print("\nEntered less options than 3:\n")
		for opt, arg in opts:
			print(str(x)+ ':', "opt:", opt, "arg:", arg, "\n")
			x += 1
		return
	return opts

def calculate(parameters):
	if not parameters:
		return ""
	for opt, arg in parameters:
		if opt == '-n':
			if arg.isnumeric() or arg[0] == '-' and arg[1:].isnumeric():
				num1 = int(arg)
			else:
				print("\nWrong argument introduced to -n, must be an integer")
				print("Arg introduced to -n: ", arg,)
				return ""
		elif opt == '-m':
			if arg.isnumeric() or arg[0] == '-' and arg[1:].isnumeric():
				num2 = int(arg)
			else:
				print("\nWrong argument introduced to -m, must be an integer")
				print("Arg introduced to -m: ", arg)
				return ""
		else:
			if arg.lower() not in ["+", "-", "x", "/"]:
				print("\nWrong argument introduced to -o, valid options are '+', '-', 'x', and '/'")
				print("Arg introduced to -o: ", arg)
				return ""
			operator = arg.lower()

	if operator == '+':
		result = num1 + num2
	elif operator == '-':
		result = num1 - num2
	elif operator == 'x':
		result = num1 * num2
		operator = '*'
	else:
		try:
			result = num1 / num2
		except ZeroDivisionError as error:
			print("Error, ", error)
			return ""
	return "\n" + str(num1) + ' ' + operator + ' ' + str(num2) +  " = " + str(result) + "\n"


print(calculate(readArgs()))