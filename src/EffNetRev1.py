import efficientnet.keras as efn
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.python.keras.optimizers import adam_v2
import tensorflow as tf
import os

# Assuming CEC_2025_dataset is an environment variable
dataset_path = os.getenv('CEC_2025_dataset')
dataset_path = os.path.join(dataset_path, 'yes')
#no_data_path = os.path.join(dataset_path, 'no')

# Load the EfficientNetB0 model with pre-trained ImageNet weights
base_model = efn.EfficientNetB0(weights='imagenet', include_top=False)

# Add custom layers on top of the base model
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)  # Two classes: yes and no

# Create the full model
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer=adam_v2.Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Function to preprocess the images
def preprocess_image(image, label):
    image = tf.image.resize(image, (224, 224))
    image = image / 255.0  # Rescale pixel values
    return image, label

# Function to load the dataset
def load_dataset(data_path, batch_size=32):
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_path,
        image_size=(224, 224),
        batch_size=batch_size,
        label_mode='categorical'
    )
    dataset = dataset.map(preprocess_image)
    return dataset

# Load the datasets
train_dataset = load_dataset(dataset_path)
val_dataset = load_dataset(dataset_path)

# Train the model
model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=10  # Adjust the number of epochs as needed
)
