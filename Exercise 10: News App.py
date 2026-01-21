import requests
import pandas as pd

query = input("What kind of news do you want? ")
url = f"https://newsapi.org/v2/everything"
params = {
    "apiKey": "75972c1193984f8d9dd7250d55ce4bcb",
    "q": query,
    "language": "en",
    "from": "2025-12-21",
    "sortBy": "publishedAt",
}
r = requests.get(url, params=params)
r.raise_for_status()
j = r.json()

frame = []
for article in j.get("articles", []):

    data = {
        # "id": article["source"]["id"], # majorly empty
        "publishedAt": article["publishedAt"],
        "name": article["source"]["name"],
        "author": article["author"],
        "title": article["title"],
        "description": article["description"],
        "url": article["url"],
        # "content": article["content"], # click the link in the file temp.xlsx for full article
    }
    frame.append(data)

df = pd.DataFrame(frame)
df.to_excel("temp.xlsx", index=False)
print(df.head())
