# Image Classification ML Model

Deep learning model for image classification using Convolutional Neural Networks (CNN). Trained on the CIFAR-10 dataset with data augmentation and transfer learning techniques.

## Features

- **CNN Architecture**: Multi-layer convolutional neural network with batch normalization
- **Data Augmentation**: Rotation, shifting, flipping, and zooming for better generalization
- **Transfer Learning Ready**: Architecture can be adapted for transfer learning
- **Comprehensive Evaluation**: Includes confusion matrix, classification report, and visualizations
- **Model Persistence**: Save and load trained models

## Dataset

The model is trained on the CIFAR-10 dataset, which contains 60,000 32x32 color images in 10 classes:
- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run training:
```bash
python train_model.py
```

## Model Architecture

The CNN model consists of:
- **3 Convolutional Blocks**: Each with 2 Conv2D layers, BatchNormalization, MaxPooling, and Dropout
- **Dense Layers**: 512 and 256 neurons with dropout regularization
- **Output Layer**: 10 neurons (one for each class) with softmax activation

## Training

The model uses:
- **Optimizer**: Adam with learning rate 0.001
- **Loss Function**: Categorical crossentropy
- **Callbacks**: Early stopping, learning rate reduction, and model checkpointing
- **Data Augmentation**: Applied during training to prevent overfitting

## Usage

### Training

```bash
python train_model.py
```

This will:
- Load and preprocess the CIFAR-10 dataset
- Train the CNN model
- Generate evaluation metrics
- Save the model as `cifar10_cnn_model.h5`
- Create visualization plots:
  - `training_history.png`: Training/validation accuracy and loss
  - `confusion_matrix.png`: Confusion matrix
  - `predictions.png`: Sample predictions

### Prediction

```bash
python predict.py <image_path>
```

Example:
```bash
python predict.py test_image.jpg
```

## Model Performance

The model achieves:
- **Test Accuracy**: ~85-90% (depending on training)
- **Training Time**: ~30-60 minutes on CPU, ~5-10 minutes on GPU

## Output Files

- `cifar10_cnn_model.h5`: Trained model
- `best_model.h5`: Best model checkpoint
- `training_history.png`: Training curves
- `confusion_matrix.png`: Confusion matrix visualization
- `predictions.png`: Sample predictions

## Future Enhancements

- Transfer learning with pre-trained models (ResNet, VGG, etc.)
- Fine-tuning on custom datasets
- Real-time prediction API
- Web interface for image upload and prediction

## Technologies Used

- TensorFlow/Keras: Deep learning framework
- NumPy: Numerical computations
- Matplotlib/Seaborn: Visualizations
- Scikit-learn: Evaluation metrics
- PIL: Image processing

