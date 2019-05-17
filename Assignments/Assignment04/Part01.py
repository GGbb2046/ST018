import random
A = random.randint(0,5)
counter =0
while True:
    x=int(input("Please enter a random number between 1 to 5:"))
    if x==A:
        print("Congratulations, the number you chose is ",x, "which is actually the random number chosen by the computer")
        break
    elif counter==2:
        print("you suck at this guessing game")
        break    
    else:
        print("Please try again")
    counter = counter +1

