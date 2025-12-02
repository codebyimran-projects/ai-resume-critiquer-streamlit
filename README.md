# AI Resume Critiquer

This project is a Streamlit-based web application that analyzes resumes using the OpenAI API. Users can upload their resume as a PDF or DOCX file, and the application extracts the text and generates detailed AI-powered feedback to improve formatting, structure, and content quality.

## Features
- Upload PDF or DOCX resumes
- Extract text from uploaded files
- Use OpenAI LLM to generate detailed resume feedback
- Clean and simple Streamlit user interface
- Error handling for empty or unreadable files

## Technologies Used
- Python
- Streamlit
- PyPDF2
- python-docx
- OpenAI API (new client version)
- dotenv for environment variables

## Folder Structure
```

project/
│── main.py
│── requirements.txt
│── .env
│── README.md

```

## Setup Instructions

### 1. Install Dependencies
```

pip install Dependencies Names

```

### 2. Add Your OpenAI API Key  
Create a `.env` file in the project directory:

```

OPENAI_API_KEY=your_api_key_here

```

### 3. Run the Application
```

py -m streamlit run main.py

```

## Requirements File
Ensure your `requirements.txt` includes:

```

streamlit
openai>=1.0.0
python-dotenv
PyPDF2
python-docx

```

## How it Works
1. The user uploads a resume file.
2. The system extracts text from PDF or DOCX.
3. The text is passed to an OpenAI model.
4. The AI generates structured feedback for improvements.
5. The results are displayed in the Streamlit interface.

## Usage
Designed for developers, students, and professionals who want AI-generated guidance on improving their resumes.

Just tell me.
