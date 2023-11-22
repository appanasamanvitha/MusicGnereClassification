import streamlit as st
import base64

def set_bg_hack(main_bg):
    # Set the background image file path and extension
    main_bg_ext = "jpg"

    # Read the image file and encode it in base64
    gif_data = open(main_bg, "rb").read()
    image_base64 = base64.b64encode(gif_data).decode()

    # Set the background using custom CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{image_base64});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image using your function
set_bg_hack("C:\\Users\\admin\\Downloads\\nathan-fertig-IW5Bm4rB9OA-unsplash.jpg")

# Your Streamlit app content
st.title("MUSIC GENRE CLASSIFICATION")
st.write("NOTES WEAVES MAGIC!!!")