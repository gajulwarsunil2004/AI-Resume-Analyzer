import streamlit as st
import PyPDF2

from skills import skills_list

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type="pdf"
)

if uploaded_file:
    
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Resume Text")
    st.write(text[:1000])

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Skills Found")
    st.write(found_skills)
    
    st.subheader("Job Description Matching")

job_description = st.text_area(
    "Paste Job Description Here"
)

if job_description:

    jd_words = set(job_description.lower().split())

    resume_words = set(text.lower().split())

    match_score = (
        len(jd_words.intersection(resume_words))
        / len(jd_words)
    ) * 100

    st.success(
        f"Match Score: {match_score:.2f}%"
    )
    
   

missing_skills = []

for skill in skills_list:

    if (
        skill.lower() in job_description.lower()
        and
        skill.lower() not in text.lower()
    ):
        missing_skills.append(skill)

st.subheader("Missing Skills")
st.write(missing_skills)