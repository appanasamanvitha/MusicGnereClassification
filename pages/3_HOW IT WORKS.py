import streamlit as st
import numpy as np
import pickle
import librosa
from pydub import AudioSegment

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
set_bg_hack("C:\\Users\\admin\\Desktop\\project\\pp2.jpg")






# Load your pre-trained model
clf = pickle.load(open('C:\\ml model dep\\trainingmodel.sav', 'rb'))
scaler = pickle.load(open('C:\\ml model dep\\models.p', 'rb'))
lookup_genre_name = scaler['lgn']

def getmetadata(filename):
    y, sr = librosa.load(filename)
    
    
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]


    chroma_stft = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))

    
    rmse = np.mean(librosa.feature.rms(y=y))

    
    spec_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

   
    spec_bw = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))

  
    spec_rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))

   
    zero_crossing = np.mean(librosa.feature.zero_crossing_rate(y))

   
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20), axis=1)

    
    metadata_dict = {
        'tempo': tempo,
        'chroma_stft': chroma_stft,
        'rmse': rmse,
        'spectral_centroid': spec_centroid,
        'spectral_bandwidth': spec_bw,
        'rolloff': spec_rolloff,
        'zero_crossing_rates': zero_crossing
    }

    for i in range(1, 21):
        metadata_dict[f'mfcc{i}'] = mfcc[i-1]

    return list(metadata_dict.values())
    # Your existing getmetadata function here

def musicpred(input_data):
    d1 = np.array(input_data)
    data1 = scaler['norma'].transform([d1])
    genre_prediction = clf.predict(data1)
    return lookup_genre_name[genre_prediction[0]]

def main():
    st.title("Music Genre Classification")

    # Create a file uploader using st.file_uploader
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        audio_data = getmetadata(uploaded_file)
        st.audio(uploaded_file, format="audio/wav")

        # Code for prediction
        predicted_genre = ""
        if st.button('Predict'):
            if audio_data is not None:
                predicted_genre = musicpred(audio_data)
                

            else:
                st.warning("Please upload an audio file before predicting.")

        st.success(f"Predicted Genre: {predicted_genre}")

if __name__ == '__main__':
    main()




