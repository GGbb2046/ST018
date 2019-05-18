## Items covered in last class - Structural Program
1. Sequence
2. Selection 
3. If
4. Elif
5. else
#### Repetition
1. for
2. while

####Logical expression
1. Relational
2. Boolean

In python, the coverage of your testing should be wide – unit testing and integrating testing
##Tips
1. #### Testing requires input from the programmer
2. #### Colon defines structure of the following codes
3. #### Define function and #define program for clarity

####Return is implied in python

1. Def PV(FV=110, r=0.1, n=1): ( is possible)
2. Let the main program determine the output as far as possible to generalize your solution

Atomic		In-between	Composite
		    String		Tuple
Int			List
Float				    Dictionary
Bool				    Collection-sets, queues, counter
			
1.	List is the most popular among the composites, tuple is similar.
    1.  	Colors 1 = [“red, “green”]  list
   
    2.	Colors 2 = (“red”, “green”)  tuple

2.	Tuples are immutable while list is mutable. Mutable allows addition or removal of an element.

3. To access the individual items on the list  print(colors1[1])

4.	Tuples can be modified only by creating a new tuple
•	Str =”Hello”	str is immutable
o	If Str[0] ==”h”:
Str[0] = “H” (Not possible due to immutability)

*e.g.*
colors =(“blue”) + colors[1:2]
colors1[0] = “blue” [“red”, “green”]

*e.g. List modification*

c=color[0]

x= “R” +c{1:]

Print(x)  Red

Alternatively,

X = “R” + color[0][1:]

### Tuple over list has advantages of security and speed.In tuple however, (“Red”)+color[1:2] is similar to the adjustments to string.

###Methods
1.	L=[0,2,5]
2.	L.append(7)  [0,2,5,7]
3.	L.pop(0)  [2,5,7] (Pop actually returns the value and so can be assigned to a variable)
4.	Del L[0]  [2,5,7]
5.	L.remove(7)  [0,5]
6.	Insert(1,127)  [0,127,5]

### Dictionaries (Mutable)

d = {‘b’:2,’c’:3,’f’:20} here b, c and f are the keys	

print(d[‘b’])  2

print(d[‘z’])  error	

e2f = { “one” : “un”, “two” : “deux” , “three” : “trois”, “four” : “quatre” }

word = input (“ Enter English word for math 1,2,3 or 4: )

Print (e2f[word])

1. Casting a tuple into a list : list(ctuple)
2. Collection are new to python.
3. The in(not in) operator checks the existence(absence) of data in a list or a tuple
4. Also used in word search
5. Display keys or values dictionary.keys(values) ;default is keys
### You can build a dictionary using two lists by casting to them to a dictionary
### Please call in a library 
### count += 1 would mean count = count=+1

#### List comprehension could be used to replicate for loops. Print function is like a typewriter, two sequential print commands pushes the second output to a new line. To override that however, we would have to print (‘Hello”, end=””)

To add two line print(‘Hello’, end =”-\n”)

### Command line arguments
1. Import the library sys
2. Import sys
3. Print (sys.argv)
    for arg in sys.argv:
    print(arg)

