import streamlit as st 
import google.generativeai as genai 
import os
import PyPDF2 as pdf

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("Google_Api_Key"))

def get_response(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-pro')

    input_prompt= f"""
        Hey Act Like a skilled or very experience ATS(Application Tracking System)
        with a deep understanding of tech field,software engineering,data science ,data analyst
        and big data engineer. Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very competitive and you should provide 
        best assistance for improving thr resumes. Assign the percentage Matching based 
        on Jd and
        the missing keywords with high accuracy
        resume:{resume_text}
        description:{jd_text}

        I want the response in one single string having the structure
        {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
    """

    response = model.generate_content(input_prompt)
    return response.text 

def extract_pdf_txt(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""

    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    
    return text


st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

st.title("AI ATS System")
st.text("Increase your Resume shortlisting and matching chances in few clicks")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload your resume/cv", type="pdf", help="please upload pdf only")

submit = st.button("Submit")

if submit:
    with st.spinner("Please wait analysing the resume/cv..."):
        if uploaded_file is not None and jd:
            resume_text = extract_pdf_txt(uploaded_file)
            response = get_response(resume_text, jd)
            st.subheader(response)
        else:
            st.error("Please upload a PDF resume and paste the job description")
