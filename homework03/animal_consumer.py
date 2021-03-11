import requests


response1 = requests.get(url="http://localhost:5019/animals")
response2 = requests.get(url="http://localhost:5019/animals/head/bunny")
response3 = requests.get(url="http://localhost:5019/animals/legs/6")

print('Response 1:')
print(response1.status_code)
print(response1.json())
print(response1.headers)

print('Response 2:')
print(response2.status_code)
print(response2.json())
print(response2.headers)

print('Response 3:')
print(response3.status_code)
print(response3.json())
print(response3.headers)