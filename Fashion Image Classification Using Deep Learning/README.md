# Fashion Image Classification Using Deep Learning

This folder contains a deep learning project for image classification using the **Fashion MNIST** dataset. The goal is to classify grayscale fashion product images into different categories using neural network models.

The project is implemented in a Jupyter/Google Colab notebook using **TensorFlow** and **Keras**. It explores and compares different deep learning approaches, including Multi-Layer Perceptron models and Convolutional Neural Networks.

## Dataset

The project uses the **Fashion MNIST** dataset, which contains 28x28 grayscale images of fashion items.

The dataset includes 10 classes:

- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle boot

Each image belongs to one of these categories, and the task is to train models that can correctly identify the class of each fashion item.

## Project Overview

The purpose of this project is to build, train, tune, and evaluate deep learning models for fashion image classification.

The notebook performs the following steps:

- Loads the Fashion MNIST dataset.
- Explores the structure and shape of the data.
- Visualizes sample images from the dataset.
- Normalizes image pixel values to the range 0-1.
- Converts class labels into one-hot encoded format.
- Splits the data into training, validation, and test sets.
- Builds and trains Multi-Layer Perceptron models.
- Builds and trains Convolutional Neural Network models.
- Compares different optimizers, including Adam and SGD.
- Applies regularization techniques such as dropout.
- Uses callbacks such as early stopping and learning rate reduction.
- Uses hyperparameter tuning to search for better model configurations.
- Evaluates model performance using classification metrics.
- Visualizes training curves and confusion matrices.

## Models

### Multi-Layer Perceptron

The project first uses Multi-Layer Perceptron models for image classification. In this approach, each 28x28 image is flattened into a one-dimensional vector before being passed into dense neural network layers.

Different configurations are tested, including:

- Number of hidden layers
- Number of neurons
- Activation functions
- Dropout rate
- Learning rate
- Optimizer type

The MLP models provide a useful baseline for the classification task.

### Convolutional Neural Network

The project also uses Convolutional Neural Networks, which are more suitable for image classification because they preserve the spatial structure of the image.

The CNN models include:

- Convolutional layers
- Pooling layers
- Dropout layers
- Dense layers
- Softmax output layer for multi-class classification

The CNN models generally perform better because they can learn local visual patterns such as edges, shapes, and textures.

## Hyperparameter Tuning

Hyperparameter tuning is used to improve model performance by searching for stronger model configurations.

The tuning process explores parameters such as:

- Number of layers
- Number of units or filters
- Activation function
- Dropout rate
- Learning rate
- Batch size
- Kernel initializer

This helps compare multiple model setups instead of relying on a single manually selected configuration.

## Evaluation

The trained models are evaluated using several performance metrics and visualizations.

The evaluation includes:

- Training accuracy
- Validation accuracy
- Test accuracy
- Training loss
- Validation loss
- Precision
- Recall
- F1-score
- Classification report
- Confusion matrix
- Accuracy and loss curves

The results help identify which model performs better and which classes are more difficult to classify.

## Results And Observations

The project shows that Convolutional Neural Networks are more effective than simple dense models for this image classification task. CNNs are better able to capture visual patterns from the fashion images, while MLP models lose spatial information after flattening the input images.

Some fashion categories are easier to classify, such as bags, trousers, sandals, sneakers, and ankle boots. Other categories, such as shirts, T-shirts, pullovers, and coats, can be more challenging because they have similar visual features.

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

This project demonstrates a complete deep learning workflow for multi-class fashion image classification. It covers data preprocessing, model development, hyperparameter tuning, training, evaluation, and result visualization.

The project highlights the difference between dense neural networks and convolutional neural networks, showing why CNNs are usually more effective for image-based tasks.

Future improvements could include more advanced CNN architectures, stronger data augmentation, transfer learning, and additional optimization techniques.
