import requests

page = requests.get('http://google.com')

for line in page:
    print(line)
