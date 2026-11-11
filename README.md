Speech Emotion Recognition Using Machine Learning

Project Overview

Speech Emotion Recognition (SER) is a machine learning project that predicts emotions from human speech recordings using audio signal processing and classification techniques.

This project uses MFCC (Mel-Frequency Cepstral Coefficients) features to extract useful information from speech signals and a Random Forest Classifier to predict emotions.

Emotions Detected

- Neutral
- Happy
- Sad
- Angry

Technologies Used

- Python
- Google Colab
- Librosa
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

Dataset

This project uses the RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song) dataset.

Only speech recordings belonging to four selected emotion categories are used.

Dataset source: https://zenodo.org/records/11063852

Project Workflow

1. Download and load the speech dataset.
2. Select four emotion categories.
3. Extract 40 MFCC coefficients from each audio recording.
4. Calculate mean and standard deviation to create 80 features.
5. Split the dataset into training and testing sets using actor-based splitting.
6. Train a Random Forest Classifier.
7. Evaluate the model using accuracy, classification report and confusion matrix.
8. Predict emotions from audio recordings.

Machine Learning Algorithm

Random Forest Classifier

Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Project Files

- "Speech_Emotion_Recognition.ipynb" – Complete project implementation.
- "speech_emotion_model.pkl" – Trained machine learning model.
- "config.json" – Model configuration and emotion labels.

How to Run

1. Open Google Colab.
2. Upload the project notebook.
3. Install the required libraries.
4. Download and extract the RAVDESS dataset.
5. Run the notebook cells in order.
6. Train the model and test emotion predictions.

Limitations

- Emotion predictions are not always accurate.
- Voice characteristics differ between individuals.
- The model is trained on a limited selection of emotions.
- Predictions should not be treated as definitive assessments of a person's feelings.

Author

Anuhya Challapalli

Project Type

Machine Learning | Data Science | Audio Processing
