print("Welcome to the calculation of Future Value ")
PV= float(input("Please enter the present value ")) 
R= float(input("Please enter the rate of return in % ")) 
N= float(input("Please enter the time period ")) 
FV= PV*(1+(R/100))**N
print("The future value", "is ", FV)
