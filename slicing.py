# slicing strings in python
name = "tanishka"# i can this line i made it from top to bottom using (alt + down arrow)
# name[1]=character[1] # strings are immutable in Python
print(name[1])# you can write like this this ,":" tthe semicolon is always required in the process of indexing
print(name[:5])
# there is also something callled negative indexing in python like last charchater will be denoted b index (-1)
namw1="gauri maheshwari"
print(namw1[:-1])

# this won't show the last string character because of the negative indexing    
#tab is used to accept the recommandation of index vs code 

print (namw1[1:5])#always remember that the last index is not included in the output
print(namw1[0:])# this will print the whole string because the last index is not mentioned.
print(namw1[:])# this will also print you the whole string 
#because the first and last index is not mentioned.

print(namw1[::2])# this will print the whole string with stepping size of 2.
print(namw1[::-1])# this will print the whole string in reverse order because of the negative step size.




