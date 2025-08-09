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
        
# --- Feature 2: Flashcard Generation ---

# Initialize the models once to be efficient.
# This might take a moment the first time you run the app after adding this.
try:
    question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
    answer_extractor = pipeline("question-answering", model="deepset/roberta-base-squad2")
except Exception as e:
    print(f"Error loading models for flashcards: {e}")
    question_generator = None
    answer_extractor = None
def generate_flashcard(context):
    """
    Generates a question-answer pair (flashcard) from a given context/paragraph.
    Returns a dictionary with 'question' and 'answer'.
    """
    if not question_generator or not answer_extractor:
        return {"question": "Error", "answer": "Models could not be loaded."}
        
