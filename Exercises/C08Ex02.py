import sys
import json

if len(sys.argv)==2:
    with open("Output.txt", "r") as fin:
        data = json.load(fin)
    print(data)       
else:
    print("please enter a single argument")
    
      
