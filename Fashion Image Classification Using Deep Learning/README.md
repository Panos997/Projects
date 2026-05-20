# Deep Learning Fashion MNIST Classification

## Overview

Deep Learning Fashion MNIST Classification is an experimental deep learning project that classifies fashion item images from the Fashion MNIST dataset.

The project compares different neural network workflows using:

- Multi-Layer Perceptron models
- Convolutional Neural Network models
- different optimizers
- batch normalization
- hyperparameter tuning

The goal is to test which model configurations perform better for image classification on the Fashion MNIST dataset.

The project was developed in a Jupyter / Google Colab notebook using TensorFlow, Keras, and Keras Tuner.

---

# Project Goal

The main goal of this project is to classify grayscale fashion images into one of 10 clothing categories.

The project is not just a simple model training notebook. It compares different deep learning approaches and training configurations to understand how they affect classification performance.

The experimentation includes:

- MLP model training
- CNN model training
- Adam optimizer testing
- SGD optimizer testing
- CNN with batch normalization
- CNN without batch normalization
- hyperparameter tuning with Keras Tuner
- learning curve analysis
- test set evaluation
- classification report analysis
- confusion matrix analysis

---

# Dataset

The project uses the Fashion MNIST dataset from TensorFlow/Keras.

Fashion MNIST contains grayscale images of fashion items.

Each image has size:

```text
28 x 28 pixels
```

Each image belongs to one of 10 classes:

```text
0 - T-shirt/top
1 - Trouser
2 - Pullover
3 - Dress
4 - Coat
5 - Sandal
6 - Shirt
7 - Sneaker
8 - Bag
9 - Ankle boot
```

The dataset is loaded directly from Keras:

```python
from tensorflow.keras.datasets import fashion_mnist

(X_train_dev, y_train_dev), (X_test, y_test) = fashion_mnist.load_data()
```

---

# What the Project Does

The notebook trains and evaluates different deep learning models for Fashion MNIST classification.

The general workflow is:

```text
Fashion MNIST Dataset
        ↓
Data Splitting
        ↓
Preprocessing
        ↓
Model Creation
        ↓
Hyperparameter Tuning
        ↓
Model Training
        ↓
Evaluation
        ↓
Model Comparison
```

The project compares MLP and CNN-based approaches and evaluates their performance using accuracy, loss curves, classification reports, and confusion matrices.

---

# Models Tested

The notebook tests the following model workflows:

## 1. MLP with Adam Optimizer

A Multi-Layer Perceptron model trained using the Adam optimizer.

This model uses flattened image data.

---

## 2. MLP with SGD Optimizer

A Multi-Layer Perceptron model trained using the SGD optimizer.

This allows comparison between Adam and SGD for the same general MLP approach.

---

## 3. CNN with Adam and Batch Normalization

A Convolutional Neural Network trained using Adam optimizer with batch normalization enabled.

This tests whether batch normalization improves CNN training and validation performance.

---

## 4. CNN with Adam without Batch Normalization

A Convolutional Neural Network trained using Adam optimizer without batch normalization.

This is compared against the batch normalization version.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | Neural network API |
| Keras Tuner | Hyperparameter tuning |
| NumPy | Numerical operations |
| Matplotlib | Learning curve visualization |
| Seaborn | Confusion matrix visualization |
| Scikit-learn | Train/test split and evaluation metrics |
| Fashion MNIST | Image classification dataset |
| Jupyter Notebook / Google Colab | Development environment |

---

# Project Structure

```text
Deep Learning Fashion MNIST Classification/
│
├── Code.ipynb
└── README.md
```

---

# File Explanation

## `Code.ipynb`

Main notebook containing the full experimentation workflow.

The notebook includes:

- library installation
- imports
- helper functions
- Fashion MNIST loading
- dataset preprocessing
- MLP model creation
- CNN model creation
- hyperparameter tuning
- training with different configurations
- model evaluation
- learning curve visualization
- classification reports
- confusion matrices
- final observations

---

# How to Run the Project

## 1. Open the Notebook

Open:

```text
Code.ipynb
```

using one of the following:

- Google Colab
- Jupyter Notebook
- JupyterLab
- VS Code

---

## 2. Install Required Library

The notebook installs Keras Tuner using:

```python
!pip install keras-tuner --upgrade
```

If running locally, install the main libraries with:

```bash
pip install tensorflow keras-tuner numpy matplotlib seaborn scikit-learn
```

---

## 3. Run the Notebook Cells

