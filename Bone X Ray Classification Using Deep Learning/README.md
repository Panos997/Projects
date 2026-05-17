# Bone X-Ray Classification Using Deep Learning

This folder contains a deep learning project for binary abnormality classification on musculoskeletal X-ray images using the **MURA v1.1 dataset**. The goal of the project is to classify X-ray images as either **positive** or **negative**, where positive cases indicate the presence of an abnormality and negative cases indicate normal studies.

The project is implemented in a Jupyter/Google Colab notebook using **TensorFlow**, **Keras**, and **Keras Tuner**. It covers the full machine learning pipeline, from dataset loading and preprocessing to model training, hyperparameter tuning, evaluation, and result visualization.

## Dataset

This project uses the **MURA v1.1 dataset**, a musculoskeletal radiograph dataset for abnormality detection in upper-extremity X-ray images.

The dataset can be found on Kaggle:

https://www.kaggle.com/datasets/panagiotiskyrmpatsos/mura-v11/data

The dataset includes X-ray images from different body parts:

- XR_ELBOW
- XR_FINGER
- XR_FOREARM
- XR_HAND
- XR_HUMERUS
- XR_SHOULDER
- XR_WRIST

Each image is labeled as one of the following classes:

- **Negative**: normal X-ray study
- **Positive**: abnormal X-ray study

## Project Overview

The purpose of this project is to build and evaluate a Convolutional Neural Network model capable of detecting abnormalities in musculoskeletal X-ray images.

The notebook performs the following steps:

- Loads the MURA v1.1 dataset files.
- Reads the image path CSV files.
- Extracts metadata from image paths, including body part, patient ID, study folder, and label.
- Explores the distribution of images across body parts and positive/negative classes.
- Splits the available data into training, validation, and test sets.
- Creates a structured folder format suitable for TensorFlow image loading.
- Loads images using TensorFlow dataset utilities.
- Resizes all images to a fixed input size.
- Normalizes pixel values to improve training stability.
- Applies data augmentation to improve generalization.
- Builds a CNN model for binary image classification.
- Uses Keras Tuner with Bayesian Optimization to search for better hyperparameters.
- Trains the best CNN model using callbacks.
- Evaluates the model on test data.
- Analyzes performance per X-ray body part.
- Generates confusion matrices and training curves.

## Model

The project uses a **Convolutional Neural Network** for binary classification.

The CNN model includes:

- Convolutional layers for feature extraction
- Max pooling layers for spatial downsampling
- Optional batch normalization
- Dropout for regularization
- Dense layers for final classification
- Sigmoid output activation for binary prediction

The model is trained using:

- **Binary cross-entropy** as the loss function
- **Adam optimizer**
- Accuracy and additional evaluation metrics

## Hyperparameter Tuning

The notebook uses **Keras Tuner** with **Bayesian Optimization** to improve model performance.

The tuning process explores different values for parameters such as:

- Number of convolutional layers
- Number of filters
- Activation function
- Kernel initializer
- Dropout rate
- Learning rate
- Output activation function

This helps identify a stronger CNN configuration instead of relying on a manually selected architecture.

## Evaluation

The trained model is evaluated using multiple methods to better understand its performance.

The evaluation includes:

- Test accuracy
- Precision
- Recall
- Cohen Kappa score
- Confusion matrices
- Per-body-part performance analysis
- Training and validation accuracy curves
- Training and validation loss curves

The notebook also examines how the model performs across the different anatomical categories, such as wrist, shoulder, hand, elbow, and others.

## Results And Observations

The project shows how a CNN can be trained to detect abnormalities in medical X-ray images. The per-body-part evaluation is especially useful because performance may vary depending on the anatomical region and the visual complexity of the X-ray images.

Some body parts may be easier to classify, while others may be more challenging due to subtle abnormalities, image variation, or class imbalance.

## Technologies Used

- Python
- Google Colab / Jupyter Notebook
- TensorFlow
- Keras
- Keras Tuner
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Conclusion

This project demonstrates a complete deep learning workflow for medical image classification using the MURA v1.1 dataset. It covers data preparation, exploratory analysis, CNN model development, hyperparameter tuning, training, and detailed evaluation.

The project can be further improved by using transfer learning with pretrained architectures such as ResNet, DenseNet, EfficientNet, or MobileNet. Additional improvements could include more advanced data augmentation, class balancing techniques, and more detailed patient-level evaluation.
