#this checks if a number is perfectly divisible by 2 or 3.
#We can have multiple if statements branching into each other.
number = 10
if number % 2 == 0:
    if number % 3 == 0:
        print("The number is divisible by 2 and 3.")
    else:
        print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
