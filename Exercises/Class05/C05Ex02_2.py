import random
e2f = {1:'uno',2:'deaux',3: 'trois', 4: 'quatre', 5 : 'cinq', 6: 'six', 7: 'sept', 8:'huit', 9:'neuf'}

while True:
    a = random.randint(1,9)
    print(a)
    x=input("Please enter the French equivalent of the number on screen or exit the program by typing exit ")

    if e2f[a] == x:
        print("Viola, you have the correct translation for the number ",a, "which is ", x)

    elif x.lower() =="exit":
        
        break
    
    else:
        print("The correct word for french is different ")

print("Thankyou for playing")

