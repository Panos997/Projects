# Deep Learning Bone X-Ray Classification

## Overview

Deep Learning Bone X-Ray Classification is an experimental medical imaging project focused on evaluating different deep learning approaches for detecting abnormalities in bone X-ray images using the MURA dataset.

The project was developed as a deep learning experimentation pipeline rather than a single fixed model workflow.

The main objective was to test and compare different preprocessing methods, training configurations, and deep learning techniques in order to analyze which approaches perform better for musculoskeletal X-ray classification tasks.

The project was implemented and tested inside Google Colab using TensorFlow and Keras.

---

# Project Goal

The goal of the project was to explore how deep learning models can assist in medical image classification by automatically identifying abnormal bone X-rays.

Instead of simply training one model, the notebook focuses on experimentation and evaluation across different workflows and configurations.

The experimentation process includes:

- dataset preprocessing
- image preparation
- CNN training
- hyperparameter tuning
- model comparison
- validation analysis
- performance evaluation

The project uses the MURA (Musculoskeletal Radiographs) dataset for experimentation and testing.

---

# Dataset

The project uses the:

```text
MURA (Musculoskeletal Radiographs) Dataset
```

which contains bone X-ray images from different body parts such as:

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

The notebook processes the dataset using the official CSV image path files:

```text
train_image_paths.csv
valid_image_paths.csv
```

---

# What the Project Does

The system loads X-ray image datasets, preprocesses the data, trains deep learning models, and evaluates classification performance.

The workflow includes:

```text
X-Ray Dataset
      ↓
CSV Preprocessing
      ↓
Dataset Splitting
      ↓
Image Preparation
      ↓
CNN Training
      ↓
Validation & Evaluation
      ↓
Performance Comparison
```

The objective is to evaluate how effectively deep learning models can classify bone X-rays as normal or abnormal.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | Neural network API |
| Keras Tuner | Hyperparameter tuning |
| TensorFlow Addons | Additional training utilities |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Dataset splitting |
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

Main notebook containing the complete experimentation workflow.

The notebook includes:

- dataset preprocessing
- metadata extraction
- train/test splitting
- image preparation
- deep learning experimentation
- model training
- hyperparameter tuning
- validation analysis
- evaluation and visualization

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

Dataset:

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

- Google Colab
- Jupyter Notebook
- JupyterLab
- VS Code

---

## 4. Configure Dataset Paths

Inside the notebook, configure the dataset location.

Example:

```python
path = '../MURA-v1.1'
```

The notebook expects the MURA dataset structure and CSV files to exist in the configured location.

---

## 5. Run the Notebook

Run the notebook cells sequentially.

The workflow will:

1. load the dataset
2. preprocess image metadata
3. split train/test data
4. prepare the images
5. train deep learning models
6. evaluate predictions
7. compare model performance

---

# Technical Details

# Dataset Preprocessing

The notebook reads dataset image paths from:

```python
train_image_paths.csv
valid_image_paths.csv
```

Metadata is extracted directly from image paths, including:

- body part
- patient ID
- study type
- abnormality labels

Example preprocessing logic:

```python
train['Body_Part'] = train['image_path'].apply(lambda x: x.split('/')[2])
```

The preprocessing pipeline also includes:

- NaN checking
- dataset statistics
- body part distribution analysis
- patient counting

---

# Dataset Splitting

The notebook splits the dataset into:

- train set
- validation set
- test set

using:

```python
train_test_split()
```

from Scikit-learn.

Example:

```python
train, test = train_test_split(
    train,
    test_size=0.15,
    random_state=1888
)
```

---

# Deep Learning Workflow

The project uses:

```python
TensorFlow + Keras
```

for deep learning model development and experimentation.

The notebook imports:

```python
import tensorflow as tf
import keras_tuner as kt
```

for model training and hyperparameter tuning.

The workflow focuses on experimentation and evaluation rather than a single production model.

---

# Hyperparameter Tuning

The project includes experimentation with:

- optimizers
- learning rates
- training configurations
- model architectures
- tuning strategies

using:

```python
Keras Tuner
```

This allows comparison between different training setups and performance results.

---

# Visualization & Analysis

The notebook uses:

- Matplotlib
- Seaborn

to visualize:

- dataset statistics
- class distribution
- preprocessing results
- training performance
- evaluation metrics

---

# Google Colab Integration

The notebook includes:

```python
from google.colab import drive
drive.mount('/content/drive/')
```

which indicates that the project was primarily developed and executed inside Google Colab using Google Drive storage.

---

# Experimental Workflow

The notebook was structured as an experimentation environment for testing multiple deep learning workflows on medical X-ray data.

The experimentation process includes:

- preprocessing experimentation
- CNN training workflows
- hyperparameter tuning
- training comparison
- validation monitoring
- performance analysis

The objective was to evaluate which methods perform better for bone X-ray abnormality classification tasks.

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
- deep learning experimentation
- CNN training pipelines
- TensorFlow/Keras workflows
- dataset preprocessing
- hyperparameter tuning
- AI-assisted medical imaging analysis
- experimental model evaluation

---

# Conclusion

Deep Learning Bone X-Ray Classification is an experimental deep learning project focused on evaluating different AI approaches for bone X-ray abnormality classification using the MURA dataset.

The project demonstrates medical image preprocessing, CNN experimentation, hyperparameter tuning, and deep learning evaluation workflows inside a Google Colab environment.
