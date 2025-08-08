import yake
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# --- Feature 1: Keyword Extraction ---

def get_keywords(text):
    """
    Extracts the top 10 most important single-word keywords from a given text.
    """
    try:
        # Initialize the extractor for single-word keywords
        extractor = yake.KeywordExtractor(n=1, top=10, features=None)
        keywords = extractor.extract_keywords(text)
        # Return only the keyword text, not the score
        return [kw[0] for kw in keywords]
    except Exception as e:
        print(f"Could not extract keywords: {e}")
        return []
