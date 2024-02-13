import requests

api_key = "44c3e80e4895cf2a7c25cc15be402466"
url = "https://api.openweathermap.org/data/2.5/weather?q=tehran&appid="

response = requests.get(url + api_key, timeout=2)

print(response.status_code)
print(response.url)
print(response.text)
print(response.cookies)
