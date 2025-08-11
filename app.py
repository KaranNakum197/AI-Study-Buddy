import streamlit as st
from logic import get_summary, get_questions, get_text_from_pdf
from features import get_keywords, generate_flashcard, get_text_from_url

st.set_page_config(page_title="AI Study Buddy", page_icon="🤖")

st.title("AI Study Buddy 🤖")
st.write("Upload your notes or paste text to get summaries and practice questions.")

# Let user choose between text input and file upload
input_method = st.radio("Choose your input method:", ("Paste Text", "Upload a PDF"))

if input_method == "Paste Text":
    text_input = st.text_area("Paste your text here:", height=250)
    if text_input:
        st.subheader("Actions")
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                summary_result = get_summary(text_input)
                st.success("Summary:")
                st.write(summary_result)

        if st.button("Generate Practice Question"):
            with st.spinner("Thinking of a question..."):
                question_result = get_questions(text_input)
                st.success("Here's a question for you:")
                st.write(question_result)

elif input_method == "Upload a PDF":
    pdf_file = st.file_uploader("Upload your PDF file", type="pdf")
    if pdf_file is not None:
        with st.spinner("Reading PDF..."):
            pdf_text = get_text_from_pdf(pdf_file)

        st.text_area("Extracted Text from PDF:", pdf_text, height=250)
        st.subheader("Actions")
        if st.button("Generate Summary"):
             with st.spinner("Summarizing..."):
                summary_result = get_summary(pdf_text)
                st.success("Summary:")
                st.write(summary_result)

        if st.button("Generate Practice Question"):
            with st.spinner("Thinking of a question..."):
                question_result = get_questions(pdf_text)
                st.success("Here's a question for you:")
                st.write(question_result)

if st.button("Extract Keywords"):
    keywords_result = get_keywords(text_input)
    st.success("Keywords:")
    st.write(keywords_result)
