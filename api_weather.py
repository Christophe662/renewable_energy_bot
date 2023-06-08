# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:44:42 2023

@author: Christophe
"""

import requests



#cityName= input("nom de la ville:")

def meteo (cityName):
    langage="en"
    api_key="ac4cc9fec3475cdd3c67e464a126a4a9"
    api_link=f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}"


    json= requests.get(api_link).json()
    JSON = json['weather'][0] ['main']
    JSON1 =json['main'] ['temp']
    return JSON, JSON1
   
    





"""
url = "https://digital.iservices.rte-france.com/token/oauth/"
data={
     'Authorization': 'Basic YmU0YWNmZDAtMTVmNC00M2Q4LThlMWMtMzllZmVjNzRjYWQ1OjRlYWIzZmMzLTIzMTgtNGQ1Ny05NzIyLWY3YjkxNzQ4OWU0Mg==',
     'Content-Type': 'application/x-www-form-urlencoded',    
      }

response=requests.post(url, headers=data)
status_code= response.status_code
print ('status code=', status_code)  #200 poue ok
infos_rte_token = response.json()
print('infos RTE token=', infos_rte_token)
token= infos_rte_token['access_token']
print ('token=', token)

url1= "https://digital.iservices.rte-france.com/open_api/ecowatt/v4/signals"
data1={
      'Authorization': 'Bearer '+ token,
      'Content-Type':  'application/soap+xml',
      'charset': 'UTF-8',     
      }

response1= requests.get(url1, headers=data1)
status_code1= response1.status_code
print ('status code=', status_code1)  #200 poue ok

infos_rte_data_ecowatt_json = response1.json()
print ('info rte data_ecowatt_json=', infos_rte_data_ecowatt_json)

heure=16
signal= infos_rte_data_ecowatt_json['signals'][0]['values'][heure]
print (int (signal.get('hvalue')))
"""


"""
url = "https://www.nordpoolgroup.com/api/marketdata/page/10?currency=EUR&endDate=2023-06-06&startDate=2023-06-06&area=DK1,DK2,FI,NO1,NO2,NO3,NO4,SE1,SE2,SE3,SE4"
headers = {
    "Accept": "application/json",
    "Authorization": "Basic Y2xpZW50X3JlbWl0X2FwaTpjbGllbnRfcmVtaXRfYXBp"
}


response = requests.get(url, headers=headers)
data = response.json()
# Traitement des données JSON pour obtenir les prix de l'électricité
prices = {}

for item in data['data']['Rows']:
    country = item['Columns'][0]['Name']
    price = item['Columns'][2]['Value']
    prices[country] = price
    
    print (country,price)

"""










