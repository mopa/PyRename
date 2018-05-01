import os
###############################################
# Clear prompt of CLI
###############################################
clear = lambda: os.system('cls')

###############################################
# Add a prefix to files
###############################################
def prefixfiles():
	clear()
	prefix = input("Prefix:  ")

	for filename in os.listdir("."):
	    os.rename(filename, prefix + filename)

###############################################
# Rename complete names and add a counter
###############################################
def filescounter(param):
	clear()
	renamefile = input("-> New Name:  ")

	listfile = []
	listfile = os.listdir(".")

	if param == 21:
		for filename in listfile:
			fileindex = listfile.index(filename)
			os.rename(filename, renamefile + str(fileindex+1) + filename[len(filename)-4:])
	else:
		matchtext = input("-> Match Word: ")
		for filename in listfile:
			fileindex = listfile.index(filename)
			if filename.startswith(matchtext):
				os.rename(filename, renamefile + str(fileindex+1) + filename[len(filename)-4:])


###############################################
# Replace/Remove Word
###############################################
def rrename():
	clear()
	renamefile = input("-> New Word: ")
	matchtext = input("-> Old Word: ")

	listfile = []
	listfile = os.listdir(".")

	for filename in listfile:
		os.rename(filename, filename.replace(matchtext,renamefile))