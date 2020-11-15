import numpy as np
import datetime 

print("Welcome to the Number Game!")
name = input("Please Enter Your name: ")
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    print('Good Morning '+ name +'!')
elif 12 <= currentTime.hour < 18:
    print('Good Afternoon '+ name +'!')
else:
    print('Good Evening '+ name +'!')

x = np.random.randint(1,100,1)
n = int(input("Enter your Number: "))
var = x
if n == x:
    print("Congratulations! "+ name +". You guessed the number.")
    print("The number is ",x)
else:
    while n:
        if n > var:
            while (n > var):
                if (n > var):
                    print("Your number is greater than the required number.")
                    n = int(input("Enter your number: "))
                break
        elif n < var:
            while(n < var):
                if(n < var):
                    print("Your number is less than the required number.")
                    n = int(input("Enter your number: "))
                break
        elif n == var:
            print("Congratulations! "+name+". Your guess is correct.")
            print("The number is ", x)
            break
