# Deep Learning Bone X-Ray Classification

## Overview

Deep Learning Bone X-Ray Classification is a medical imaging project that uses Convolutional Neural Networks (CNNs) to classify bone X-ray images from the MURA dataset.

The goal of the project is to explore how deep learning can assist in medical image analysis by automatically detecting abnormalities in bone X-rays.

The project focuses on:

- medical image preprocessing
- deep learning classification
- transfer learning experimentation
- model evaluation
- image-based abnormality detection

The system was developed and tested inside a Jupyter/Google Colab environment using TensorFlow and Keras.

---

# What the Project Does

The project processes bone X-ray images from the MURA dataset and trains deep learning models to classify whether an image is:

- normal
- abnormal

The workflow includes:

- dataset preprocessing
- train/validation/test splitting
- image preparation
- CNN training
- performance evaluation

The project experiments with deep learning techniques for medical image classification and automated diagnosis support.

---

# Dataset

The project uses the:

```text
MURA (Musculoskeletal Radiographs) Dataset
```

which contains bone X-ray images from different body parts.

Examples include:

- elbow
- finger
- forearm
- hand
- humerus
- shoulder
- wrist

The dataset contains both:

- normal studies
- abnormal studies

---

# How It Works

The workflow of the project is:

```text
X-Ray Images
      ↓
Dataset Preprocessing
      ↓
Train / Validation / Test Split
      ↓
Image Preparation
      ↓
CNN Model Training
      ↓
Prediction & Evaluation
```

---

# Main Workflow

## 1. Dataset Loading

The project loads image paths from CSV files provided by the MURA dataset.

Example:

```python
train_image_paths.csv
valid_image_paths.csv
```

The notebook extracts metadata such as:

- body part
- patient ID
- study type
- abnormality labels

---

## 2. Data Preprocessing

The preprocessing pipeline includes:

- image path processing
- label extraction
- dataset cleaning
- train/test splitting
- normalization
- image resizing

The notebook also performs exploratory analysis on the dataset.

---

## 3. Model Training

The project trains deep learning models using TensorFlow/Keras.

The workflow includes:

- CNN training
- transfer learning experimentation
- hyperparameter tuning
- validation monitoring

---

## 4. Evaluation

The trained model is evaluated using validation and test data.

The notebook includes:

- prediction analysis
- performance metrics
- visualization
- confusion matrix analysis

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | Neural network API |
| Keras Tuner | Hyperparameter tuning |
| TensorFlow Addons | Additional deep learning utilities |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Dataset splitting and evaluation |
| Google Colab | Training environment |

---

# Project Structure

```text
Deep Learning Bone X-Ray Classification/
│
├── Code.ipynb
├── README.md
└── requirements.txt
```

---

# File Explanation

## `Code.ipynb`

Main notebook containing the complete deep learning workflow.

The notebook includes:

- dataset preprocessing
- metadata extraction
- train/test splitting
- image preparation
- model training
- hyperparameter tuning
- evaluation
- visualization

The notebook was developed inside Google Colab and includes Google Drive integration for dataset access.

---

# How to Run the Project

## 1. Install Dependencies

Example:

```bash
pip install tensorflow keras keras-tuner tensorflow-addons pandas numpy matplotlib seaborn scikit-learn
```

---

## 2. Download the MURA Dataset

Download the dataset from:

```text
https://stanfordmlgroup.github.io/competitions/mura/
```

---

## 3. Open the Notebook

Open:

```text
Code.ipynb
```

using:

- Jupyter Notebook
- JupyterLab
- Google Colab
- VS Code

---

## 4. Configure Dataset Paths

Inside the notebook, update dataset paths if necessary.

Example:

```python
path = '../MURA-v1.1'
```

---

## 5. Run the Notebook

Run the notebook cells sequentially.

The workflow will:

1. load the dataset
2. preprocess images
3. split the dataset
4. train the model
5. evaluate predictions

---

# Technical Details

# Dataset Processing

The notebook reads dataset CSV files containing image paths:

```python
train_image_paths.csv
valid_image_paths.csv
```

Metadata such as:

- body part
- patient ID
- study type
- abnormality labels

is extracted directly from image paths.

Example logic:

```python
train['Body_Part'] = train['image_path'].apply(lambda x: x.split('/')[2])
```

---

# Data Splitting

The dataset is split into:

- training set
- validation set
- test set

using:

```python
train_test_split()
```

from Scikit-learn.

---

# Deep Learning Framework

The project uses:

```python
TensorFlow + Keras
```

for model development and training.

The notebook imports:

```python
tensorflow as tf
```

and:

```python
keras_tuner as kt
```

for hyperparameter experimentation.

---

# Hyperparameter Tuning

The project includes experimentation with:

- learning rates
- optimizers
- model configurations
- training parameters

using:

```python
Keras Tuner
```

---

# Visualization

The notebook uses:

- Matplotlib
- Seaborn

to visualize:

- dataset statistics
- class distribution
- training performance
- evaluation results

---

# Google Colab Integration

The notebook includes:

```python
from google.colab import drive
drive.mount('/content/drive/')
```

which indicates that the project was trained inside Google Colab using Google Drive storage.

---

# Medical AI Focus

The project explores how deep learning models can support medical imaging workflows by identifying abnormalities in X-ray images.

The system is designed as an experimental educational project and not as a production-ready medical diagnosis system.

---

# Example Workflow

```text
Bone X-Ray Image
        ↓
Image Preprocessing
        ↓
CNN Feature Extraction
        ↓
Deep Learning Classification
        ↓
Normal / Abnormal Prediction
```

---

# What This Project Demonstrates

This project demonstrates:

- medical image classification
- deep learning workflows
- CNN training pipelines
- TensorFlow/Keras usage
- medical dataset preprocessing
- transfer learning experimentation
- hyperparameter tuning
- AI-assisted medical imaging analysis

---

# Conclusion

Deep Learning Bone X-Ray Classification demonstrates how deep learning models can be applied to medical imaging tasks using TensorFlow and CNN architectures.

The project focuses on medical image preprocessing, model training, and automated abnormality classification using the MURA musculoskeletal radiograph dataset.
