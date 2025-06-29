import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def google_search_linkedin(query, num_results=10):
    print("🔍 Running real Google LinkedIn search...")

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results,
    }

    search_url = "https://serpapi.com/search"
    response = requests.get(search_url, params=params)
    results = response.json()

    candidates = []

    for result in results.get("organic_results", []):
        title = result.get("title", "")
        link = result.get("link", "")
        snippet = result.get("snippet", "")

        if "linkedin.com/in" in link:
            candidates.append({
                "name": title.split(" - ")[0],
                "linkedin_url": link,
                "snippet": snippet
            })

    return candidates
