import sys
import requests
import json
base_url = 'http://api.icndb.com/jokes/random?'
if len(sys.argv) == 3:
    
    full_url = base_url+"firstName="+sys.argv[1]+"&lastName="+sys.argv[2]  
    f = requests.get(full_url)
    json_string = f.text

    if len(json_string) < 1:
        print("The API is currently unavailable. Please try again in a few minutes. ")
    else: 
        parsed_json = json.loads(json_string)
        joke = parsed_json['value']['joke'] 

    print(joke)

else:
    print("You have to enter first name and last name as two arguments.") 
