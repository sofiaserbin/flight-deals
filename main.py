import requests

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager


data_manager=DataManager()
sheet_data=data_manager.get_rows()
i=2


while i<=len(sheet_data["prices"])+2:
    if len(sheet_data["prices"][i-2]["iataCode"])==0:
        print("Empty code")
        sheet_data["prices"][i-2]["iataCode"]="TESTING"
        new_data = {
            "price": {
                "iataCode": "TESTING"
            }
        }
        response = requests.put(
            url=f"https://api.sheety.co/d3653c6a1f7ddcb38c4ec45281880725/flightDeals/prices/{i}",
            json=new_data
        )
        print(response)

    i=i+1

print(sheet_data)