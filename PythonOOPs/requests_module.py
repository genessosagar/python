import requests
import json

req = requests.get('http://ergast.com/api/f1/2004/1/results.json')

res = req.json()

# print(res)
for k,v in res.items():
    print(k,v)
# print(res['Races'])