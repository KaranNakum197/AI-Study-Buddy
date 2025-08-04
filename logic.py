from transformers import pipeline
import PyPDF2

# Initialize the AI models once when the script starts
# This avoids reloading them every time a button is clicked
summarizer = pipeline("summarization", model="t5-small")
question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def get_summary(text_to_summarize):
    """Generates a summary for the given text."""
    # The model works best on text up to a certain length
    summary = summarizer(text_to_summarize, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def get_questions(context):
    """Generates a practice question for the given context."""
    questions = question_generator(context)
    return questions[0]['generated_text']

def get_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
