#FIZZbuzz by Joe Xavier
#Make range here
for i in range(101):
    if (i % 3 == 0):
        print("Fizz")
    if (i % 5 == 0):
        print("Buzz")
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    if (i == 0):
        print("Welcome to FizzBuzz")
    print(i)
