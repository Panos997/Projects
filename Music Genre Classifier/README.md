# Music Genre Classification Web App

## Overview

Music Genre Classification Web App is a machine learning web application that predicts the genre of an uploaded audio file.

The user uploads a music file, the application extracts audio features from the first 10 seconds, scales those features using a saved scaler, and then uses a trained machine learning model to predict the most likely music genres.

The app returns the **top 3 predicted genres** with their probabilities.

The project is built with Flask, Librosa, Scikit-learn, NumPy, and Joblib.

---

# Project Goal

The goal of this project is to classify music audio files into different genres using machine learning.

The application focuses on:

- audio feature extraction
- music genre prediction
- probability-based classification
- web-based user interaction
- loading a pre-trained machine learning model
- returning the top genre predictions through an API response

This is not a deep learning project.  
It uses a trained Scikit-learn model saved as a `.pkl` file.

---

# What the Application Does

The application allows a user to upload an audio file.

Then it:

1. saves the uploaded audio temporarily
2. loads the first 10 seconds of the audio
3. extracts audio features using Librosa
4. scales the features using a saved `StandardScaler`
5. sends the processed features to a trained Random Forest model
6. calculates prediction probabilities
7. returns the top 3 most likely genres as JSON

---

# Output Example

Example response:

```json
[
  {
    "genre": "ROCK",
    "probability": 42.35
  },
  {
    "genre": "METAL",
    "probability": 31.18
  },
  {
    "genre": "DISCO",
    "probability": 12.44
  }
]
```

The output includes:

- predicted genre name
- probability percentage

---

# Supported Genres

The trained label encoder contains the following music genres:

```text
blues
classical
country
disco
hiphop
jazz
metal
pop
reggae
rock
```

The application returns the predicted genres in uppercase.

---

# How It Works

The workflow of the application is:

```text
User uploads audio file
        ↓
Audio is temporarily saved
        ↓
Librosa loads first 10 seconds
        ↓
Audio features are extracted
        ↓
Features are scaled
        ↓
Random Forest model predicts probabilities
        ↓
Top 3 genres are selected
        ↓
Results are returned as JSON
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web application and API routes |
| Librosa | Audio loading and feature extraction |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning model, scaler, label encoder |
| Joblib | Loading saved `.pkl` files |
| Matplotlib | Listed dependency, useful for visualization |
| SoundFile | Audio file support |
| Gunicorn | Production server deployment |

The required libraries are listed in `requirements.txt`: :contentReference[oaicite:0]{index=0}

```text
flask
librosa
numpy
joblib
scikit-learn
matplotlib
soundfile
gunicorn
```

---

# Project Structure

```text
Music Genre Classification Web App/
│
├── app.py
├── music_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
└── templates/
    └── index.html
```

---

# File Explanation

## `app.py`

Main Flask application file. :contentReference[oaicite:1]{index=1}

It contains:

- Flask app initialization
- model loading
- scaler loading
- label encoder loading
- audio feature extraction function
- homepage route
- prediction API route
- temporary audio file handling
- JSON response generation

---

## `music_model.pkl`

Saved trained machine learning model.

The loaded model is a:

```text
RandomForestClassifier
```

This model receives the extracted and scaled audio features and predicts music genre probabilities.

---

## `scaler.pkl`

Saved feature scaler.

The loaded scaler is a:

```text
StandardScaler
```

It transforms the extracted audio features into the same scale used during model training.

This is important because the model expects the input features to have the same format and scale as the training data.

---

## `label_encoder.pkl`

Saved label encoder.

The loaded encoder is a:

```text
LabelEncoder
```

It converts numeric model predictions back into readable genre names.

Example:

```text
0 → blues
1 → classical
2 → country
```

---

## `requirements.txt`

Contains all required Python libraries for running the project. :contentReference[oaicite:2]{index=2}

Install them with:

```bash
pip install -r requirements.txt
```

---

## `templates/index.html`

HTML page rendered by Flask at the homepage route.

The route:

```python
@app.route('/')
def index():
    return render_template('index.html')
