import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import Input
from keras.layers import Flatten
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.colab import drive
import os
from PIL import Image

#Connect Google Drive
drive.mount('/content/drive')

#Set dataset path 
data_dir = '/content/drive/MyDrive/character_ocr'

img_height, img_width = 28, 28
batch_size = 64 
num_classes = 34 

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% for validation
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    color_mode='grayscale',  # Assuming your images are grayscale
    batch_size=batch_size,
    class_mode='categorical',
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    color_mode='grayscale',
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation')

model = Sequential()
model.add(Input(shape=(img_height, img_width, 1)))  # Match data generator output
model.add(Flatten())                                # Flatten the 28x28 input to 784
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

#Train Model 
epochs = 20
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Evaluate Model
test_loss, test_acc = model.evaluate(validation_generator)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_acc}")

# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Confusion Matrix
Y_pred = model.predict(validation_generator)
y_pred_classes = np.argmax(Y_pred, axis=1)
y_true = validation_generator.classes
confusion_mtx = confusion_matrix(y_true, y_pred_classes)

# Plot Confusion Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_mtx, annot=True, fmt='d', cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Function to preprocess and predict the digit
def predict_digit(image_path, model, class_indices):
    # Load the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((img_width, img_height))  # Resize to match the model input size
    img_array = np.array(img) / 255.0          # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=(0, -1))  # Add batch and channel dimensions

def predict_digit(image_path, model, class_indices):
    try:
        # Load the image
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img = img.resize((img_width, img_height))  # Resize to match the model input size
        img_array = np.array(img) / 255.0          # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=(0, -1))  # Add batch and channel dimensions

        # Predict the digit
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Map predicted class to label
        label_map = {v: k for k, v in class_indices.items()}  # Reverse the class_indices
        predicted_label = label_map[predicted_class]

        return predicted_label, prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None

from google.colab import files

# Upload a file
uploaded = files.upload()
for file_name in uploaded.keys():
    image_path = file_name
    predicted_label, prediction_confidences = predict_digit(image_path, model, train_generator.class_indices)
    if predicted_label is not None:
        print(f"Predicted Label: {predicted_label}")
        print(f"Prediction Confidence: {prediction_confidences}")
