#typecasting 
#tells us what is the type of value stored in any varible 
a = 13
#print(a(type))# you cant write like this 
#the function you calling here must be outside the bracket the bracket must only consist of what we want as output 
print(type(a))
#can white it like this only 
name ="tanishka"
print(type(name))
value  = 10.9
print(type(value))
value  = "10.9"#we print it with in double quotes it will be as string intead of a float 
print(type(value))



#converting one data type to other if the convertion is possible 
b = float(value)
print(type(b)) #so here it was convertable value and we convertaed the string into float since it was possible 



#also,
c ="harry"
d = float(c)
print(d)
# this will not be converted as the value of "harry"is just not convertable or possible 
