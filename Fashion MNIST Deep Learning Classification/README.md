# Deep Learning Assignment 1: Fashion MNIST Classification

This project focuses on image classification using the Fashion MNIST dataset. The goal is to classify grayscale images of clothing items into 10 different categories, such as T-shirts, trousers, pullovers, dresses, coats, sandals, sneakers, bags, and ankle boots.

The notebook compares different deep learning approaches for this classification task. First, it builds and evaluates Multi-Layer Perceptron (MLP) models, where the 28x28 images are flattened into one-dimensional vectors. Then, it builds and evaluates Convolutional Neural Network (CNN) models, where the original image structure is preserved.

## What This Project Does

- Loads and preprocesses the Fashion MNIST dataset.
- Splits the data into training, validation, and test sets.
- Normalizes pixel values from the range 0-255 to 0-1.
- Converts class labels into one-hot encoded vectors.
- Trains MLP models using different optimizers, such as Adam and SGD.
- Trains CNN models with and without batch normalization.
- Uses Keras Tuner with Bayesian Optimization to search for good hyperparameters.
- Applies techniques such as dropout, early stopping, and learning rate reduction.
- Evaluates the models using accuracy, loss, precision, recall, F1-score, and confusion matrices.
- Compares model performance and discusses possible improvements.

## Models Used

### Multi-Layer Perceptron

The MLP model receives flattened image vectors as input. Different hyperparameters are tested, including the number of hidden layers, number of units, activation functions, dropout rate, learning rate, batch size, and kernel initializer.

Two MLP versions are trained and compared:

- MLP with Adam optimizer
- MLP with SGD optimizer

The Adam optimizer performs better than SGD in this experiment, mainly because it converges faster and produces more stable validation results.

### Convolutional Neural Network

The CNN model works directly with the original 28x28 image format. It uses convolutional layers, max pooling, dropout, and dense layers to learn visual patterns from the images.

Two CNN versions are trained and compared:

- CNN with Adam optimizer and batch normalization
- CNN with Adam optimizer without batch normalization

The CNN models achieve strong performance, with test accuracy around 91%. The results show that batch normalization does not significantly improve performance in this specific experiment.

## Evaluation

The notebook evaluates each model using:

- Training, validation, and test accuracy
- Training, validation, and test loss
- Classification reports
- Precision, recall, and F1-score per class
- Confusion matrices
- Learning curves for accuracy and loss

The results show that visually similar categories, such as shirts, T-shirts, pullovers, and coats, are more difficult to classify correctly. Easier categories, such as bags, sandals, sneakers, and ankle boots, are classified more accurately.

## Conclusion

This project demonstrates how different neural network architectures and training strategies affect image classification performance. Overall, Adam performs better than SGD for the MLP model, while the CNN models provide strong and stable results for Fashion MNIST classification.

Future improvements could include testing more hyperparameter values, experimenting with additional optimizers such as AdamW, using data augmentation, and trying deeper CNN architectures.
