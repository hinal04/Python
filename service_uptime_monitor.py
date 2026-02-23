import requests

try:
    response = requests.get("http://google.com")
    if response.status_code != 200:
        print("Service Down Alert!")
except Exception as e:
    print("Service Unreachable!")