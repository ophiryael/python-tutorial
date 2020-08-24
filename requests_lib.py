import requests

# r = requests.get("https://api.github.com/events")
# print(r.encoding)
# print(r.status_code)
# print(r.text)
# print(r.json())

# r = requests.post("https://httpbin.org/post", data={"key": "value"})

# payload = {"key1": "value1", "key2": "value2", "key3": None}
# r = requests.get("https://httpbin.org/get", params=payload)
# print(r.url)

url = "https://httpbin.org/get"
headers = {"user-agent": "my-app/0.0.1"}
r = requests.get(url, headers=headers)
print(r.request.headers)
