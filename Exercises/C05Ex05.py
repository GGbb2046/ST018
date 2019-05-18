s2 = [x**3 for x in range(101)]
for i in s2:
    if (i**(1/3))<=99:
        print(i,end="-")
    else:
        print(i,end="")
    
