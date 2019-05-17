t=float(input("Please enter the temperature in Fahrenheit "))
if t>=212:
    print("The water at this temperature is in gaseous state")
elif t<=32:
    print("The water at this temperature is in frozen state")
else: 
    print("The water at this temperature is in liquid state")