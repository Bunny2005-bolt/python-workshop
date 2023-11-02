#1
def my_function():
    x=10 #x local variable
    print(x)
my_function()

#2
y=10 #y is global variable
def myfunction():
    print(y)
myfunction()

#3
z=10 #global variable
def modify_global():
    global z
    z=20
    print(z)
modify_global()

#4
import random
def guess_number():
    return random.randint(1,100)
target_number=guess_number()
attempts=0
while True:
    user_guess=int(input("guess a number:"))
    attempts+=1

    if user_guess == target_number:
        print("congratualtions! you won a game in {attempts} attempts")
        break
    elif user_guess<target_number:
        print("try a higher number")
    else: 
        print("try a lower number")


