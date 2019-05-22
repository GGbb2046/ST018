numbers = [1,2,3,4,5,6,7]
for count, i in enumerate(numbers):
    print(i,end='')
    if count <len (numbers)-1:
        print ('-',end ='')
