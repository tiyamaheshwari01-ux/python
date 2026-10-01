# the function . items 
marks={
    "tiya":100,
    "tiyuu":101,
    "tanishka":200
}
print(marks["tiya"])

#using the actual function 
print(marks.items())
# this statement gives us the list of item within the dict. 
# but key and the value closed in a tuple to be notes 
#output as tuple in lists(miltiple) in a tuple 


print(marks.keys())
# gives as all the keys 
#list withn the tuple 
# the outer most braceket decides that what the actually data type is 
#[]-list
#()-tuple

print(marks.values())
# gives us the vlues 

#updating the dictionary 
print(marks.update({"tiya":1000,}))
# if we run thi it will return as none 
# we need ro add on the print statement after the update one
#bothdont work together as written in the next line 
marks.update({"tiya":1000})
print(marks)


# why this is happening bcz printing with the updation is returning non 
#as the python updates function of dict. do not return something it just update it in place 
#later after updation in place you can print 
#at the same time as above might show you (none)since,update always returns none


# get function 
# important differece
print(marks.get("tiya"))
print(marks["tiya"])
#works the same but are actually different 
# as
print(marks.get("tiya1"))
print(marks["tiya1"])
# the first gives the (none) in this we want if it exist then give us so it prints out none since nothing there like this 
# the second retuens the eorroras nothing exist like this.


#get works give output if any if not it returns none 
#marks-show you error since there is nothing like this existing in the above data 
# see the output dumbooooo
# works 
# smile 


# pop method
print(marks.pop("tiya"))
print(marks)
# help removeout the specific key
"""print(marks.pop(1000))"""
# you can remove items only giving the key values 

#popitem function
print(marks.popitem())
# this help to remove or pops out the last key and the value present in the given list 


#clear function 
print(marks.clear())
# gives out put as none for the reason nothing lest in the dictionary all clear 
#"none"

