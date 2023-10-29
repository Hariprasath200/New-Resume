from pathlib import Path
import streamlit as st

from PIL import Image


current_dir = Path (__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "hari.pdf"
profile_pic = current_dir / "assets" / "profile.jpg"
SOCIAL_MEDIA=current_dir/ "1.JPG" 


PAGE_TITLE = "My CV | HARI's Website"
PAGE_ICON = ":sparkles:"
NAME = "HARIPRASATH S"
DESCRIPTION = """ PYTHON FULL STACK DEVELOPER"""
int ("9360809634")
EMAIL = "haridhamo3@gmail.com"
SOCIAL_MEDIA = { 
    " 🔗LinkedIn": "https://www.linkedin.com/in/hariprasath-s-58144b191",
    "⚡Instagram": "https://instagram.com/hari_child?igshid=ZGUzMzM3NWJiOQ==",
    "💬WhatsApp":  "https://wa.me/qr/XVFHTPMOBNH4B1",
    "📄Certificate verification": "https://coursera.org/share/9dfd3ec817e80e7fb62663055e85e620"
    
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
with open(css_file)as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Dowload Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )    
    st.write("📩", EMAIL)
    st.text(9360809634)
 

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Hard Skills")
st.write(
"""
- 👨🏻‍💻 Programming : Python.
- 🟢 Frameworks  : Django,Streamlit.
- ⚪ Frontend    : Html,Css,Angularjs.
- ⚪ DataBase    : Sql.
- ⚪ Version Control : Git,GitHub.         
- 🔴 Basic     : MS Office 
"""
)
st.write("#")
st.subheader("CERTIFICATES")
st.write(
    """
- Coursera (Google)
     - Crash Course On Python.   
       - This Course Provided By Google.


"""

    """
- UDEMY Python Course.
     - Complete Python 2023 For Absolute Beginners.   
       


"""

"""

    
    
- Certificate of Participation.
     - Advances in Image Processing using Python.


"""

"""
- Domestic Data Entry
    
"""

"""
-  Master Class
      
     -  Build a Chatbot using Artificial Intelligence and    Machine Learning.
"""


"""
-  Master Class
     -  Upskill for the Post-Recession Software Engineering World
    """
)

st.write("#")
st.subheader("EDUCATION")
st.write(
    """
  🏫 AMC ENGINEERING COLLEGE
     - 🎓 Master of Computer Application - 🎓 2024.

    
    """
        
 """
    🏫SHANMUGA INDUSTRIES ARTS AND SCIENCE COLLEGE
     - 👨🏻‍🎓BSc,COMPUTER SCIENCE - 🎓 2022
     - 80%
    """
    
    """
    🏫SRI.VDS JAIN HIGHER SECONDARY SCHOOL
     - +2
     - 2019
     - 52%
    """

    """
    🏫SRI.VDS JAIN HIGHER SECONDARY SCHOOL
     - 10TH
     - 2017
     - 60%
    """
)
st.write("#")
st.subheader("PERSONAL DETAILS")
st.write(
    """

    -🗓DATE OF BIRTH       :    20/04/2002
"""
"""
-👨🏻FATHER NAME        :    SRIKANTH K
"""
"""
 -🧕🏻MOTHER NAME      :    TAMILARASI S

"""
)



st.write("#")
st.subheader("PROJECT")
st.write(
    """
    -🌐CREATED OWN RESUME WEBSITE (Using Python + Streamlit)  

    """

)

st.write("#")
st.subheader("INTERESTS")
st.write(
"""
   -🧑🏻‍💻PYTHON FULL STACK DEVELOPER
     

"""

)

st.write("#")
st.subheader("OBJECTIVES")
st.write(
"""
-💯To be with a reputed organization where I can explore my skills and
abilities to improve my self as well as company

"""
)