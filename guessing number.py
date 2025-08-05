import math

upper_number = int(input("enter a high range number"))
lower_number = int(input("enter lower range number"))

random_number = int(input("enter random number"))

guess_number = int(input("enter guessing number"))

chances = 0
while chances <1:
    
    if guess_number == random_number:
        print("number is guessed")
        
    elif guess_number >random_number:
        print("u selected large number")
    
    elif guess_number < random_number:
        print("u selected low value")
    else:
        print("sorry you have not selcted")
    
    chances +=1
    
print("u have guessed the number in",chances,"chances")
    