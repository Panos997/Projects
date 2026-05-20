# Deep Learning Bone X-Ray Classification

## Overview

Deep Learning Bone X-Ray Classification is an experimental deep learning project for classifying bone X-ray images as **positive** or **negative** using the MURA dataset.

The project focuses on building and testing a custom Convolutional Neural Network (CNN) workflow for medical image classification.

The notebook does not compare pretrained architectures such as ResNet, EfficientNet, DenseNet, or VGG. Instead, it experiments with a custom CNN model and tunes some of its training and architecture-related hyperparameters.

The project was developed in Google Colab using TensorFlow, Keras, and Keras Tuner.

---

# Project Goal

The main goal of this project is to test how a custom CNN model can classify musculoskeletal X-ray images as normal or abnormal.

The project explores CNN training on the MURA dataset through:

- dataset preprocessing
- train / validation / test preparation
- image loading
- image normalization
- simple image augmentation
- custom CNN model creation
- hyperparameter tuning
- model training
- model evaluation
- prediction analysis by body part

The project is an experimentation notebook, not a production-ready medical diagnosis system.

---

# Dataset

The project uses the MURA dataset.

MURA stands for:

```text
Musculoskeletal Radiographs
```

The dataset contains X-ray images from different body parts, including:

- elbow
- finger
- forearm
- hand
- humerus
- shoulder
- wrist

Each image belongs to one of two classes:

```text
positive
negative
```

In this project:

- `positive` means abnormal
- `negative` means normal

The notebook reads the official MURA CSV files:

```text
train_image_paths.csv
valid_image_paths.csv
```

These files contain the image paths used to build the training, validation, and test datasets.

---

# What the Project Does

The project follows this workflow:

```text
MURA CSV files
      ↓
Image path preprocessing
      ↓
Metadata extraction
      ↓
Train / validation / test split
      ↓
Folder creation by class
      ↓
Image loading with TensorFlow
      ↓
Image normalization and augmentation
      ↓
Custom CNN training
      ↓
Hyperparameter tuning
      ↓
Model evaluation
      ↓
Prediction analysis
```

The final goal is to train a CNN model that can classify X-ray images into:

```text
positive
negative
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | Neural network API |
| Keras Tuner | Hyperparameter tuning |
| TensorFlow Addons | Additional metrics |
| Pandas | CSV and dataframe processing |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| Seaborn | Data visualization |
| Scikit-learn | Train/test split and evaluation metrics |
| PIL | Image loading and saving |
| Google Colab | Notebook execution environment |
| Google Drive | Dataset storage |

---

# Project Structure

```text
Deep Learning Bone X-Ray Classification/
│
├── Code.ipynb
└── README.md
```

---

# File Explanation

## `Code.ipynb`

This is the main notebook of the project.

It contains the complete workflow:

- library installation
- imports
- Google Drive mounting
- MURA CSV loading
- dataset metadata extraction
- train/test splitting
- folder creation for image datasets
- TensorFlow dataset loading
- normalization
- random image augmentation
- CNN model definition
- hyperparameter tuning with Keras Tuner
- model training
- model evaluation
- predictions on the test set
- body-part-level analysis

---

# How to Run the Project

## 1. Open the Notebook

Open:

```text
Code.ipynb
```

using Google Colab.

The notebook is designed to work mainly in a Colab environment because it uses:

```python
from google.colab import drive
drive.mount('/content/drive/')
```

---

## 2. Mount Google Drive

The dataset should be stored in Google Drive.

The notebook mounts Drive so it can access the MURA files.

---

## 3. Configure Dataset Path

Inside the notebook, the dataset path is set manually.

Example:

```python
path = '../MURA-v1.1'
```

You may need to change this path depending on where the dataset is stored in your Google Drive.

---

## 4. Run the Notebook Cells

Run the notebook cells in order.

The notebook will:

1. load the MURA CSV files
2. extract metadata from image paths
3. split part of the training data into a test set
4. create image folders for positive and negative classes
5. load images using TensorFlow
6. normalize image values
7. apply simple augmentation
8. train a CNN model
9. evaluate the model
10. generate predictions

---

# Technical Details

## Dataset Loading

The notebook reads the MURA image path CSV files using Pandas:

```python
train = pd.read_csv(os.path.join(path, "train_image_paths.csv"), dtype=str, header=None)
valid = pd.read_csv(os.path.join(path, "valid_image_paths.csv"), dtype=str, header=None)
```

The CSV files are then converted into dataframes with one main column:

```python
image_path
```

---

## Metadata Extraction

The notebook extracts useful metadata from each image path.

The extracted fields include:

- body part
- patient ID
- folder ID
- study type
- label

Example:

```python
train['Body_Part'] = train['image_path'].apply(lambda x: x.split('/')[2])
train['PatientId'] = train['image_path'].apply(lambda x: x.split('/')[3].replace('patient',''))
train['FolderId'] = train['image_path'].map(lambda x: x.split('/')[-2])
train['Study'] = train['FolderId'].map(lambda x: x.split('_')[0])
train['label'] = train['image_path'].map(lambda x:'positive' if 'positive' in x else 'negative')
```

This allows the project to analyze the dataset by class, patient, and body part.

---

## Dataset Analysis

The notebook checks:

- missing values
- number of images
- number of patients
- number of labels
- positive cases
- negative cases
- body part distribution

This helps understand the dataset before training the model.

---

## Train / Test Split

The notebook creates a test set from the training dataframe using Scikit-learn:

```python
train, test = train_test_split(
    train,
    test_size=0.15,
    random_state=1888
)
```

This means that 15% of the training data is separated and used as a test set.

---

## Folder Preparation

The notebook creates folders for each dataset split and class.

Example structure:

```text
Train/
├── Positive/
└── Negative/

