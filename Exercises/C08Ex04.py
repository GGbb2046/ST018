import sys
import json

if len(sys.argv)==2:
    with open("output_1.txt", 'r') as fin:
        data=json.load(fin)
        print(data)
else: 
    print("please enter a single argument")
