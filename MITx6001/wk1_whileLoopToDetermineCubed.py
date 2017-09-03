#This python program uses a whle loop to determine
#if a number entered by the user is a perfect cube
#or if it isn't, using a while loop and a conditional

numberToCheck = int(input("Enter a number to check if it is a perfect square:"))
answer = 0
while answer ** 3 < abs(numberToCheck):
    answer += 1;
if answer ** 3 != abs(numberToCheck):
    print(str(numberToCheck) + " is not a perfect cube.")
else:
    if numberToCheck < 0:
        answer = answer -1
    print("The cube root of " + str(numberToCheck) + " is " + str(answer))
