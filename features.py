import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Find all paragraph tags <p> and join their text
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except:
        return "Error: Could not fetch or parse the URL."

import yake

def get_keywords(text):
    # Initialize the extractor
    extractor = yake.KeywordExtractor(n=1, top=10, features=None) # n=1 means single-word keywords
    keywords = extractor.extract_keywords(text)
    return [kw[0] for kw in keywords] # Returns a list of the top 10 keywords
