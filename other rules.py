name1="tisha pandey"
print(name1[1:5])
print(name1[-5:-1])# printed from backward index 

name2="shivi pandey"
print(name2[1:])
# last is not mentioned so it  will print the wholw string but starting by index1

print(name1[0:5:2])
# this is callled step size indexing in python it will giv output as per the mentioned index
#in this is printing like first the values from index 0 to 5 and
#  then it is printing the value of index 0 and then it is skipping the next value 
# and printing the value of index 2 and then it is skipping the next value and printing 
# the value of index 4 because of the step size of 2.
# in general the last index tell us how many chracter we need to skip in.
