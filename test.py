import requests
import json

r = requests.get('http://localhost:8000/').json()
print(r)
# Writing to sample.json
with open("sample.json", "w") as json_file:
    json.dump(r,json_file)


  