#First python lab
#Guess the random Number between 1 - 15
import random
rn = random.randint(1,15)
win = False
turns = 1
r = range (0,16)
while win==False:
    number1 = input("Enter a number between 1 and 15: ")
    number = int(number1)
    if number not in r:
        print("Please select a number between 1 and 15 and try again")
    else:
        if rn == number:
            win = True
            print("You guessed the correct number!", rn)
            print('You guessed the correct number in:',turns,'turns')
            break
        else:
            turns += 1
            if rn < number:
                print("Your guess was too high, please try again")
            else:
                print("Your guess was too low, please try again")    