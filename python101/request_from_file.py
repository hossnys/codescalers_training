import requests

file = "/home/samir/test.txt"
f = open(file,"r")
for line in f.readlines():
    url = line.strip()
    if url:
        try:
            res = requests.get(url)
            print(url +" is ok")
        except:
            print(url+" is not reachable")