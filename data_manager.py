import requests

class DataManager:
    def get_rows(self):
        response=requests.get("https://api.sheety.co/d3653c6a1f7ddcb38c4ec45281880725/flightDeals/prices")
        return response.json()


    def update_codes(self, id):
        payload={"prices"[id]["iataCode"]: "TESTING"
        }
        response=requests.put(url=f"https://api.sheety.co/d3653c6a1f7ddcb38c4ec45281880725/flightDeals/prices/{id}", json=payload)
        print(response)



