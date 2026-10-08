# for example we need to do it for 50 user 
#we can give name to this piece of logic using functions

# creating a function 
# also called####"function defination"####


def avg():
# you can give any syntax like i gave for avergare since it all depends on the formula
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=int(input("enter the number:"))

    average=(a+b+c)/3
    print(average)
    # this program wont give output bcz you seperted the logic but you didnt told when to do perform vg
    avg()# this meaning i want to run what ever i have written inside the function 
    # now it will run

# calling function as many as time i want five runs the same program for n times as i want 
#ex
    avg()# this is called function call 
    print("thankyou")
    avg()
    print("thankyou")
    avg()
    print("thankyou")
    avg()
    print("thankyou")
    avg()
# o here it will run the same program five times as shown 



# another exmple 
def fuc1():
    print("hello")
   
   # """def fuc1()"""
 # you dont cll it like this you call is just metion what nick name you gave a function 
    fuc1()       
    fuc1()       
    fuc1()
