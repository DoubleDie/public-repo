import requests
url = 'https://discord.com/api/v9/auth/login'
data = {'login': "h#############com", 'password': "B#######2", 'undelete': 'false', 'gift_code_sku_id': 'null'}
response = requests.post(url, json=data)
print(response)
