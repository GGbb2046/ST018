# __Revision: Notes to class 0607__
### __Example 1__ 
S1 = “hello”

S1 =S1.upper()

### __Comparison for case upper:__

S=input(“enter a word exit to exit”) 

If s.upper() == ”exit”

break

### __Slicing__

S = input(“enter a word”)

If len(s) >1:

Print (s[1])

### _use pass if you want to do nothing after else_

### __Please visualize the data before passing command__

s = [ [ “Hello”]]

Print (s[0][0][0])

### __Example 2__

s = [ {“first”:[“hello”]}]

Print (s[0][“first”][0][0])  “H”

__Few notes__
1. java script don’t have tuples
2. Jason and text files are the two type of files we will handle. Shelf files are more proprietary.
3.  a and w creates new files

### __Example 3__

With open (“input.txt”) as fin:  opening for reading

S = fin.read()

S=s[0].upper() +s[1:]

With open(“output.txt”, ‘w’) as fout:

fout.write(S)

## __Serializing and Deserializing__

{“first”: “Hello”}

import json

with open(“input.txt”, ‘r’) as fin:

data=json.load(fin)

data[“first”] = data[“first”].upper()

with open(“output.txt”, ‘w’) as fout:

json.dump(data, fout)

## __Things to consider__
1. use json and create a list.
2. try solving the assignment 05 part 02 problem with a different approach

# __API’s__
Making calls to web API. It is a way to access service to get various data back.
1.	https://www. Timcsmith.com/my-api?first_arg=’Tim’&second_arg=”emith”
2.	protocol – https					Get request
3.	address
4.	default index.htm after the address
5.	two approaches – api_key requires registration and NO.
6.	PIP, anaconda are some of the way to install a package.
7.	Conda install requests
8.	Press shift alt F to wrap text
9.	Loads accepts a string unlike load which loads a file
10. quandro  is a service which has a package.

## __Things to cover in next class:__
Exception handling 
Tools to look at the software: static and dynamic analysis.
