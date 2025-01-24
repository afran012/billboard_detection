# TensorFlow utility functions for the billboard detection project

import tensorflow as tf

def load_model(model_path):
    """
    Carga un modelo de TensorFlow desde la ruta especificada.
    
    Parameters:
        model_path: Ruta al modelo guardado.
    
    Returns:
        model: Modelo de TensorFlow cargado.
    """
    model = tf.keras.models.load_model(model_path)
    return model

def save_model(model, model_path):
    """
    Guarda un modelo de TensorFlow en la ruta especificada.
    
    Parameters:
        model: Modelo de TensorFlow a guardar.
        model_path: Ruta donde se guardará el modelo.
    """
    model.save(model_path)

def preprocess_input(image):
    """
    Preprocesa la imagen de entrada para el modelo.
    
    Parameters:
        image: Imagen de entrada en formato numpy.
    
    Returns:
        image: Imagen preprocesada.
    """
    image = tf.image.resize(image, [224, 224])  # Redimensionar
    image = image / 255.0  # Normalización
    return image

def postprocess_output(output):
    """
    Postprocesa la salida del modelo.
    
    Parameters:
        output: Salida del modelo.
    
    Returns:
        output: Salida postprocesada.
    """
    return tf.argmax(output, axis=-1)  # Obtener la clase con mayor probabilidad