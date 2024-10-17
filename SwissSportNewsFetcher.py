import requests
from sys import argv 

BASE_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "646116081e08424fb4e952f3fb88821a"

def fetch_news_by_category(category):
    params = {
        "category": category,
        "sortBy": "top",
        "country": "ch",  # Switzerland
        "apiKey": API_KEY
    }
    return _retrieve_articles(params)


def fetch_news_by_category(category):
    params = {
        "category": category,
        "sortBy": "top",
        "country": "ch",  # Switzerland
        "apiKey": API_KEY
    }
    return _retrieve_articles(params)

def fetch_news_by_search_term(search_term):
    params = {
        "q": search_term,
        "sortBy": "top",
        "country": "ch",  # Switzerland
        "apiKey": API_KEY
    }
    return _retrieve_articles(params)

def _retrieve_articles(parameters):
    response = requests.get(BASE_URL, params=parameters)

    # Validate response
    if response.status_code != 200:
        print(f"Error fetching articles: {response.status_code}")
        return

    news_articles = response.json().get('articles', [])
    articles_list = []
        
    for item in news_articles:
        articles_list.append({"headline": item["title"], "link": item["url"]})

    for article in articles_list:
        print(article['headline'])
        print(article['link'])
        print('')

def display_sources_by_category(category):
    source_url = 'https://newsapi.org/v2/top-headlines/sources'
    params = {
        "category": category,
        "language": "de",  # Swiss German
        "apiKey": API_KEY
    }

    response = requests.get(source_url, params=params)

    # Validate response
    if response.status_code != 200:
        print(f"Error fetching sources: {response.status_code}")
        return

    sources_data = response.json().get('sources', [])

    for source in sources_data:
        print(source['name'])
        print(source['url'])

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script_name.py [category]")
        sys.exit(1)
    
    print(f"Fetching news for category: {argv[1]}...\n")
    fetch_news_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines")

