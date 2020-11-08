import requests
import json

while True:
    formatted_input = input("Enter string\n>")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox'}
    data = {'text': formatted_input}

    r = requests.post('https://politeness.cornell.edu/score-politeness', headers=headers, data=data)
    s = r.json()

    confidence = (s['confidence'])
    label = (s['label'])

    print(f"Label: {label}\nConfidence: {confidence}")
