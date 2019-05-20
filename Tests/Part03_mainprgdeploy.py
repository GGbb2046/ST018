t=int(input("Please enter the temperature in Fahrenheit: "))

while True:   
    
    if t<60:
        print("FALSE. It is too cold for the squirrels to come out and play at ",t, "F be it any season."  )
        break
    
    elif t>100:
        print("FALSE. It is too hot for the squirrels to come out and play at ",t, "F be it any season."  )
        break

    elif t<=90:
        print("TRUE. It is an optimum temperature for squirrels to come out and play at ",t, "F be it any season")
        break
    
    else:
        s=input("Please enter T for summer or anything else to indicate other seasons ") 
        if s.upper()=='T':
            if t <= 100:       
                print("TRUE. The temperature is optimum at ",t ,"F ", "in summer so the squirrels are playing.")
                break
            else:
                print("FALSE. It is too hot at ",t ,"F ", "in summer so the squirrels are not playing.")
                break
        else:
            if t <= 90:       
                print("TRUE. The temperature is optimum at ",t ,"F ", "not in summer so the squirrels are playing.")
                break
            else:
                print("FALSE. Other than summer, it is too hot at ",t ,"F ", "for squirrels to come out playing.")
                break