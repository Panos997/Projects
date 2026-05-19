# Fashion Image Classification Using Deep Learning

This folder contains a deep learning project for image classification using the **Fashion MNIST** dataset, available on Kaggle:

https://www.kaggle.com/datasets/zalando-research/fashionmnist

The goal of the project is to classify grayscale fashion product images into different categories using deep learning models.

The project is implemented in a Jupyter/Google Colab notebook using **TensorFlow** and **Keras**. It explores and compares different neural network approaches, including Multi-Layer Perceptron models and Convolutional Neural Networks.

## Dataset

The project uses the **Fashion MNIST** dataset, which contains 28x28 grayscale images of fashion products. It is designed as a more challenging alternative to the classic MNIST digit dataset and is commonly used for benchmarking image classification models.

The dataset includes 10 classes:
* T-shirt/top
* Trouser
* Pullover
* Dress
* Coat
* Sandal
* Shirt
* Sneaker
* Bag
* Ankle boot

Each image belongs to one of these categories, and the task is to train deep learning models that can correctly classify each fashion item.

## Project Overview

The purpose of this project is to build, train, tune, and evaluate deep learning models for fashion image classification.

The notebook performs the following steps:
* Loads the Fashion MNIST dataset.
* Explores the structure and shape of the data.
* Visualizes sample images from the dataset.
* Normalizes image pixel values to the range 0-1.
* Converts class labels into one-hot encoded format.
* Splits the data into training, validation, and test sets.
* Builds and trains Multi-Layer Perceptron models.
* Builds and trains Convolutional Neural Network models.
* Compares different optimizers, including Adam and SGD.
* Applies regularization techniques such as dropout.
* Uses callbacks such as Early Stopping and ReduceLROnPlateau.
* Uses hyperparameter tuning to search for better model configurations.
* Evaluates model performance using classification metrics.
* Visualizes training curves and confusion matrices.

## Models

This project implements and compares two fundamentally different architectural approaches to demonstrate the evolution of Deep Learning in Computer Vision.

### 1. Multi-Layer Perceptron (MLP) - The Baseline
In this approach, the spatial 2D structure of the image is disregarded to establish a simple baseline.

* **The Pipeline:** The $28 \times 28$ pixel image is immediately fed into a `Flatten()` layer, converting it into a flat, one-dimensional vector of $784$ features ($28 \times 28 = 784$).
* **The Architecture:** This 1D vector passes directly through a sequence of fully connected (`Dense`) layers, followed by `Dropout` for regularization, and a final `Softmax` layer for prediction.
* **Limitation:** By flattening the input at the very beginning, the MLP loses all spatial relationships between neighboring pixels (e.g., it cannot inherently process the geometric structure of a sleeve or a collar).

### 2. Convolutional Neural Network (CNN) - The Spatial Approach
To overcome the limitations of the MLP, a CNN is implemented to extract visual features while preserving the image's original geometry.

* **The Pipeline:** The image retains its 2D grid shape ($28 \times 28 \times 1$) and is first passed through local feature extraction layers.
* **The Architecture:** It starts with alternating **Convolutional layers** (`Conv2D`), which apply learnable filters to detect local patterns (like edges, textures, and clothing shapes), and **Pooling layers** (`MaxPooling2D`) to downsample the spatial dimensions.
* **The Transition:** Only *after* the CNN layers have extracted these high-level visual features do we apply a `Flatten()` layer. This converts the rich feature maps into a 1D vector, which is then passed to the final `Dense` classification layers.

---

### Architectural Comparison Summary

| Feature | Multi-Layer Perceptron (MLP) | Convolutional Neural Network (CNN) |
| :--- | :--- | :--- |
| **Input Shape at Layer 1** | Flattened 1D Vector ($784$) | Original 2D Grid ($28 \times 28 \times 1$) |
| **Initial Processing** | Fully Connected (`Dense`) layers | Convolutional (`Conv2D`) + Pooling layers |
| **Spatial Awareness** | Lost immediately at the input stage | Preserved throughout feature extraction |
| **Target Patterns** | Global pixel intensities | Local visual features (edges, shapes, patches) |

---

## Hyperparameter Tuning

Hyperparameter tuning is used to improve model performance by searching for stronger model configurations.

The tuning process explores parameters such as:
* Number of layers
* Number of units or filters
* Activation function
* Dropout rate
* Learning rate
* Batch size
* Kernel initializer

This helps compare multiple model setups instead of relying on a single manually selected configuration.

## Evaluation

The trained models are evaluated using several performance metrics and visualizations.

The evaluation includes:
* Training / Validation / Test accuracy
* Training / Validation loss
* Precision, Recall, and F1-score
* Detailed Classification Report
* Confusion Matrix
* Accuracy and loss curves

The results help identify which model performs better and which fashion categories are more difficult to classify.

## Results And Observations

The project shows that Convolutional Neural Networks are more effective than simple dense models for this image classification task. CNNs are better able to capture visual patterns from the fashion images, while MLP models lose spatial information after flattening the input images.

Some fashion categories are easier to classify, such as bags, trousers, sandals, sneakers, and ankle boots. Other categories, such as shirts, T-shirts, pullovers, and coats, can be more challenging because they share similar shapes and visual features.

The comparison between optimizers also shows how training strategy affects model performance. Adaptive optimizers such as Adam usually converge faster and more smoothly than basic SGD in this type of experiment.

## Technologies Used

* Python
* Google Colab / Jupyter Notebook
* TensorFlow / Keras
* Keras Tuner
* NumPy & Pandas
* Matplotlib
* Scikit-learn

## Conclusion

This project demonstrates a complete deep learning workflow for multi-class fashion image classification. It covers data preprocessing, model development, hyperparameter tuning, training, evaluation, and result visualization.

The project highlights the structural difference between dense neural networks and convolutional neural networks, showing why CNNs are significantly more effective for image-based tasks.

Future improvements could include more advanced CNN architectures, stronger data augmentation, transfer learning, and additional optimization techniques.
