# Fashion Image Classification Using Deep Learning

This repository contains a deep learning project for multi-class image classification using the **Fashion MNIST** dataset. The goal is to classify $28 \times 28$ grayscale fashion product images into 10 distinct categories, exploring the architectural transition and performance differences between dense networks and convolutional networks.

The project is implemented in Python using **TensorFlow**, **Keras**, and **Keras Tuner** for automated hyperparameter optimization.

---

## Dataset

The **Fashion MNIST** dataset consists of 60,000 training images and 10,000 test images. Each sample is a $28 \times 28$ grayscale image associated with a label from one of the following 10 classes:

* `0`: T-shirt/top
* `1`: Trouser
* `2`: Pullover
* `3`: Dress
* `4`: Coat
* `5`: Sandal
* `6`: Shirt
* `7`: Sneaker
* `8`: Bag
* `9`: Ankle boot

All pixel values are normalized to the range $[0, 1]$ prior to training to ensure numerical stability.

---

## Project Workflow

The machine learning pipeline inside the notebook follows these core steps:
1. **Data Loading & Splitting:** Importing the dataset and splitting the original training data into training ($90\%$) and validation/dev ($10\%$) sets.
2. **Data Exploration:** Visualizing sample images and inspecting class distributions across the subsets.
3. **Preprocessing:** Normalizing pixel intensities and converting integer labels into one-hot encoded vectors.
4. **Baseline Modeling (MLP):** Reshaping images into 1D vectors and training fully connected neural networks.
5. **Advanced Modeling (CNN):** Maintaining the 2D spatial grid of the images and training convolutional architectures.
6. **Hyperparameter Tuning:** Using `Keras Tuner` with **Bayesian Optimization** to automatically find the best structural parameters (layers, units, learning rates, batch sizes).
7. **Evaluation:** Comparing models using learning curves (loss/accuracy), classification reports (Precision, Recall, F1-score), and Confusion Matrices.

---

## Model Architectures

This project highlights and compares two fundamentally different structural approaches:

### 1. Multi-Layer Perceptron (MLP) - The Baseline
* **Data Reshaping:** The $28 \times 28$ image is immediately flattened into a single 1D vector of $784$ features ($28 \times 28 = 784$).
* **Pipeline:** This vector passes directly through a sequence of fully connected (`Dense`) hidden layers, regularized with `Dropout`.
* **Limitation:** By flattening the image right at the input stage, the network completely loses the spatial/geometric relationships between neighboring pixels.

### 2. Convolutional Neural Network (CNN) - The Spatial Approach
* **Data Reshaping:** Images retain their original 2D grid shape ($28 \times 28 \times 1$, where $1$ represents the grayscale channel).
* **Pipeline:** The input first passes through alternating **Convolutional layers** (`Conv2D`) to extract local visual patterns (edges, textures, shapes) and **Pooling layers** (`MaxPool2D`) to downsample spatial dimensions. 
* **The Transition:** A `Flatten()` layer is applied **only after** the convolutional layers have completed feature extraction. The resulting feature vector is then routed to the final dense layers for classification.

---

### Architectural Comparison Summary

| Feature | Multi-Layer Perceptron (MLP) | Convolutional Neural Network (CNN) |
| :--- | :--- | :--- |
| **Input Shape at Layer 1** | Flattened 1D Vector ($784$) | Original 2D Grid ($28 \times 28 \times 1$) |
| **Initial Processing** | Fully Connected (`Dense`) layers | Convolutional (`Conv2D`) + Max-Pooling layers |
| **Spatial Awareness** | Lost immediately at the input stage | Preserved throughout feature extraction |
| **Target Patterns** | Global pixel intensities | Local visual features (edges, shapes, patches) |

---

## Results & Key Observations

* **Architectural Superiority:** The Convolutional Neural Network significantly outperforms the MLP baseline, achieving a test accuracy of **~91%**. This demonstrates that retaining the spatial geometry of image data is critical for computer vision tasks.
* **Optimizer Performance:** Experiments show that adaptive optimizers like **Adam** converge faster and yield much smoother optimization paths compared to standard Stochastic Gradient Descent (**SGD**).
* **Batch Normalization Effects:** Comparing CNN variants revealed that training with and without Batch Normalization achieved nearly identical performance on the test set. The most critical hyperparameters influencing model score variance were **learning rate** and **batch size**.
* **Classification Challenges:** Across all models, distinct clothing categories like *Bags*, *Trousers*, *Sandals*, *Sneakers*, and *Ankle boots* are classified with very high accuracy. Conversely, categories such as *Shirts*, *T-shirts*, *Pullovers*, and *Coats* present a greater challenge and are frequently misclassified due to their highly similar visual shapes and shared features.

---

## Technologies Used

* **Python**
* **TensorFlow / Keras**
* **Keras Tuner** (Bayesian Optimization)
* **Scikit-learn** (Metrics & Data Splitting)
* **NumPy & Pandas**
* **Matplotlib & Seaborn** (Visualizations & Confusion Matrices)
