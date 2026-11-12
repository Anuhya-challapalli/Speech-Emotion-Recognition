import streamlit as st
import librosa
import numpy as np
import joblib
from io import BytesIO

st.set_page_config(
    page_title="Speech Emotion Recognition",
    page_icon="🎙️"
)

st.title("🎙️ Speech Emotion Recognition")
st.write("Upload a voice recording to predict its emotion.")

@st.cache_resource
def load_model():
    return joblib.load("speech_emotion_model.pkl")

model = load_model()

audio_file = st.file_uploader(
    "Upload an audio file",
    type=["wav"]
)

if audio_file is not None:
    st.audio(audio_file, format="audio/wav")

    if st.button("Detect Emotion"):
        try:
            audio, sr = librosa.load(
                BytesIO(audio_file.getvalue()),
                sr=16000
            )

            mfcc = librosa.feature.mfcc(
                y=audio,
                sr=sr,
                n_mfcc=40
            )

            mfcc_mean = np.mean(mfcc, axis=1)
            mfcc_std = np.std(mfcc, axis=1)

            features = np.concatenate(
                [mfcc_mean, mfcc_std]
            ).reshape(1, -1)

            prediction = model.predict(features)[0]
            probabilities = model.predict_proba(features)[0]
            confidence = np.max(probabilities) * 100

            st.success(f"Predicted Emotion: {prediction}")
            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

            st.caption(
                "This is an experimental prediction, "
                "not a reliable assessment of someone's actual feelings."
            )

        except Exception as e:
            st.error(f"Error processing audio: {e}")
