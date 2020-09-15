import requests
import json
import time

response = requests.get("https://www.google.com")
# domain = response.headers["domain"]
data = response.headers

print(data)
time.sleep(60)