import streamlit as st
from resume_generator import generate_resume
from cover_letter_generator import generate_cover_letter
import tempfile

st.title("🚀 AI-Powered Resume & Cover Letter Generator (Google Gemini)")

# === Resume Generator Section ===
st.header("📄 Generate Your Resume")

full_name = st.text_input("Full Name")
email_address = st.text_input("Email Address")
phone_number = st.text_input("Phone Number")
address = st.text_input("Address")
summary = st.text_area("Professional Summary")
experience = st.text_area("Work Experience (List jobs, roles, achievements)")
skills = st.text_area("Skills (Technical & Soft skills)")
education = st.text_input("Education (Degree & University)")
certifications = st.text_area("Certifications (Optional)")
awards = st.text_area("Awards & Recognitions (Optional)")

if st.button("Generate Resume"):
    if full_name and email_address and summary and experience:
        resume = generate_resume(full_name, address, phone_number, email_address, summary, experience, skills, education, certifications, awards)

        # Display Resume in Streamlit Properly
        st.markdown("## ✅ Generated Resume:")
        st.markdown(f"```\n{resume}\n```", unsafe_allow_html=False)  # ✅ Fixed Markdown rendering for readability

        # Function to Save Resume
        def save_resume(content, filename="Resume.txt"):
            """Save resume as a text file."""
            with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as f:
                f.write(content)
                return f.name

        resume_file_path = save_resume(resume)

        with open(resume_file_path, "rb") as file:
            st.download_button(label="📥 Download Resume", data=file, file_name="Resume.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please fill in at least Name, Email, Summary, and Experience.")

# === Cover Letter Generator Section ===
st.header("📝 Generate Your Cover Letter")

job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")

if st.button("Generate Cover Letter"):
    if full_name and email_address and phone_number and job_title and company_name and skills:
        cover_letter = generate_cover_letter(full_name, email_address, phone_number, job_title, company_name, skills)

        # Properly formatted Markdown Output
        formatted_cover_letter = f"""
        **{full_name}**  
        **{email_address}**  
        **{phone_number}**  

        {cover_letter}  
        """

        st.markdown("## ✅ Generated Cover Letter:")
        st.markdown(formatted_cover_letter, unsafe_allow_html=False)  # ✅ Correct Markdown formatting

        # Function to Save Cover Letter
        def save_cover_letter(content, filename="Cover_Letter.txt"):
            """Save cover letter as a text file."""
            with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as f:
                f.write(content)
                return f.name

        cover_letter_file_path = save_cover_letter(cover_letter)

        with open(cover_letter_file_path, "rb") as file:
            st.download_button(label="📥 Download Cover Letter", data=file, file_name="Cover_Letter.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please enter Full Name, Email, Phone Number, Job Title, Company Name, and Skills.")