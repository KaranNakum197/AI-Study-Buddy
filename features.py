
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
    
