import requests
from requests.exceptions import HTTPError

data={
    'userId':2,
    'name':"Manjusha",
    'email':"manju1234@gmail.com",
    'password':"23455"
}

url="http://localhost:8000/api/users"

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.json())
except HTTPError as http_err:
    print(response.json())
else:
    print("Success")

# res=requests.get(url)
# print(res.json())
# print(res.cookies)
# print(res.headers)
# print(res.status_code)

# res=requests.get('https://api.github.com/events')
# print(res.headers)
# print(res.status_code)


url="http://localhost:8000/users"

try:
    res=requests.post(url,json=data)
    print("response from try",res.json())

except HTTPError as http_err:
  if res.status_code==201:
    print(res.json())
    print("user is created successfully")
else:
    print(res.status_code)


    