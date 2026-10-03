 
    # we often cofuse between that if always is previous of else 
    # but if can also start after else it will start cheaking other sererate condition 
    #ex.
a=int(input("enter the number"))
# condition 1 started
if a>20:
    print("valid")

else:
    print("invalid")
 # condition 1 ended 
 # condition 2 started(if the beging if the nexw condiction )    
if a%2==0:
    print("number is even")
# so the problem breaked that if and be run after else ,elif
# also this runs to tell a seperate condition 



"""elif a > 5:
    print("...")
if a % 2 == 0:   # ❓""" #not wrong
