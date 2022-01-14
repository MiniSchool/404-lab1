import requests

page = requests.get('https://github.com/MiniSchool/404-lab1/blob/main/lab1.py')

for line in page:
    print(line)
