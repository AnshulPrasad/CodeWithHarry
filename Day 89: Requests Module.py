import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userId": 1,
    "body": "bar",
    "title": "foo",
}
headers = {
    "Content-type": "application/json;charset=UTF-8",
}
response = requests.post(url, headers=headers, json=data)
print(response.text)


url = "https://www.nytimes.com/international/"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
