from os import link
import requests
import json
import random
import re
data = requests.get("https://api.imgflip.com/get_memes")
data = (str(data.content))
links = []
for i in re.finditer(r"https:[\a-zA-Z.]+.jpg",data):
    x,y = (i.span())
    links.append(data[x:y].replace("\\",""))
random.shuffle(links)
for i in (links[:10]):
    print(i)