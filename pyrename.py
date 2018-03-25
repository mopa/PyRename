# -*- coding: utf-8 -*-
"""
PyRename 

Version: 0.5
Author: Pablo M. Pareja
License: GPL
"""
import os

###############################################
# Add a prefix to files
###############################################
def prefixfiles():
	print("Name of Prefix:")
	prefix = input()

	for filename in os.listdir("."):
	    os.rename(filename, prefix + filename)

###############################################
# Rename complete names and add a counter
###############################################
def filescounter(param):
	print("Name to rename:")
	renamefile = input()

	listfile = []
	listfile = os.listdir(".")

	if param == 21:
		for filename in listfile:
			fileindex = listfile.index(filename)
			os.rename(filename, renamefile + str(fileindex+1) + filename[len(filename)-4:])
	else:
		matchtext = input("Match word: ")
		for filename in listfile:
			fileindex = listfile.index(filename)
			if filename.startswith(matchtext):
				os.rename(filename, renamefile + str(fileindex+1) + filename[len(filename)-4:])


###############################################
# Menu
###############################################
def print_menu():
	print(30 * "-" , "MENU" , 30 * "-")
	print("1. Add prefix to files")
	print("2. Rename files with a counter")
	print("3. Rename files with a counter and match the word...")
	print("4. Exit")
	print(67 * "-")


# Directory that include the files to rename
directory = input("Directory of files: ")
os.chdir(r'%s' % directory)


loop = True
while loop:
	print_menu()
	choice = int(input("Enter your choice [1-4]: "))

	if choice==1:
		prefixfiles()
	elif choice==2:
		filescounter(21)
	elif choice==3:
		filescounter(22)
	elif choice==4:
		loop=False
	else:
		input("Wrong option selection. Enter any key to try again..")