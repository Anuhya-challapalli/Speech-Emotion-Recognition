🎙️ Speech Emotion Recognition

Project Overview

Speech Emotion Recognition is a machine learning project that identifies emotions from human speech recordings. It analyzes audio features and predicts the emotion expressed in the voice.

The model classifies four emotions:

- Neutral
- Happy
- Sad
- Angry

🚀 Live Demo

Try the application here:

https://speech-emotion-recognition-bqvr8ysmolq3qbpfz7iuvn.streamlit.app/

Upload a WAV audio recording and click Detect Emotion to get a prediction.

🎯 Problem Statement

Understanding emotions in speech can help improve human-computer interaction. This project explores how machine learning can identify emotional patterns from voice recordings.

🛠️ Technologies Used

- Python
- Librosa
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

📂 Dataset

RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)

This project uses the speech portion of the RAVDESS dataset, containing recordings from different actors.

⚙️ Project Workflow

1. Download and load the speech dataset.
2. Extract audio features using MFCC (Mel-Frequency Cepstral Coefficients).
3. Calculate mean and standard deviation of the extracted features.
4. Train a Random Forest classification model.
5. Evaluate the model using accuracy and a confusion matrix.
6. Save the trained model.
7. Build a Streamlit application for audio uploads and emotion prediction.

📊 Model Performance

- Algorithm: Random Forest Classifier
- Number of MFCC features: 40
- Extracted statistical features: 80
- Test accuracy: 54.17%

Note: The model is an experimental baseline and may produce incorrect predictions, especially for voices or recording conditions different from the training dataset.

🖥️ Application Features

- Upload WAV audio recordings.
- Play the uploaded recording.
- Predict one of four emotions.
- Display the model's prediction confidence.

📁 Project Structure

Speech-Emotion-Recognition/
│
├── README.md
├── Speech_Emotion_Recognition.ipynb
├── app.py
├── config.json
├── requirements.txt
└── speech_emotion_model.pkl

▶️ How to Run Locally

1. Clone the repository:

git clone https://github.com/Anuhya-challapalli/Speech-Emotion-Recognition.git

2. Open the project folder:

cd Speech-Emotion-Recognition

3. Install the dependencies:

pip install -r requirements.txt

4. Run the application:

streamlit run app.py

🔮 Future Improvements

- Improve model accuracy.
- Support additional audio formats.
- Explore deep learning models.
- Improve performance on real-world voice recordings.

👩‍💻 Author

Anuhya Challapalli

GitHub: "Anuhya-challapalli" (https://github.com/Anuhya-challapalli)

---

⭐ If you find this project interesting, consider giving the repository a star!