Valid/
├── Positive/
└── Negative/

Test/
├── Positive/
└── Negative/
```

Images are copied/saved into the correct folders based on their label.

This is done so TensorFlow can later load the images using folder names as labels.

---

## Image Loading

The notebook loads the datasets using:

```python
tf.keras.utils.image_dataset_from_directory()
```

Images are loaded as RGB images with size:

```text
128 x 128
```

The batch size is:

```text
32
```

Example:

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    directory=path,
    labels="inferred",
    color_mode="rgb",
    batch_size=32,
    image_size=(128, 128)
)
```

---

## Image Normalization

The notebook normalizes image pixel values using:

```python
tf.keras.layers.Rescaling(1./255)
```

This converts pixel values from the range:

```text
0 - 255
```

to:

```text
0 - 1
```

Normalization helps the neural network train more effectively.

---

## Image Augmentation

The notebook applies simple image augmentation using TensorFlow layers:

```python
tf.keras.layers.RandomFlip("horizontal_and_vertical")
tf.keras.layers.RandomRotation(factor=(-1/12, 1/12))
```

The augmentation includes:

- random horizontal and vertical flipping
- random rotation

In the notebook, these transformations are applied to the train, validation, and test datasets.

---

## Dataset Performance Optimization

The notebook improves dataset loading performance using:

```python
cache()
prefetch()
```

with:

```python
tf.data.AUTOTUNE
```

This helps the model receive data more efficiently during training.

---

# CNN Model

The project uses a custom CNN model created with the Keras Functional API.

The model is defined inside a custom Keras Tuner hypermodel class:

```python
class MyCNNHyperModel(kt.HyperModel):
```

The model includes:

- input layer
- convolutional layers
- max pooling layers
- optional batch normalization
- optional dropout
- flatten layer
- output dense layer

The model performs binary classification using:

```python
binary_crossentropy
```

as the loss function.

The output layer uses:

```python
sigmoid
```

activation because the task is binary classification.

---

# What Is Actually Tuned

The notebook tunes a custom CNN model.

It does not compare different pretrained model families.

The tuned parameters include:

## Number of Convolutional Layers

```python
hp.Int('convolutional layers', 2, 5)
```

This means the tuner can test CNN depth from:

```text
2 to 5 convolutional layers
```

---

## Activation Function

```python
hp.Choice('activation_function', ['relu', 'tanh'])
```

The notebook can test:

```text
relu
tanh
```

---

## Kernel Initializer

```python
hp.Choice('kernel_initializer', ['glorot_uniform', 'glorot_normal'])
```

The notebook can test:

```text
glorot_uniform
glorot_normal
```

---

