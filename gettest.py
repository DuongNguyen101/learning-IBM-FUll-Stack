import requests
import json
page=requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
x=page.json()
print(x[0])
print(json.dumps(x, indent=2))
