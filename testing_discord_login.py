import requests
url = 'https://discord.com/api/v9/auth/login'
data = {'login': "hnumrich@gmail.com", 'password': "BigFatBalls12", 'undelete': 'false', 'login_source': 'null'}
response = requests.post(url, json=data)
print(response)