```

expects an `index.html` file inside a `templates` folder.

---

# How to Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Make Sure Model Files Exist

The following files must be in the same folder as `app.py`:

```text
music_model.pkl
scaler.pkl
label_encoder.pkl
```

The application loads them at startup using Joblib:

```python
model = joblib.load('music_model.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')
```

---

## 3. Run the Flask App

```bash
python app.py
```

The app runs on:

```text
http://localhost:5000
```

The Flask configuration uses:

```python
app.run(host='0.0.0.0', port=5000)
```

This makes it possible to expose the app when running in environments such as Google Colab.

---

# API Usage

## Homepage

```text
GET /
```

Returns the main HTML page.

---

## Prediction Endpoint

```text
POST /predict
```

This endpoint expects an uploaded audio file under the form field name:

```text
file
```

Example request using `curl`:

```bash
curl -X POST -F "file=@song.mp3" http://localhost:5000/predict
```

Example JSON response:

```json
[
  {
    "genre": "POP",
    "probability": 38.74
  },
  {
    "genre": "DISCO",
    "probability": 21.55
  },
  {
    "genre": "ROCK",
    "probability": 16.82
  }
]
```

---

# Technical Details

## Model Loading

When the application starts, it loads three saved objects:

```python
model = joblib.load('music_model.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')
```

These are loaded once at startup and reused for predictions.

The model is a trained `RandomForestClassifier`.

The scaler is a `StandardScaler`.

The label encoder is a `LabelEncoder`.

---

# Audio Loading

The uploaded audio file is loaded using Librosa:

```python
y, sr = librosa.load(file_path, duration=10)
```

This means the application only uses the first:

```text
10 seconds
```

of the uploaded audio file.

---

# Feature Extraction

The application extracts audio features from the uploaded file.

The extracted features include:

## Tempo

```text
tempo
```

---

## Chroma Features

```text
chroma_stft_mean
chroma_stft_var
```

---

## RMS Energy

```text
rms_mean
rms_var
```

---

## Spectral Features

```text
spectral_centroid_mean
spectral_centroid_var
spectral_bandwidth_mean
spectral_bandwidth_var
rolloff_mean
rolloff_var
zero_crossing_rate_mean
zero_crossing_rate_var
```

---

## Harmony and Percussive Features

```text
harmony_mean
harmony_var
perceptr_mean
perceptr_var
```

---

## MFCC Features

The app extracts 20 MFCC coefficients.

For each MFCC, it calculates:

- mean
- variance

Example:

```text
mfcc1_mean
mfcc1_var
mfcc2_mean
mfcc2_var
...
mfcc20_mean
mfcc20_var
```

---

# Number of Features

The model expects:

```text
57 audio features
```

The features are aligned using:

```python
scaler.feature_names_in_
```

This ensures that the feature order during prediction matches the feature order used during training.

This is important because machine learning models require the input columns to be in the same order as during training.

---

# Feature Scaling

After feature extraction, the app transforms the features using the saved scaler:

```python
X_scaled = scaler.transform(X)
```

The scaled features are then passed to the model.

---

# Prediction Logic

The model predicts probabilities using:

```python
probs = model.predict_proba(features)[0]
```

Then the application selects the top 3 predictions:

```python
top_3_idx = np.argsort(probs)[-3:][::-1]
```

Each prediction is converted back into a genre label using:

```python
le.inverse_transform([idx])
```

---

# Temporary File Handling

When a user uploads an audio file, the app temporarily saves it as:

```text
temp_audio.mp3
```

After prediction, the file is deleted:

```python
if os.path.exists(temp_path):
    os.remove(temp_path)
```

This prevents temporary files from staying in the project folder after each request.

---

# Error Handling

The app handles common request errors.

If no file is uploaded:

```json
{
  "error": "No file uploaded"
}
```

If no file is selected:

```json
{
  "error": "No file selected"
}
```

If an exception occurs during processing, the app returns:

```json
{
  "error": "error message"
}
```

---

# Important Notes

This project uses a pre-trained machine learning model.

The training code is not included in the uploaded application files.

The application focuses on inference, meaning it uses an already trained model to make predictions on new audio files.

The uploaded model was trained with Scikit-learn and saved using Joblib.

The app expects audio input but temporarily saves the uploaded file as:

```text
temp_audio.mp3
```

Because of this, MP3 files are the safest expected input format.

---

# Example Usage

## Example 1

### Input

```text
Uploaded file: rock_song.mp3
```

### Output

```json
[
  {
    "genre": "ROCK",
    "probability": 46.21
  },
  {
    "genre": "METAL",
    "probability": 24.77
  },
  {
    "genre": "BLUES",
    "probability": 11.36
  }
]
```

---

## Example 2

### Input

```text
Uploaded file: jazz_sample.mp3
```

### Output

```json
[
  {
    "genre": "JAZZ",
    "probability": 51.88
  },
  {
    "genre": "BLUES",
    "probability": 18.43
  },
  {
    "genre": "CLASSICAL",
    "probability": 9.62
  }
]
```

---

# What This Project Demonstrates

This project demonstrates:

- audio classification
- music genre prediction
- Flask API development
- audio feature extraction with Librosa
- Scikit-learn model inference
- saved model loading with Joblib
- feature scaling during inference
- label decoding
- probability-based predictions
- JSON API responses

---

# Conclusion

Music Genre Classification Web App is a Flask-based machine learning application that predicts the genre of an uploaded music file.

The app extracts audio features using Librosa, scales them with a saved StandardScaler, and uses a trained Random Forest model to return the top 3 predicted music genres with probabilities.

The project is mainly useful as an inference-focused machine learning web app for audio classification and music genre prediction.
