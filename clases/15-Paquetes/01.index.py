import requests
import json

mi_data = requests.get('https://jsonplaceholder.typicode.com/users')
print(mi_data)
mi_lista = mi_data.json()
print(type(mi_lista))

for user in mi_lista:
    print('*'*100)
    # print(user)
    print(user["name"])
    
json_mylist = json.dumps(mi_lista, separators=(',', ':'))    
print(json_mylist)

# for user in json_mylist:
#     print('*'*100)
#     print(user)
    # print(user["name"])


