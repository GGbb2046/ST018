import sys
import requests
import json
from astropy.table import Table, Column
import numpy as np

Requirement = ['Currency Converter', 'Stock Info'] 
Argument = ['-c', '-s']
tab= Table([Requirement, Argument],names = ('Requirement','Argument'))

if len(sys.argv)==1:
    print("Please retry entering one of the following arguments to meet your requirement: ")
    print("\n")  
    print(tab)
    

elif len(sys.argv)>2:
    print("You have entered multiple arguments. Please retry entering a single argument follwing the program name.\n")
    print(tab)

else:
    while True:
        if sys.argv[1] == '-c':
            
            Currency = ['US Dollar', 'Eurpean Euro', 'Japanese Yen', 'British Pound', 'Swiss Franc', 'Canadian Dollar', 'New Zealand dollar','South African Rand'] 
            Ticker = ['USD', 'EUR','JPY','GBP','CHF','CAD','NZD', 'ZAR']
            t= Table([Currency, Ticker],names = ('Currency','Ticker'))
            print(t,"\n")
            dc=input("Please input your domestic currency ticker in the list provided above or any other of your choice: ")
            fc = input("Please input your foreign currency ticker in the list provided above or any other of your choice: ")
            a= input("The amount of "+dc + " you want to exchange for "+fc+": ")
            if dc==0 or fc ==0 or a==0:
                print("Please enter valid input.")
            else:
                c='CURRENCY_EXCHANGE_RATE'
                api_key = "J42OIFGWMD37J58V" # this is my appid for alpha vanatage
                base_url = 'https://www.alphavantage.co/query?'
                full_url = base_url +  "function="+c+'&from_currency='+dc.upper()+'&to_currency='+fc.upper()+'&apikey='+api_key 
                # print("Here is the full URL being used for the WebAPI call", full_url)
                f = requests.get(full_url)
                json_string = f.text
                if len(json_string) < 1:
                    print("The API is currently unavailable. Please try again in a few minutes. ")
                    break
                else: 
                    parsed_json = json.loads(json_string)
                    #print(parsed_json)
                    try:
                        bidr = parsed_json['Realtime Currency Exchange Rate']['8. Bid Price']
                        askr = parsed_json['Realtime Currency Exchange Rate']['9. Ask Price']
                        br = round(float(bidr),4)
                        ar = round(float(askr),4)
                        sp = round((ar-br),4)
                        t = int(br*round(float(a),2))
                    except:
                        print("You have entered invalid arguments. Please retry entering valid arguments")

                    else:
                    
                        print("The amount you will receive upon exchange is {:,} ".format(t) +  fc)
                        print("The quoted spread on the exchange is {:.4f} ".format(sp))
                        break

        elif sys.argv[1] == '-s':
            print("work under progress")
            break

        else:
            print("Please enter the correct argument after the program name. \n")
            print(tab)
            break
