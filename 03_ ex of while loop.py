###ex####
password="tanishka"
 
a= input("enter the passowrd:")
while a==password :
    print("access allowed")
    # if i will not give the break statment it will iterate that print statement n times 
    break
else:
    print("access denied")
# you need to assign a end statement bcz veran while loop will never terminate .
# works  



# this code without break statement 
# the version without break is generally considered better since it's logically more correct 



password="shashwat"

a=input("enter password:")
while a!= password:
    print("Access denied")
    break# with a while loop you always eed to use this break statament in this senerios.
else:
    print("access allowed")





# in this we made in loop as enter password again 

# better you do it like this 
password = "shashwat"
a = input("enter password: ")

while a != password:
    print("access denied")
    a = input("enter password again: ")

print("access allowed")
#👉 A loop should be written so it can end naturally, not forced to stop with break.
#Use while condition: → when you know the stopping condition
#Use while True + break → when stopping depends on something inside the loop.


# to terminate even this "enter password " again n again we set limits on .