from flask import Flask, request, render_template, jsonify
import librosa
import numpy as np
import joblib
import os

app = Flask(__name__)

# --- ΦΟΡΤΩΣΗ ΜΟΝΤΕΛΩΝ ---
# Βεβαιώσου ότι τα αρχεία .pkl είναι στον ίδιο φάκελο
model = joblib.load('music_model.pkl')
scaler = joblib.load('scaler.pkl')
le = joblib.load('label_encoder.pkl')

def extract_features(file_path):
    """Εξαγωγή 58 χαρακτηριστικών ακριβώς όπως στο εκπαιδευμένο μοντέλο"""
    y, sr = librosa.load(file_path, duration=10)
    
    features_dict = {}
    
    # Tempo
    tempo_data = librosa.beat.beat_track(y=y, sr=sr)
    features_dict['tempo'] = float(np.atleast_1d(tempo_data[0])[0])
    
    # Spectral & RMS
    features_dict['chroma_stft_mean'] = float(np.mean(librosa.feature.chroma_stft(y=y, sr=sr)))
    features_dict['chroma_stft_var'] = float(np.var(librosa.feature.chroma_stft(y=y, sr=sr)))
    features_dict['rms_mean'] = float(np.mean(librosa.feature.rms(y=y)))
    features_dict['rms_var'] = float(np.var(librosa.feature.rms(y=y)))
    features_dict['spectral_centroid_mean'] = float(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    features_dict['spectral_centroid_var'] = float(np.var(librosa.feature.spectral_centroid(y=y, sr=sr)))
    features_dict['spectral_bandwidth_mean'] = float(np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr)))
    features_dict['spectral_bandwidth_var'] = float(np.var(librosa.feature.spectral_bandwidth(y=y, sr=sr)))
    features_dict['rolloff_mean'] = float(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)))
    features_dict['rolloff_var'] = float(np.var(librosa.feature.spectral_rolloff(y=y, sr=sr)))
    features_dict['zero_crossing_rate_mean'] = float(np.mean(librosa.feature.zero_crossing_rate(y=y)))
    features_dict['zero_crossing_rate_var'] = float(np.var(librosa.feature.zero_crossing_rate(y=y)))
    
    # Harmony & Percussive
    y_harm, y_perc = librosa.effects.hpss(y)
    features_dict['harmony_mean'] = float(np.mean(y_harm))
    features_dict['harmony_var'] = float(np.var(y_harm))
    features_dict['perceptr_mean'] = float(np.mean(y_perc))
    features_dict['perceptr_var'] = float(np.var(y_perc))
    
    # MFCCs (20 mean + 20 var)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    for i in range(1, 21):
        features_dict[f'mfcc{i}_mean'] = float(np.mean(mfccs[i-1]))
        features_dict[f'mfcc{i}_var'] = float(np.var(mfccs[i-1]))

    # Ευθυγράμμιση με τον Scaler
    ordered_features = [features_dict[name] for name in scaler.feature_names_in_]
    X = np.array(ordered_features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    
    return X_scaled

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Προσωρινή αποθήκευση
    temp_path = "temp_audio.mp3"
    file.save(temp_path)
    
    try:
        # 1. Feature Extraction
        features = extract_features(temp_path)
        
        # 2. Prediction Probabilities
        probs = model.predict_proba(features)[0]
        
        # 3. Get Top 3
        top_3_idx = np.argsort(probs)[-3:][::-1]
        
        results = []
        for idx in top_3_idx:
            results.append({
                "genre": str(le.inverse_transform([idx])[0]).upper(),
                "probability": round(float(probs[idx]) * 100, 2)
            })
            
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    # Το host='0.0.0.0' είναι το κλειδί για να δουλέψει το link του Colab!
    app.run(host='0.0.0.0', port=5000)
