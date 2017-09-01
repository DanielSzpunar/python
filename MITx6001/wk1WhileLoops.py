start = 1
while start <= 100:
    if start % 3 == 0 and start % 5 == 0:
        print(str(start)+ ". Fizz Buzz")
    elif start % 3 == 0:
        print(str(start) + ". Fizz")
    elif start % 5 == 0:
        print(str(start) + ". Buzz")
    else:
        print(str(start) + ".")
    start += 1
