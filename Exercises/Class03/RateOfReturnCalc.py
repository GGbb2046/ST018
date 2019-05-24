print("Welcome to the calculation of Rate of return ")
FV= float(input("Please enter the Future value ")) 
PV= float(input("Please enter the Present value ")) 
N= float(input("Please enter the Time period ")) 
R= (FV/PV)**(1/N) - 1
print("The rate of return in percentage", "is ", (R*100))