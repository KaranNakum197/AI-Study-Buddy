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

    try:
        # 1. Generate a question from the context
        generated_question = question_generator(context)[0]['generated_text']

        # 2. Use the generated question and original context to find the answer
        qa_input = {
            'question': generated_question,
            'context': context
        }
        result = answer_extractor(qa_input)
        
        return {"question": generated_question, "answer": result['answer']}
    except Exception as e:
        print(f"Could not generate flashcard: {e}")
        return {"question": "Could not generate question.", "answer": "An error occurred."}
# --- Feature 3: URL Text Extraction ---

def get_text_from_url(url):
    """
    Fetches a webpage URL and extracts all paragraph text.
    """
    try:
        # Add a header to pretend we are a browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(url, headers=headers, timeout=10)
        
        # Check if the request was successful
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            # Find all paragraph tags <p> and join their text
            paragraphs = soup.find_all('p')
            text = ' '.join([p.get_text() for p in paragraphs])
            return text
        else:
            return f"Error: Could not fetch URL. Status code: {page.status_code}"
    except Exception as e:
        return f"Error: An exception occurred while fetching the URL: {e}"
        
