import requests

url = "https://toplearn.com/"

response = requests.get(url, timeout=2)

print(response.status_code)
print(response.url)
print(response.text)
print(response.cookies)
