import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API Key is Loaded Correctly
if not API_KEY:
    print("❌ ERROR: GEMINI_API_KEY not found. Please check your .env file.")
    exit()

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

def generate_resume(full_name, address, phone, email, summary, experience, skills, education, certifications, awards):
    """
    Calls Google Gemini API to generate a structured resume.
    """
    prompt = f"""
    You are an expert resume writer. Generate a **fully formatted, professional resume** using Markdown.
    Use proper **headings, bullet points, and spacing** for a well-structured document.
    Ensure the resume looks **ATS-friendly** and **well-organized**.

    ---
    **Candidate Details:**
    - **Name:** {full_name}
    - **Address:** {address}
    - **Phone:** {phone}
    - **Email:** {email}

    ---
    **Professional Summary:**
    {summary}

    ---
    **Work Experience:**
    {experience}

    ---
    **Skills:**
    {skills}

    ---
    **Education:**
    {education}

    ---
    **Certifications:**
    {certifications}

    ---
    **Awards and Recognition:**
    {awards}

    Generate the **final resume output** directly, without adding placeholders like [Your Name] or [Your Address].
    """

    try:
        # Call Google Gemini AI API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        # Handle the API response
        if response and response.text:
            return response.text.strip()
        else:
            return "❌ Error: AI failed to generate the resume. Please try again."
    
    except Exception as e:
        return f"❌ API Error: {str(e)}"

# ✅ Test the Function When Running the Script Directly
if __name__ == "__main__":
    print("🔹 Testing Resume Generator...")

    # Test Data
    test_resume = generate_resume(
        full_name="John Doe",
        address="123 Main St, New York, NY",
        phone="123-456-7890",
        email="johndoe@example.com",
        summary="Software Engineer with 5 years of experience in AI and cloud computing.",
        experience="Worked at Google, developed AI models and cloud solutions.",
        skills="Python, TensorFlow, AWS, JavaScript",
        education="B.Tech in Computer Science, MIT",
        certifications="AWS Certified, TensorFlow Developer",
        awards="Best Developer Award at Google"
    )

    print("\n✅ Generated Resume:\n")
    print(test_resume)