Run the notebook cells from top to bottom.

The notebook will:

1. load Fashion MNIST
2. split the training data into train and validation sets
3. preprocess the data for MLP
4. train and tune MLP models
5. preprocess the data for CNN
6. train and tune CNN models
7. evaluate the models
8. visualize learning curves
9. generate classification reports and confusion matrices

---

# Technical Details

# Dataset Loading

The dataset is loaded from Keras:

```python
from tensorflow.keras.datasets import fashion_mnist
```

The dataset contains:

```text
60,000 training images
10,000 test images
```

The notebook further splits the training data into:

```text
54,000 training images
6,000 validation images
```

using:

```python
train_test_split()
```

---

# Preprocessing for MLP

For the MLP models, the images are flattened.

Original image shape:

```text
28 x 28
```

Flattened shape:

```text
784
```

Example:

```python
X_train = X_train.reshape(54000, 784)
X_dev = X_dev.reshape(6000, 784)
X_test = X_test.reshape(10000, 784)
```

The pixel values are converted to `float32` and normalized:

```python
X_train /= 255
X_dev /= 255
X_test /= 255
```

Labels are converted into one-hot encoded vectors using:

```python
to_categorical()
```

---

# Preprocessing for CNN

For the CNN models, the images keep their spatial structure.

The data is reshaped into:

```text
28 x 28 x 1
```

because Fashion MNIST images are grayscale.

Example:

```python
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_dev = X_dev.reshape(X_dev.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
```

The pixel values are normalized to the range:

```text
0 to 1
```

and labels are one-hot encoded.

---

# Helper Functions

The notebook defines helper functions for:

## Learning Curves

```python
plot_history()
```

Used to plot training and validation curves for:

- loss
- accuracy

---

## Memory Cleanup

```python
clean_up()
```

Used to clear the Keras session and free memory after model training.

---

## Model Report

```python
report()
```

Used to print:

- train loss
- validation loss
- test loss
- train accuracy
- validation accuracy
- test accuracy

---

# MLP Model

The MLP model is created using a custom Keras Tuner HyperModel class:

```python
class MyHyperModel(kt.HyperModel):
```

The model uses:

- input layer
- multiple dense hidden layers
- optional dropout
- output layer with softmax activation

The model is compiled with:

```python
loss='categorical_crossentropy'
metrics=['accuracy']
```

because this is a multi-class classification problem.

---

# MLP Hyperparameters Tuned

The MLP tuning process includes:

## Number of Hidden Layers

```python
hp.Int('hidden layers', 2, 5)
```

The tuner tests between:

```text
2 and 5 hidden layers
```

---

## Units per Dense Layer

```python
hp.Choice('units of Dense', [128, 256, 512])
```

The tuner tests dense layers with:

```text
128, 256, or 512 units
```

---

## Activation Function

```python
hp.Choice('activation_function', ['swish', 'tanh', 'gelu'])
```

The tuner tests:

```text
swish
tanh
gelu
```

---

## Kernel Initializer

```python
hp.Choice('kernel_initializer', ['glorot_uniform', 'glorot_normal'])
```

The output layer also includes:

```text
he_normal
```

as an additional initializer option.

---

## Dropout Rate

```python
hp.Float('dropout_rate', 0, 0.6, step=0.2)
```

The tuner tests dropout values from:

```text
0 to 0.6
```

---

## Learning Rate

```python
hp.Float("lr", 0.00001, 0.001)
```

The tuner tests learning rates between:

```text
0.00001 and 0.001
```

---

## Batch Size

```python
hp.Choice("batch_size", [16, 32, 64, 128, 256])
```

The tuner tests different batch sizes.

---

# MLP Experiments

The notebook trains two MLP configurations:

## MLP with Adam

```python
MyHyperModel(True, Adam)
```

This model uses:

- dropout enabled
- Adam optimizer
- Bayesian Optimization tuning
- validation accuracy as tuning objective

---

## MLP with SGD

```python
MyHyperModel(True, SGD)
```

This model uses:

- dropout enabled
- SGD optimizer
- Bayesian Optimization tuning
- validation accuracy as tuning objective

---

# CNN Model

The CNN model is created using another custom Keras Tuner HyperModel class:

```python
class MyCNNHyperModel(kt.HyperModel):
```

The CNN includes:

- input layer
- convolutional blocks
- optional batch normalization
- max pooling
- optional dropout
- flatten layer
- softmax output layer

The output layer has 10 units because Fashion MNIST has 10 classes.

