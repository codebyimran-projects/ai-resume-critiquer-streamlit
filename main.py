import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI as openai
import io
from PyPDF2 import PdfReader
load_dotenv()


st.set_page_config(page_title="AI Resume Critiquer", page_icon=":memo:", layout="centered")
st.title("AI Resume Critiquer")
st.write("Upload your resume and get AI-generated feedback to improve it!")
uploaded_file = st.file_uploader("Choose your resume file (PDF or DOCX)", type=["pdf", "docx"])

analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(file):

    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
   if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
   
   return uploaded_file.getvalue().decode("utf-8")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if analyze_button and uploaded_file is not None:
    try:
        with st.spinner("Analyzing your resume..."):
            file_content = extract_text_from_file(uploaded_file)
            if not file_content.strip():
                st.error("The uploaded file is empty or could not be read.")
                st.stop()
            prompt = f"Please provide detailed feedback on the following resume:\n\n{file_content}\n\nFeedback:"
            client = openai(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert career coach."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7,
            )
            st.markdown("### Resume Analysis Complete!")
            feedback = response.choices[0].message.content
            st.markdown(feedback)
       
    except Exception as e:
        st.error(f"An error occurred: {e}")
     