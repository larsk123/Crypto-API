import requests
import pandas as pd
import numpy as np
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)
import csv
import time as t
from datetime import datetime

#sec=int(input('>>'))
sec=100
with open('api_price.csv', 'a', newline='\n') as csvfile:
    fieldnames = ['time', 'exmo_bid', 'exmo_ask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

while sec>0:
#while 1>0:
    time = datetime.now()

    #Exmo API
    response = requests.get("https://api.exmo.com/v1/order_book/?pair=BTC_USD")
    data = json.loads(response.text)
    #should you do time stamp of server time?
    exmo_bid =float(data['BTC_USD']['bid'][0][0])
    exmo_ask =float(data['BTC_USD']['ask'][0][0])


    with open('api_price.csv', 'a', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'time': time,'exmo_bid': exmo_bid, 'exmo_ask': exmo_ask})
    #pp.pprint(exmo_ask) #you are printing a random one just to make sure something is coming in!
    t.sleep(1) # every second
    sec-=1  # take one second awayt
