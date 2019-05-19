t=int(input("Please enter the temperature in Fahrenheit: "))

while True:   
    
    if t<60:
        print("It is too cold for the squirrels to come out and play at ",t, "F be it any season."  )
        break
    
    elif t>100:
        print("It is too hot for the squirrels to come out and play at ",t, "F be it any season."  )
        break

    elif t<=90:
        print("It is an optimum temperature for squirrels to come out and play at ",t, "F be it any season")
        break
    
    else:
        s=input("Please enter T for summer or anything else to indicate other seasons ") 
        if s.upper()=='T':
            if (60 <= t <= 100):       
                print("The temperature is optimum at ",t ,"F ", "in summer so the squirrels are playing.")
                break
            else:
                print("It is too hot at ",t ,"F ", "in summer so the squirrels are not playing.")
                break
        else:
            if (60 <= t <= 90):       
                print("The temperature is optimum at ",t ,"F ", "not in summer so the squirrels are playing.")
                break
            else:
                print("Other than summer, it is too hot at ",t ,"F ", "for squirrels to come out playing.")
                break