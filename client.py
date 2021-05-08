import requests
import sys

url = "http://127.0.0.1:7777"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
if len(sys.argv) < 3:
    print("Usage: python client.py <endpoint> <post_data>")

endpoint = sys.argv[1]
data = sys.argv[2]

res = requests.post("{}/{}".format(url, endpoint), data=data, headers=headers)
print(res.text)

