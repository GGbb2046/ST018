# Quick review from last class
1.	Types of operands: Bool (true or false), Float (3.14), Int (3), String(“Apple” or ‘Apple’) 
2.	Types of Operators: +, -, /, *, //, %
3.	Expression is the combination of operators and operands
    1.	Arithmetic expression
    	PEMDAS
    2.  String expression
        +   Concatention
	    * ------    “*” * 80 – Repeating
    3. Logical expression
        1. Relational operators - >, < , = , <=, >= ,= = , ! = (Binary operators)
        2. Boolean operators – and, or, not (not is a unary operator)

*Two types of loops in a python: for loop  and while loop*
*All variables are reference variables in python*

Example

## Logical operation

    X=10

    Y=12

    Z=13

    int(x>y) --> False

We can perform logical operations on 3 variables

-->print(x<y<z) True

## Boolean operation
1. bool and bool; can perform bitwise operation.
2. AND is true when both sides are true

### Elegant is always simple!

*Example_1*

    x=int(input(“   “))

    If 0<=x<=100

        Print(“good user”)

    Else: 

        Print(“bad user”)

*Example 2*

    X =int(input(“”)

    If x>=920

        Print(“”)

    Elif:

        Print(“”)

    Else:

        Print(“”)

### *Single, double and multi block selection are approaches to the logical operation.

## Iteration
1. For loop

*Examples*

    for i in range(10): -->0 to 9 will be displayed

    print (i)

    for i in range(1,10): --> 1 to 9 will be displayed

    for i in range(1,10,2): --> odd numbers displayed

*Countdown*

    for i in range(10,0,-1): --> descending order
	
    print(i)

    print(“blastoff”)

### While Loop

Counter= 10

    While counter >0:

	Print(Counter)

	Counter = counter-1

•	Break
•	Continue
•	Pass

    While True:

    X= int(input(“enter value between 0 and 100 inclusive”))

    If 0<=x<=100:

        print (“good”)

        Break

    Else: 

    print(“please reenter the value”)


    str =(”ITM695”)

    counter=0

    While counter <len(str):
        Print (str[counter])
        Counter = counter +1


## Determining the length of string
    Str=”hello”
    Print (len(str))


## Pulling out the first character from a string (string slicing)
    Str =”hello”
    Print(str[0:4:2])



## Functions
    •	Reducing duplication of codes
    •	Decomposing complex problems
    •	Improving readability

# You can create, import or use built in function

    ### Defining function 

    Def <circle_area>(r):

        A=3.14*r**2

        Return A

    ### Main program
    
        Print(circle_area(2))
    
        X=10
    
    Print (circle_area(x))
    
    A=20

    Print(circle_area(A))

*Example*
        
        def  FV(PV,r,n):
        
            return PV*(1+r)**n
        
        def Print_banner(str)	
        
            print(“*”*(len(str)+2))
        
            print(“*”+str+”*”)
        
            print(“*”*(len(str)+2))
        
            return None

    Print (FV(100,0.1,1))
 

*Setting Default values*

    Def circle_area(r=1): Optional argument – 
    
    Default values
	
    Return 3.14*r**2

    Print (circle_area())
    
    Or Print (circle_area(5))

	def  FV(PV,r,n):
		return PV*(1+r)**n

    Print (FV(r=.01, PV=100,n=1))  
    
If we forget the parameters sequence or changing the sequence


Test the units rigorously before pushing them to the libraries
