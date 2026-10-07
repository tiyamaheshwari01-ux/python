# break,continue,pass statement 
i=0
for i in range (0,100):
    if(i==26):
        break# break the line through the condiction met in
    print(i)
    i+=1

# use of continue statment 
i=0
for i in range (0,100):
    if(i==26):
        continue# this will allow to print in the all the value except the condition and after the condition it continue to print in in range given
    print(i)
# continue statment iteration is skipped 
# break statement skips the loop 



# use of pass statement 
i=0
for i in range(0,90):
    pass
while (i<10):
    print(i)
    i+=1