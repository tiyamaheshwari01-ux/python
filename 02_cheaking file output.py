
f = open("file.txt", "r")# here r is read in the file
content = f.read()
print(content)
f.close()# this is the instruction where we get to know that we took whatever we wanna take from the file kindle close it.

#if you never call close(), the operating system keeps the file open until Python eventually closes it (usually when the program ends).


# the buy default of the open function is read .