---

# CNN Hyperparameters Tuned

## Number of Convolutional Blocks

```python
hp.Int('convolutional_layers', 1, 3)
```

The tuner tests between:

```text
1 and 3 convolutional blocks
```

Each block contains two `Conv2D` layers.

---

## Activation Function

```python
hp.Choice('activation_function', ['swish', 'tanh', 'gelu'])
```

The tuner tests:

```text
swish
tanh
gelu
```

---

## Kernel Initializer

```python
hp.Choice('kernel_initializer', ['glorot_uniform', 'glorot_normal'])
```

The tuner tests:

```text
glorot_uniform
glorot_normal
```

---

## Dropout Rate

```python
hp.Float('dropout_rate', 0, 0.6, step=0.2)
```

The tuner tests dropout rates from:

```text
0 to 0.6
```

---

## Learning Rate

```python
hp.Float("lr", 0.00001, 0.001)
```

The tuner tests learning rates between:

```text
0.00001 and 0.001
```

---

## Batch Size

```python
hp.Choice("batch_size", [16, 32, 64, 128, 256])
```

The tuner tests different batch sizes.

---

# CNN Experiments

The notebook trains two CNN configurations:

## CNN with Adam and Batch Normalization

```python
MyCNNHyperModel(True, Adam, True)
```

This model uses:

- dropout enabled
- Adam optimizer
- batch normalization enabled
- Bayesian Optimization tuning

---

## CNN with Adam without Batch Normalization

```python
MyCNNHyperModel(True, Adam, False)
```

This model uses:

- dropout enabled
- Adam optimizer
- batch normalization disabled
- Bayesian Optimization tuning

---

# Hyperparameter Tuning

The notebook uses Keras Tuner with Bayesian Optimization:

```python
kt.BayesianOptimization()
```

The tuning objective is:

```python
val_accuracy
```

Each tuner uses:

```python
max_trials=10
```

This means each experiment can test up to 10 hyperparameter combinations.

---

# Training Setup

The models are trained using:

```python
model.fit()
```

with:

- training data
- validation data
- up to 100 epochs
- learning rate scheduling
- early stopping

---

# Callbacks

The notebook uses two important callbacks:

## Reduce Learning Rate on Plateau

```python
ReduceLROnPlateau()
```

This reduces the learning rate when validation performance stops improving.

---

## Early Stopping

```python
EarlyStopping()
```

This stops training early when validation performance stops improving and restores the best model weights.

---

# Evaluation

The models are evaluated on the test set using:

```python
model.evaluate()
```

The notebook also produces:

- learning curves
- classification reports
- confusion matrices

The evaluation focuses on:

- training loss
- validation loss
- test loss
- training accuracy
- validation accuracy
- test accuracy
- class-level performance

---

# Model Comparison Logic

The project compares performance across these main setups:

```text
MLP + Adam
MLP + SGD
CNN + Adam + Batch Normalization
CNN + Adam without Batch Normalization
```

The comparison is based on:

- validation accuracy
- test accuracy
- learning curves
- classification reports
- confusion matrices

The notebook also notes that batch size, learning rate, and optimizer had a significant impact on model performance.

---

# Example Workflow

```text
Fashion MNIST image
        ↓
Preprocess image
        ↓
Train MLP or CNN model
        ↓
Tune hyperparameters
        ↓
Evaluate on test set
        ↓
Compare results
```

---

# What This Project Demonstrates

This project demonstrates:

- image classification with deep learning
- Fashion MNIST dataset handling
- MLP model experimentation
- CNN model experimentation
- optimizer comparison
- batch normalization testing
- hyperparameter tuning with Keras Tuner
- learning curve visualization
- confusion matrix analysis
- classification report evaluation

---

# Important Notes

This project is an educational and experimental deep learning notebook.

It does not use pretrained architectures such as:

- ResNet
- EfficientNet
- VGG
- DenseNet

The project focuses on custom MLP and CNN models built with TensorFlow/Keras.

The goal is to compare training configurations and understand which settings improve Fashion MNIST classification performance.

---

# Conclusion

Deep Learning Fashion MNIST Classification is an experimental deep learning project that compares MLP and CNN workflows for classifying Fashion MNIST images.

The notebook demonstrates how model architecture, optimizer choice, batch normalization, learning rate, batch size, and hyperparameter tuning affect image classification performance.

It is mainly useful as a learning project for neural networks, CNNs, TensorFlow/Keras, and practical deep learning experimentation.
