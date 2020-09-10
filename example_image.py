import requests
import json
import time

response = requests.get("http://www.google.com")
# domain = response.headers["domain"]
date = response.headers["Date"]

f = open("./result.txt", "a+")
f.write(date + "\n")
f.close()

print("pausing...")
time.sleep(60)