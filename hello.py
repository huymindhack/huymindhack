import requests
from PIL import Image
import streamlit as st

st.set_page_config(page_title="My First Web App Using Streamlit", page_icon=":tada:", layout="wide")

image_login = Image.open("register-form-validator.png")
image_modal = Image.open("create-modal.png")
image_intro = Image.open("pexels-sebastiaan-stam-1097456.jpg")



def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
    
with st.container():
    left_columns, right_columns = st.columns(2)

    with left_columns:
        st.subheader("Hello, I'm Huy")
        st.title("A Pupil at PTIT")
        st.write("I am interested in coding web and now i am a bit curious to build a web by using streamlit in python")
        st.write("[To know more about me](https://www.facebook.com/profile.php?id=100070906924722)")

    with right_columns:
        st.image(image_intro)

with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(image_login)
    with text_column:
        st.subheader("Login Form")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_modal)
    with text_column:
        st.subheader("Create Modal")

with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
<form action="https://formsubmit.co/huyarkadata@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Enter your name" required>
     <input type="email" name="email" placeholder="Enter your email" required>
     <textarea name="message" placeholder="Enter your message here"></textarea>
     <button type="submit">Send</button>
</form>"""

    left_columns, right_columns = st.columns(2)

    with left_columns:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_columns:
        st.empty()
