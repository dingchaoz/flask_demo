import requests

# URL
url = 'http://localhost:8080/api'

# Change the value of experience that you want to test
r = requests.post(url, json={'exp': 1800, })
print(r.json())
