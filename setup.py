#!/usr/bin/python
# from setuptools
# import setup
import os

__author__ = "Andre Christoga"
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

# setup(
#     name="PyMaIn",
#     version="1.0.0",
#     author="Coding Smart School",
#     author_email="codingsmartschool@gmail.com",
#     url="https://github.com/codingsmartschool/pymain",
#     description="Python Math Input",
#     long_description=("PyMaIn is a python program that takes maths number"                 
#                       " and give user the answer."),
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Programming Language :: Python',
#     ],
#     license="MIT",
#     packages=['pymain'],
# )