import sys
import json

string =[[1,2,3,4,5],{"fname":"Galab", "lname":"Bista"}]
if len(sys.argv)==2:
    with open("output_1.txt",'w') as fout:
        json.dump(string, fout)

else:
    print("Please enter a single argument")