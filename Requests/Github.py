import requests

user = 'niozhxs'
password = 'abc'

r = requests.get('https://api.github.com/user', auth=(user, password))

print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)

print(r.text)

print(r.json())
