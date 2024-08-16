# JobMatcher AI

**JobMatcher AI** is an AI-powered tool designed to analyze and optimize resumes against job descriptions, enhancing job application effectiveness.

## Features

- **Resume Analysis:** AI-driven evaluation of resumes.
- **Match Percentage:** Shows how well the resume matches the job description.
- **Keyword Identification:** Highlights missing skills and keywords.
- **Profile Summary:** Provides suggestions for improving resumes.

## Technologies Used

- **Streamlit**: For building the web application.
- **Google Generative AI**: For generating content and analyzing resumes.
- **PyPDF2**: For extracting text from PDF resumes.
- **Python**: For backend logic.

## Deployment

The application is deployed and accessible at [JobMatcher AI](https://jobmatcher-ai.streamlit.app)

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/JobMatcher-AI.git
   cd JobMatcher-AI

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**
    Create a .env file in the root directory and add your Google API key:

   ```bash
   Google_Api_Key=your_google_api_key_here

5. **Run the Streamlit Application**

   ```bash
   streamlit run app.py

### Usage

1. Upload your resume in PDF format.
2. Paste the job description.
3. Click "Submit" to get the evaluation results.
