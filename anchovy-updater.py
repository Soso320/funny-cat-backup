# This program updates the anchovy link Database
# Modify the url and tags accordingly if you want

import requests
import json

url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=anchovy_(girls_und_panzer)+rating:safe&limit=3000&json=1"

r = requests.get(url)
s = r.json()
for i in range(999):
    image = (s[i]['file_url'])
    print(image)
    with open("resources/anchovy.txt", "a") as myfile:
        myfile.write(f"{image}\n")
