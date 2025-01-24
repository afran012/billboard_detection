from pyspark.sql.functions import udf
from pyspark.sql.types import BinaryType
import cv2
import numpy as np

class DistributedDataLoader:
    def __init__(self, spark_session):
        """
        Inicializa el cargador de datos distribuido.
        
        Parameters:
            spark_session: Sesión activa de Spark
        """
        self.spark = spark_session
        
    def load_images(self, image_path):
        """
        Carga imágenes de forma distribuida usando Spark.
        
        Parameters:
            image_path: Ruta al directorio de imágenes
        """
        # Creamos un DataFrame de Spark con las rutas de las imágenes
        images_df = self.spark.read.format("image").load(image_path)
        
        # Definimos una función UDF para preprocesar imágenes
        @udf(returnType=BinaryType())
        def preprocess_image(binary_data):
            # Convertimos los bytes a una imagen numpy
            nparr = np.frombuffer(binary_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Realizamos el preprocesamiento
            img = cv2.resize(img, (224, 224))
            img = img / 255.0  # Normalización
            
            return img.tobytes()
        
        # Aplicamos el preprocesamiento de forma distribuida
        return images_df.withColumn("processed_image", 
                                  preprocess_image("image"))