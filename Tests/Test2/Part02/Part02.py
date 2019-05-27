import sys #importing command line module for entering arguments
import requests # importing requests to fetch data from api
import json # importing a data structure which we will use in storing and analyzing data
from astropy.table import Table, Column # importing table modules to create user information table
import numpy as np # importing numpy for number operations
import matplotlib.pyplot as plt # importing graphics module to plot time series data

Requirement = ['Currency Converter', 'Stock Info'] # Creating of table to help the user input their command line arguments.
Argument = ['-c', '-s']
tab= Table([Requirement, Argument],names = ('Requirement','Argument'))

if len(sys.argv)==1:# Informing user that they have to input an argument to proceed
    print("\n")
    print("Please retry entering one of the following arguments to meet your requirement: ")
    print("\n")  
    print(tab)
    

elif len(sys.argv)>2: # Informing the user that they have entered too many arguments
    print("You have entered multiple arguments. Please retry entering a single argument following the program name.\n")
    print(tab)

else:
    while True:
        if sys.argv[1] == '-c': 
            print("\n")
            print("This extension of the program enables you to compute the equivalent foreign currency amount for your domestic currency. \n")
            Currency = ['US Dollar', 'Eurpean Euro', 'Japanese Yen', 'British Pound', 'Swiss Franc', 'Canadian Dollar', 'New Zealand dollar','South African Rand'] 
            Ticker = ['USD', 'EUR','JPY','GBP','CHF','CAD','NZD', 'ZAR']
            t= Table([Currency, Ticker],names = ('Currency','Ticker'))
            print(t,"\n")
            dc=input("Please input your domestic currency ticker from the list provided above or any other of your choice: ")
            fc = input("Please input the foreign currency ticker from the list provided above or any other of your choice: ")
            a= input("The amount of "+dc + " you want to exchange for "+fc+": ")
            
            if dc==0 or fc ==0 or a==0:
                print("Please enter valid input.")
            else:# processing input from the customer and calling data from API
                c='CURRENCY_EXCHANGE_RATE'
                api_key = "J42OIFGWMD37J58V" # this is my appid for alpha vanatage
                base_url = 'https://www.alphavantage.co/query?'
                full_url = base_url +  "function="+c+'&from_currency='+dc.upper()+'&to_currency='+fc.upper()+'&apikey='+api_key 
                # fetching the request and storing the data in memory within a json structure
                f = requests.get(full_url)
                json_string = f.text
                
                if len(json_string) < 1:
                    print("The API is currently unavailable. Please try again in a few minutes. ")
                    break
                else: 
                    parsed_json = json.loads(json_string)
                    
                    try: #use of exception handle to throw an error if the user is unable to input valid input for tickers and amounts
                        bidr = parsed_json['Realtime Currency Exchange Rate']['8. Bid Price']
                        askr = parsed_json['Realtime Currency Exchange Rate']['9. Ask Price']
                        br = round(float(bidr),4)
                        ar = round(float(askr),4)
                        sp = round((ar-br),4)
                        t = int(br*round(float(a),2))
                    
                    except: #ser informing the user of their invalid inputs
                        print("\n")
                        print("You have entered invalid inputs. Please retry entering valid inputs for currency tickers or amount for conversion or both.")
                        break
                    
                    else:# displaying the amounts to be received after exchange with the quoted spread
                    
                        print("The amount you will receive upon exchange is {:,} ".format(t) +  fc)
                        print("The quoted spread on the exchange is {:.4f} ".format(sp))
                        print('Have a nice day!')
                        break

        elif sys.argv[1] == '-s':# checking for the stock analysis extension of the program
            print("\n")
            print("This extension of the program enables you to reflect on the current stock price of your ticker with a daily time series for last 100 days.\n")
            s=input("Please enter a stock ticker of your choice: ")
            t='TIME_SERIES_DAILY'
            api_key = "J42OIFGWMD37J58V" # this is my appid for alpha vanatage
            base_url = 'https://www.alphavantage.co/query?'
            full_url = base_url +  "function="+t+'&symbol='+s+'&apikey='+api_key+'&datatype=json'
            
            f = requests.get(full_url)
            json_string = f.text
                
            if len(json_string) < 1:# informing the user that the program is unable to call data from the server.
                print("The API is currently unavailable. Please try again in a few minutes. ")
                break
            else: 
                parsed_json = json.loads(json_string)# parsing the json structure to fetch keys and values
                
                try:
                    date = [date for date in parsed_json['Time Series (Daily)'].keys()]# creating list of dates 
                    list.reverse(date)# reversing the order of dates in a chronological order
                    dict2 = {x:parsed_json['Time Series (Daily)'][x]['4. close'] for x in date}# creating a new dictionary for date keys and stock prices as the values
                    print("The current price of stock "+s+" is "+ dict2[parsed_json['Meta Data']['3. Last Refreshed']])
                    
                    #preparing the coordinates for graph
                    x = dict2.keys() 
                    y = [float(y) for y in list(dict2.values())]
                    plt.figure(figsize=(80,10))#setting the size of the graph
                    plt.plot(x,y,color ='green', marker = '.')
                    plt.gca().yaxis.set_major_locator(plt.LinearLocator())# setting the ticks for linearity and aesthetics
                    plt.gca().xaxis.set_major_locator(plt.LinearLocator())
                    plt.xlabel('Time')# setting the labels for the axes
                    plt.ylabel('Price')
                    plt.title(s.upper())
                    print("Please refer to the new window that has opened just now for the time series plot.\n")
                    plt.show()
                    print("Have a nice day!")
                except:
                    print("You have entered an invalid ticker for your chosen stock.")#exception throw that the user has input an invalid ticker.


                break

        else:
            print("Please enter the correct argument after the program name. \n")# throw an error that the user did not enter the correct argument from the table. 
            print(tab)
            break
