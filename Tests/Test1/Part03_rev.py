#defining function
def squirrelplay(t,s):
   
    if 60<=t<=100 and s=="is_summer":
        result = "TRUE"
          
    elif 60<=t<=90 and s!="is_summer":
        result = "TRUE"
    
    else:
        result ="FALSE"
      
    return result

#main program
print("\n")
print("True implies squirrel play and False implies squirrel do not play. \n")    
print("testing for is_summer at different temperatures \n")
print(squirrelplay(59,"is_summer")) #should print Flase
print(squirrelplay(60,"is_summer")) #should print True
print(squirrelplay(70,"is_summer")) #should print True
print(squirrelplay(80,"is_summer")) #should print True
print(squirrelplay(90,"is_summer")) #should print True
print(squirrelplay(95,"is_summer")) #should print True
print(squirrelplay(100,"is_summer")) #should print True
print(squirrelplay(105,"is_summer")) #should print False
print("\n")

print("testing for is_not summer at different temperatures \n")

print(squirrelplay(59,"is_not summer")) #should print False
print(squirrelplay(60,"is_not summer")) #should print True
print(squirrelplay(70,"is_not summer")) #should print True
print(squirrelplay(80,"is_not summer")) #should print True
print(squirrelplay(90,"is_not summer")) #should print True
print(squirrelplay(95,"is_not summer")) #should print False
print(squirrelplay(100,"is_not summer")) #should print False
print(squirrelplay(105,"is_not summer")) #should print False
