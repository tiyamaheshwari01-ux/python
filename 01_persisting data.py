# this is without persisting the data 

name = input("Enter your name: ")
print(name)


# this when you persist the data means when you read and write in the file and save its completly so that it can be used later or edited later since saved permanently instead as above it runned in the random access memory.

name = input("Enter your name: ")
file = open("name.txt", "w")# here w is write in the file
file.write(name)
file.close()



# persisting data -
#Saving data so that it still exists even after the program is closed or the computer is restarted.


"""ram is the memory used for running the code since it is run the code and its volitile when we close the progrm everything wash off while persisting data is saving the data in the file so that it can be used later or edited later since saved permanently in sdd, hard disk in phonr or any where else."""


