# Deep Learning Bone X-Ray Classification

## Overview

Deep Learning Bone X-Ray Classification is an experimental medical imaging project focused on evaluating deep learning workflows for detecting abnormalities in bone X-ray images using the MURA dataset.

The project was designed as a deep learning experimentation environment rather than a single fixed model implementation.

The main objective was to explore how different CNN configurations, preprocessing approaches, and hyperparameter settings affect classification performance on musculoskeletal radiograph data.

The project was developed and tested inside Google Colab using TensorFlow and Keras.

---

# Project Goal

The goal of the project was to investigate how deep learning models can assist in medical image classification tasks by automatically identifying abnormal bone X-rays.

Instead of simply training one model, the notebook focuses on experimentation and evaluation across multiple training configurations.

The experimentation process includes:

- CNN architecture experimentation
- preprocessing workflows
- hyperparameter tuning
- optimizer comparison
- activation function comparison
- dropout experimentation
- batch normalization testing
- validation analysis
- performance evaluation

The objective was to analyze which configurations perform better for bone X-ray abnormality classification.

---

# Dataset

The project uses the:

```text
MURA (Musculoskeletal Radiographs) Dataset
```

The dataset contains bone X-ray studies from different body parts, including:

- elbow
- finger
- forearm
- hand
- humerus
- shoulder
- wrist

Each study is labeled as:

- normal
- abnormal

The notebook processes dataset image paths using the official CSV files:

```text
train_image_paths.csv
valid_image_paths.csv
```

---

# What the Project Does

The system loads X-ray image datasets, preprocesses image metadata, trains CNN models, and evaluates classification performance.

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
Hyperparameter Experimentation
      ↓
Validation & Evaluation
      ↓
Performance Comparison
```

The project focuses on experimentation and evaluation rather than deployment or production usage.

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

Main notebook containing the complete experimentation workflow.

The notebook includes:

- dataset preprocessing
- metadata extraction
- train/test splitting
- image preparation
- CNN experimentation
- hyperparameter tuning
- model training
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
3. split the dataset
4. prepare the images
5. train CNN models
6. perform hyperparameter tuning
7. evaluate predictions
8. compare performance results

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

The preprocessing workflow also includes:

- NaN checking
- dataset statistics
- body part distribution analysis
- patient counting
- class balance analysis

---

# Dataset Splitting

The dataset is split into:

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

for model development and experimentation.

The notebook imports:

```python
import tensorflow as tf
import keras_tuner as kt
```

for training and hyperparameter tuning.

The workflow is based on custom CNN experimentation rather than comparing prebuilt architectures such as ResNet or EfficientNet.

---

# CNN Experimentation

The notebook experiments with multiple CNN configurations and training setups.

The experimentation includes:

- varying the number of convolutional layers
- activation function comparison
- dropout experimentation
- batch normalization testing
- optimizer configuration
- learning rate tuning
- kernel initializer comparison

The notebook tests configurations such as:

## Convolutional Layers

```python
hp.Int('convolutional layers', 2, 5)
```

which experiments with:

- 2 convolutional layers
- 3 convolutional layers
- 4 convolutional layers
- 5 convolutional layers

---

## Activation Functions

The notebook experiments with:

```python
relu
tanh
```

---

## Kernel Initializers

The notebook compares:

```python
glorot_uniform
glorot_normal
```

---

## Regularization & Training

The experimentation also includes:

- dropout layers
- batch normalization
- optimizer tuning
- training configuration tuning

---

# Hyperparameter Tuning

The project uses:

```python
Keras Tuner
```

for hyperparameter experimentation.

The notebook tests different combinations of:

- CNN depth
- activation functions
- optimizers
- learning rates
- regularization settings

to evaluate how different configurations affect model performance.

---

# Visualization & Analysis

The notebook uses:

- Matplotlib
- Seaborn

to visualize:

- dataset statistics
- class distribution
- preprocessing analysis
- training performance
- evaluation metrics

---

# Google Colab Integration

The notebook includes:

```python
from google.colab import drive
drive.mount('/content/drive/')
```

which indicates that the project was developed and executed inside Google Colab using Google Drive storage.

---

# Experimental Workflow

The notebook was structured as a deep learning experimentation environment for testing multiple CNN training workflows on medical X-ray data.

The experimentation process includes:

- preprocessing experimentation
- CNN configuration testing
- hyperparameter tuning
- validation monitoring
- performance comparison
- evaluation analysis

The objective was to identify which configurations perform better for bone X-ray abnormality classification tasks.

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
- hyperparameter tuning
- model evaluation
- preprocessing experimentation
- AI-assisted medical imaging analysis

---

# Conclusion

Deep Learning Bone X-Ray Classification is an experimental deep learning project focused on evaluating CNN training workflows for bone X-ray abnormality classification using the MURA dataset.

The project demonstrates medical image preprocessing, CNN experimentation, hyperparameter tuning, and evaluation workflows inside a Google Colab environment.
