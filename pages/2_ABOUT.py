import streamlit as st
import base64

# Function to set a background image
def set_bg_hack(main_bg):
    main_bg_ext = "png"
    
    image_data = open(main_bg, "rb").read()
    image_base64 = base64.b64encode(image_data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{image_base64});
            background-size: cover;
            font-family: 'CustomFont', sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image
set_bg_hack("C:\\Users\\admin\\Desktop\\project\\POP- METAL - JAzz.png")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
about_url = "https://www.musicianwave.com/top-music-genres/"

# Create an "About" button

# Streamlit content
with st.container():
    st.subheader("About")
    st.write("----")
    st.write(
            """
            Music genre classification involves the automatic categorization of music tracks into predefined genre labels, such as rock, pop, jazz, or hip-hop. This task is crucial for various applications, including music recommendation systems, content organization, and music streaming platforms.
          """
        )
    
if st.button("Read More"):
    # Redirect to the "About" page when the button is clicked
    st.markdown(f"Click [here]({about_url}) to learn more about music genre's.")
