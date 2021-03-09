#FIZZbuzz by Joe Xavier
#Start Range loop
for i in range(101):#Makes Range
    if (i == 0):#detechs zero and replaces it with
        print("Welcome to FizzBuzz")
    elif (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
