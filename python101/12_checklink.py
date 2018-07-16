# WHAT DOES IT MEAN TO HAVE A GOOD LINK?
# 200 on GET REQUEST?


import requests
urls = ["http://www.google.com", "http://www.yahoo.com" , "http://www.codescalers.com"]
for url in urls:
    res = requests.get(url)
    if res.status_code == 200:
        print(url+": is ok")
