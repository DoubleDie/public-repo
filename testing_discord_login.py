import requests
url = 'https://discord.com/api/v9/auth/login'
data = {'login': "hnumrich@gmail.com", 'password': "BigBalls12", 'undelete': 'false', 'gift_code_sku_id': 'null'}
response = requests.post(url, json=data)
print(response)
