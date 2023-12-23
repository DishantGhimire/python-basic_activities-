import requests
import json
responseApi=requests.get("https://api.kanye.rest")
if(responseApi.status_code==200):
    data=json.loads(responseApi.text)
    print(data['quote']);
else:
    print("Error fetching the api.");