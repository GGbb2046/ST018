#creating a list of possible temperature ranges 
t=[50,55,59,60,70,80,90,91,100,101,110]

#creating a list of boolean for presence or absence of summer
s=["in summer", "not in summer"]

#displaying the list of temperature and boolean ranges
print("We have used the following temperature range for testing the program\n")
for i in t:
    print (i, end= "  ")
print('\n')
print("We have used the following boolean range for seasonality effect testing in the program\n")
for i in s:
    print (i)
print('\n')

#testing the program for each possible combination of temperature and boolean
for i in t:
    while True:   
        
        if i<60:
            print("FALSE. It is too cold for the squirrels to come out and play at ",i, "F be it any season."  )
            break
        
        elif i>100:
            print("FALSE. It is too hot for the squirrels to come out and play at ",i, "F be it any season."  )
            break

        elif i<=90:
            print("TRUE. It is an optimum temperature for squirrels to come out and play at ",i, "F be it any season.")
            break
        
        else:                                  
                    for j in s:
                    
                        if j=='in summer':
                            print("TRUE. The temperature is optimum at ",i ,"F", j,"so the squirrels are playing.")
                            
                        else:
                            print("FALSE. It is too hot at ",i ,"F ", j, "so the squirrels are not playing.")
                            break
                       
        break