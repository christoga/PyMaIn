#!/usr/bin/python
import os
__author__ = "Andre Christoga"

def main():
	'''
	Python Math Input
	'''	
	input = raw_input("> (eg plus, minus, divide...)")

	if input == "plus":
		os.system("pymain/plus.py")
	if input == "minus":
		os.system("pymain/minus.py")
	if input == "multi":
		os.system("pymain/multi.py")
	if input == "divide":
		os.system("pymain/divide.py")
	if input == "modulos":
		os.system("pymain/modulos.py")

if __name__ == '__main__':
	main()