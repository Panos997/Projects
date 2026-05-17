# MURA Bone X-Ray Classification Using Deep Learning

This project focuses on binary image classification for musculoskeletal X-ray images using deep learning. The goal is to classify each X-ray image as either **positive** or **negative**, where positive cases indicate the presence of an abnormality and negative cases indicate normal studies.

The project uses the **MURA v1.1 dataset**, which contains musculoskeletal radiographs from different upper-extremity body parts, including the elbow, finger, forearm, hand, humerus, shoulder, and wrist.

The dataset can be found on Kaggle here:

https://www.kaggle.com/datasets/panagiotiskyrmpatsos/mura-v11/data

## What This Project Does

- Loads the MURA v1.1 image path CSV files.
- Extracts useful metadata from the image paths, such as:
  - body part
  - patient ID
  - study folder
  - positive or negative label
- Explores the distribution of images across body parts and labels.
- Splits the original training data into training and test sets.
- Creates a clean folder structure for training, validation, and test images.
- Loads the images using TensorFlow image datasets.
- Resizes all images to 128x128 pixels.
- Normalizes pixel values to the range 0-1.
- Applies simple data augmentation, including random flipping and random rotation.
- Builds a Convolutional Neural Network using TensorFlow and Keras.
- Uses Keras Tuner with Bayesian Optimization for hyperparameter tuning.
- Trains the CNN model using the Adam optimizer.
- Uses callbacks such as Early Stopping and ReduceLROnPlateau.
- Evaluates the model on the test set.
- Generates evaluation results per body part.
- Creates confusion matrices for each X-ray body part.
- Plots training history to compare model performance across epochs.

## Dataset

The project is based on the MURA v1.1 dataset. MURA is a large dataset of musculoskeletal radiographs designed for abnormality detection in X-ray images.

The notebook works with the following image categories:

- XR_ELBOW
- XR_FINGER
- XR_FOREARM
- XR_HAND
- XR_HUMERUS
- XR_SHOULDER
- XR_WRIST

Each image is labeled as either:

- Negative
- Positive

## Model

The project uses a Convolutional Neural Network for binary classification.

The CNN architecture includes:

- Input layer for 128x128 RGB images
- Multiple convolutional layers
- Max pooling layers
- Optional batch normalization
- Dropout layers
- Flatten layer
- Final dense output layer with sigmoid activation

The model is trained using binary cross-entropy loss and the Adam optimizer.

## Hyperparameter Tuning

Keras Tuner with Bayesian Optimization is used to search for better model configurations.

The tuned parameters include:

- Number of convolutional layers
- Activation function
- Kernel initializer
- Dropout rate
- Learning rate
- Output activation function

## Evaluation

The model is evaluated using several metrics, including:

- Precision
- Recall
- Cohen Kappa
- Confusion matrices
- Per-body-part classification results

The notebook also visualizes model performance through training curves and confusion matrices for each body part.

## Conclusion

This project demonstrates how deep learning can be applied to medical image classification using musculoskeletal X-ray images. It shows the full pipeline from dataset preprocessing and folder organization to CNN training, hyperparameter tuning, evaluation, and per-category analysis.

The project can be further improved by using more advanced architectures such as ResNet, EfficientNet, DenseNet, or transfer learning models pretrained on large image datasets.
