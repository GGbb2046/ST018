p=[x for x in range(2, 2000) if all(x % y != 0 for y in range(2, x))] 

y=int(input("Please enter a number: "))

while True:
 
    if y in p:
        print("The number", y, "is prime.")
    
    elif y<2:
        print("This terminates our session. Have a nice day.")
        break
    
    else: 
        print("The number",y, "is not prime")
        
    y=int(input("Please enter another number: "))
        

    

    
