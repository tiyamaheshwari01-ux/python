def good_day(name,greeting):
    print(f"hiii,{name}")
    print(greeting)
good_day("tanishka","love you")
# this is whTat passing value whn function call 
# in this its definate that you need to pass 2 arguments 


def good_day(name,greeting="love you"):
    print(f"hiii,{name}")
    print(greeting)
good_day("tanishka","beautiful")
# this is what system do have the default value (love you)
# now if i right anything else like here"beautiful" while function call it will give me out put 
# as that since passed value while calling 
# function if i wold have not passed value then it would have shown the defult value (love you)


# in this its not definate since there is one defult argument already there..you may 1 or 2 your choice 



# analogy
"""🎁 Case 1 (No default)

You order a custom gift:

You MUST specify message every time

👉 “Write message on card?” → You HAVE to answer

🎁 Case 2 (Default value)

Shop already has a default message:
👉 “Happy Birthday”

If you don’t say anything → it uses default
If you want → you can change it"""