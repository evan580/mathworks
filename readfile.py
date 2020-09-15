

f = open("matlab_script.txt", "r")


for line in f:
	if line == "\n":
		continue
	print(line)