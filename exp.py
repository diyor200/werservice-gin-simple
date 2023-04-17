import requests

payload = {"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": "49.99"}
url = "http://localhost:8080/albums"
response = requests.post(url=url, data=payload)
print(response.status_code)
print(response)