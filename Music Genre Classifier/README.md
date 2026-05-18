# Music Genre AI

A simple web app that predicts the music genre of an uploaded audio file.

The user uploads a song, the app analyzes the audio, and then it shows the top 3 most likely genres with percentages.

## What this project does

This project uses a trained machine learning model to recognize the genre of a music file.

In simple words:

1. You upload an audio file.
2. The app takes a short sample from the song.
3. It extracts useful audio information, such as tempo and sound features.
4. The trained model predicts the most likely music genres.
5. The results are shown on the page with percentages and a chart.

## Main files

- `app.py`  
  The main Flask application. It loads the model, receives the uploaded audio file, extracts audio features, and returns the prediction.

- `index.html`  
  The web page that the user sees. It has the upload button, progress bar, results area, and chart.

- `music_model.pkl`  
  The trained machine learning model.

- `scaler.pkl`  
  Used to scale the audio features before prediction.

- `label_encoder.pkl`  
  Converts the model output into readable genre names.

- `requirements.txt`  
  Contains the Python libraries needed to run the project.

## How it works

The app extracts audio features from the uploaded file using `librosa`.

Some examples of features are:

- tempo
- rhythm
- loudness
- spectral features
- MFCCs

These features are then passed to the trained model.  
The model returns probabilities for different genres.

The app finally shows the top 3 genres.

## How to run the project

First, install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the Flask app:

```bash
python app.py
```

Open the app in your browser:

```text
http://localhost:5000
```

## Example result

After uploading a song, the app may return something like:

```text
ROCK: 72.5%
POP: 18.3%
DISCO: 9.2%
```

This means the model thinks the song is most likely Rock.

## Notes

- The `.pkl` files must be in the same folder as `app.py`.
- The app is made for simple music genre prediction.
- The prediction depends on the trained model and the quality of the uploaded audio file.
- This is a machine learning project, so the result may not always be perfect.

## Technologies used

- Python
- Flask
- Librosa
- NumPy
- Scikit-learn
- Joblib
- Chart.js
- HTML / CSS / JavaScript
