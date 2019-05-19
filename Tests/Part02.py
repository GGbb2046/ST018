p=[x for x in range(2, 2000) if all(x % y != 0 for y in range(2, x))] 

while True:

    y=int(input("Please enter a number between 2 and 2000 "))
    
    if y in p:
        print("You have entered a prime number")
    
    elif y<2:
        print("You have chosen to exit the program. Have a great day!")
        break
    
    else: 
        print("The number you entered is not prime")

    

    
