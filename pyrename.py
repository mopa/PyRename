# -*- coding: utf-8 -*-
"""
PyRename 

Version: 0.8
Author: Pablo M. Pareja
License: GPL
"""
import os
# import re

from functions import *

###############################################
# Clear prompt of CLI
###############################################
clear = lambda: os.system('cls')

###############################################
# Menu
###############################################
def print_menu():
	clear()
	print("")
	print(30 * "-" , "MENU" , 30 * "-")
	print("1. Add prefix to files")
	print("2. Rename files with a counter")
	print("3. Rename files with a counter and match the word...")
	print("4. Replace/Remove Word")
	print("5. Exit")
	print(67 * "-")


# Directory that include the files to rename
directory = input("Directory of files: ")
os.chdir(r'%s' % directory)


loop = True
while loop:
	print_menu()
	choice = int(input("Enter your choice [1-5]: "))

	if choice==1:
		prefixfiles()
	elif choice==2:
		filescounter(21)
	elif choice==3:
		filescounter(22)
	elif choice==4:
		rrename()
	elif choice==5:
		loop=False
	else:
		input("Wrong option selection. Enter any key to try again..")