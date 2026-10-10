f = open("file.txt", "r")# here r is read in the file
lines = f.readlines()# this is the instruction where we get to know that we took whatever we wanna take from the file kindle close it.
print(lines)
print(type(lines))
f.close()