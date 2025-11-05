"""
Image Classification Prediction Script
Load trained model and make predictions on new images
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Load the trained model
model = keras.models.load_model('cifar10_cnn_model.h5')

# CIFAR-10 class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']

def preprocess_image(img_path):
    """Preprocess image for prediction"""
    img = Image.open(img_path)
    img = img.resize((32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array, img

def predict_image(img_path):
    """Predict class of an image"""
    img_array, original_img = preprocess_image(img_path)
    
    predictions = model.predict(img_array, verbose=0)
    predicted_class_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class_idx]
    predicted_class = class_names[predicted_class_idx]
    
    return predicted_class, confidence, original_img, predictions[0]

def visualize_prediction(img_path):
    """Visualize prediction with confidence scores"""
    predicted_class, confidence, img, all_predictions = predict_image(img_path)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Original image
    axes[0].imshow(img)
    axes[0].set_title(f'Predicted: {predicted_class}\nConfidence: {confidence:.2%}')
    axes[0].axis('off')
    
    # Confidence scores
    axes[1].barh(class_names, all_predictions)
    axes[1].set_xlabel('Confidence')
    axes[1].set_title('Class Probabilities')
    axes[1].grid(True, axis='x')
    
    plt.tight_layout()
    plt.show()
    
    return predicted_class, confidence

if __name__ == "__main__":
    # Example usage
    if len(os.sys.argv) > 1:
        image_path = os.sys.argv[1]
        if os.path.exists(image_path):
            predicted_class, confidence = visualize_prediction(image_path)
            print(f"\nPrediction: {predicted_class}")
            print(f"Confidence: {confidence:.2%}")
        else:
            print(f"Error: Image file '{image_path}' not found")
    else:
        print("Usage: python predict.py <image_path>")
        print("\nExample: python predict.py test_image.jpg")

