import json
import requests




def firt_try():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())

firt_try()