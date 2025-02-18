import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

def generate_cover_letter(full_name, email_address, phone_number, job_title, company_name, skills):
    """
    Generate a professional cover letter using Google Gemini API with enforced formatting.
    """
    if not all([full_name, email_address, phone_number, job_title, company_name, skills]):
        return "❌ Error: Missing required inputs for cover letter generation."

    prompt = f"""
    You are a professional cover letter writer. Write a **fully formatted cover letter** that uses the following **real candidate details** (DO NOT use placeholders).

    **Candidate Details:**
    - **Full Name:** {full_name.title()}
    - **Email Address:** {email_address.lower()}
    - **Phone Number:** {phone_number}
    - **Job Title Applying For:** {job_title}
    - **Company Name:** {company_name.title()}
    - **Skills:** {skills}

    **Cover Letter Format:**
    - Addressed to "**Dear Hiring Manager,**"
    - Introduction that expresses interest in the `{job_title}` role at `{company_name}`.
    - **Incorporate skills** `{skills}` into the body of the letter.
    - Show how the candidate’s experience makes them a great fit.
    - Closing statement that expresses enthusiasm and willingness for an interview.
    - **No placeholders like [Your Name] or [Your Address]! Use only provided details!**

    **Generate the full final version of the cover letter in plain text.**
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if response else "❌ Error: AI failed to generate cover letter."
    except Exception as e:
        return f"❌ API Error: {str(e)}"