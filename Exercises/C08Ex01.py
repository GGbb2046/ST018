import sys
import json
string="Hello World"

if len(sys.argv)==2:
    with open("Output.txt", "w") as fout:
        json.dump(string, fout)
           
else:
    print("please enter a single argument")
    
      
