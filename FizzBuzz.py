#FIZZbuzz by Joe Xavier
#Keep track of time
from datetime import datetime

#Saves the time when it starts
startTime = datetime.now()

#Start Range loop
for i in range(101):
    
#remove the math and do it at the beging
    
#detechs zero and replaces it  
    if (i == 0):                
        print("Welcome to FizzBuzz")
    elif (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
        
#How long did it take
print(datetime.now() - startTime)
#original time before improvement 0:00:00.232463