## Dropout Rate

```python
hp.Float('dropout_rate', 0, 0.5)
```

The notebook can test dropout values between:

```text
0 and 0.5
```

---

## Learning Rate

```python
hp.Float("lr", 0.00001, 0.001)
```

The notebook can test learning rate values between:

```text
0.00001 and 0.001
```

---

# What Is Not Tuned

The notebook clearly states that the basic CNN architecture is not fully hypertuned.

The following are not tuned:

- filter formula
- kernel size
- pooling size
- stride values
- full architecture family

The CNN uses a fixed pattern where the number of filters increases with each convolutional layer:

```python
filters = 8 * (2 ** i)
```

The convolution kernel size is fixed as:

```python
(3, 3)
```

The max pooling size is fixed as:

```python
(2, 2)
```

---

# Hyperparameter Tuning

The notebook uses Keras Tuner with Bayesian Optimization:

```python
kt.BayesianOptimization()
```

The tuning objective is:

```python
val_f1_score
```

However, in the notebook this metric is implemented using TensorFlow Addons Cohen Kappa:

```python
tfa.metrics.CohenKappa(name="val_f1_score", num_classes=2)
```

So the metric name is `val_f1_score`, but the underlying metric is Cohen Kappa.

The actual tuner configuration shown in the notebook uses:

```python
max_trials=1
```

This means the tuning run is very limited and should be understood as a small experiment, not a full benchmark search.

---

# Training Setup

The actual model configuration used in the notebook is:

```python
MyCNNHyperModel(True, Adam, True)
```

This means:

- dropout is enabled
- Adam optimizer is used
- batch normalization is enabled

The model is trained with:

```python
model.fit()
```

using:

- training dataset
- validation dataset
- early stopping
- learning rate reduction on plateau

---

# Callbacks

The notebook uses two main callbacks:

## Early Stopping

```python
tf.keras.callbacks.EarlyStopping()
```

This stops training when validation performance stops improving.

## Reduce Learning Rate on Plateau

```python
tf.keras.callbacks.ReduceLROnPlateau()
```

This reduces the learning rate when validation performance stops improving.

---

# Evaluation

The notebook evaluates the trained model on the test dataset using:

```python
model.evaluate(test_ds)
```

It also generates predictions using:

```python
model.predict_generator(test_ds)
```

The predictions are rounded into binary labels:

```python
0 = negative
1 = positive
```

---

# Body-Part Analysis

After prediction, the notebook compares predictions with the real labels and performs analysis by body part.

The body parts analyzed are:

```text
XR_ELBOW
XR_FINGER
XR_FOREARM
XR_HAND
XR_HUMERUS
XR_SHOULDER
XR_WRIST
```

The notebook generates confusion matrices for each body part.

This helps evaluate whether the model performs differently across different types of X-ray images.

---

# Example Workflow

```text
X-ray image
    ↓
Resize to 128x128
    ↓
Normalize pixel values
    ↓
Apply augmentation
    ↓
Pass through CNN
    ↓
Generate probability
    ↓
Convert probability to class
    ↓
Positive / Negative prediction
```

---

# What This Project Demonstrates

This project demonstrates:

- medical image classification with CNNs
- working with the MURA X-ray dataset
- image path preprocessing
- folder-based dataset creation
- TensorFlow image dataset loading
- image normalization
- simple image augmentation
- custom CNN model creation
- limited hyperparameter tuning with Keras Tuner
- binary classification
- model evaluation
- confusion matrix analysis by body part

---

# Important Notes

This project is an educational and experimental deep learning notebook.

It should not be used as a real medical diagnosis tool.

The notebook does not compare pretrained architectures such as ResNet, EfficientNet, DenseNet, or VGG.

The main experiment is based on a custom CNN model with selected hyperparameters tuned through Keras Tuner.

---

# Conclusion

Deep Learning Bone X-Ray Classification is an experimental CNN-based medical imaging project that classifies MURA bone X-ray images as positive or negative.

The project demonstrates the full workflow of loading medical image data, preparing datasets, training a custom CNN model, tuning selected hyperparameters, and evaluating predictions by body part.

It is mainly useful as a learning and experimentation project for deep learning, medical image classification, and TensorFlow/Keras workflows.
