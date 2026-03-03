import requests

def search_grants(query: str, api_key: str):
    url = f"https://serpapi.com/search?q={query}+grants+2026&api_key={api_key}"
    results = requests.get(url).json()

    found_money = []
    for item in results.get('organic_results', []):
        if "deadline" in item.get('snippet', '').lower():
            found_money.append({
                "source": item['title'],
                "link": item['link'],
                "intelligence": "High Priority: Potential Win found by BirdDog"
            })
    return found_money
