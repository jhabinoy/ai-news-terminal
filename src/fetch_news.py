import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

URL = "https://newsapi.org/v2/everything"


def get_financial_news(query="stock market", page_size=10):

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": API_KEY,
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("articles", [])


