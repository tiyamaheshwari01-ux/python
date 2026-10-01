# function of sets 

# union 
set_1={1,2,3,4,5,6}
set_2={1,2,3,5,6,7,8,9}
print(set_2.union(set_2))

#intersection
print(set_1.intersection(set_2))


#finding subset 
print({1,2}.issubset(set_1))
# is a inside b?
#🍎 {1,2} = a small basket of fruits
#🧺 set_1 = {1,2,3,4} = a big basket

# subset are the number which are present in the set already this returns us boolean value 


#finding id any superset is there 
print(set_1.issuperset({1,2}))
#does set_1 contain the given set??
#Does the big basket contain all fruits of the small basket?”

# the reason they have bit of different index 
