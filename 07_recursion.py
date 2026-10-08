# a funtion calling itself is recursion
"""factorial(1)=1
factorial (2)=2*1
factorial (3)=3*2*1
factorial(4)=4*3*2*1
factorial (5)=5*4*3*2*1
factorial (n)=n*(n-1)......3*2*1
also can say 
factorial (n)=n*factorial(n-1)"""

# to be noted that factorial 0 is by defination 1
"""🪜 Climbing Down and Up Stairs
Going down → recursive calls
Reaching ground → base case
Coming back up → returning values"""



# 
def factorial(n):# giveing function defination what to do 
    if (n==1 or n==0):# giving up base case where threcursion will actully stop
        # with out mention base case the program would run forever so base case is really imporatant .

        return 1
    return n*factorial(n-1)# giving out main logic how to do it 

# we used the return bcz we need to sen the calculated value back to the place where function was called.

n =int(input("enter the value:"))
print(f"the factorial of this number is:{factorial(n)}")
# call the function # return gives the calculted value here.
# get returned value
# print it 



"""👉 So the function keeps asking itself:

“Hey, give me factorial of smaller number”"""
# getting it as a small number becomes the key and making and breaking in smaller and building the bigger output or the ans is what recursion darling.



