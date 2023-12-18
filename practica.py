import tensorflow as tf
import matplotlib as plt
from keras.preprocessing.image import ImageDataGenerator

import os
import csv
import datetime
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, GlobalAveragePooling2D, Dense, Flatten, BatchNormalization, LayerNormalization
from keras.optimizers import SGD, Adam, Adamax
from keras.initializers import he_normal
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = 'animals_dataset/animals/animals'

np.random.seed(42)
tf.random.set_seed(314)

batch_size = 128
n_epochs = 50
learning_rate = 0.1
mom = 0.8
patience=5

datagen = ImageDataGenerator(
    rescale=1 / 255.0,
    validation_split=0.2)

train_generator = datagen.flow_from_directory(
    directory=os.path.join(DATASET_PATH),
    color_mode="rgb",
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=True,
    seed=42,
    subset='training')

val_generator = datagen.flow_from_directory(
    directory=os.path.join(DATASET_PATH),
    color_mode="rgb",
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=True,
    seed = 42,
    subset='validation')

# Obtén un lote de imágenes y etiquetas del generador de entrenamiento
x_batch, y_batch = train_generator.next()

# Muestra la primera imagen del lote
for i in range(10):
    plt.imshow(x_batch[i])
    label_index = int(y_batch[i].argmax())
    # Obtiene el nombre de la etiqueta a partir del índice usando class_indices
    class_labels = list(train_generator.class_indices.keys())
    label = class_labels[label_index]
    plt.title(f'Clase: {label}')
    plt.axis('off')  # Desactiva los ejes
    plt.show()

