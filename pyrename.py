import os

prefix = "a2_"

for filename in os.listdir("."):
    os.rename(filename, prefix + filename)
