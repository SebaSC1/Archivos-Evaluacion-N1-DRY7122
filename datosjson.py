import json
import yaml

with open('myfile.json','r') as datosjson:
    ourjson = json.load(datosjson)
print (ourjson)
