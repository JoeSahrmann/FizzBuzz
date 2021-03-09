#FIZZbuzz by Joe Xavier
#Keep track of time
from datetime import datetime

#Saves the time when it starts
startTime = datetime.now()

#Make range
ranger = range(101)

#Start Range loop
for i in ranger:
    
#remove the math and do it at the beging
    three = i % 3
    five = i % 5
    
#detechs zero and replaces it  
    if (i == 0):                
        print("Welcome to FizzBuzz")

#checks if it is multiple of both 5 and 3
    elif (three == 0 and five == 0):
        print("FizzBuzz")

#checks if it is multiple of 3
    elif (three == 0):
        print("Fizz")

#checks if it is multiple of 5
    elif (five == 0):
        print("Buzz")

#if not any of the ones above print out the number
    else:
        print(i)
        
#How long did it take
print(datetime.now() - startTime)
#original time before improvement 0:00:00.232463
#NEW time 0:00:00.218723
