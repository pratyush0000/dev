import requests
import json

request = requests.get('https://api.stackexchange.com//2.3/answers?order=desc&sort=activity&site=stackoverflow')

print(request.status_code)
print(request.headers['content-type'])
print(request.json())

print('USER NAMES:')
for item in request.json()['items']:
    print(item['owner']['display_name'])