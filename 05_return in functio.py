def function(name,emotion):
    print("hello",name)
    print(emotion)
    return"ok"

# using return 
a=function("tiya", "alright")


#a = function(...) ,value get stored 
# now a = "ok" ,can be used later on 

# what ever value you return is the value of the new assigned variable like here it will be vlue of a 
# also in the output you can find this tha print(a) returns "ok"  
print(a)
# this will lead to return none 

# we use retun as we say function takes and value and assign it to the variable jab bhi voh mange 


# another example of retuning the value 
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# we use return as it store the value back into the variable so that it can bed used later on.




#to be more precise what it is 

#👉 print() = for humans (output on screen)
#👉 return = for program (value for further use)




# get to know what exactly print and retun function are doing.
#Case 1: Only print() (no return)
"""Chef cooks food 🍝
Waiter shows it to you 👀
But doesn’t give it to you

👉 You saw it… but you can’t eat it.

➡️ That’s like:

print("hello")

✔️ Output is visible
❌ But not usable later

Case 2: Using return
Chef cooks food 🍝
Waiter hands it to you 🤲
Now you can eat, share, reuse it

➡️ That’s like:

return "food"""
 