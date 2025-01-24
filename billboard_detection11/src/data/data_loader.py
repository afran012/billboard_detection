from pyspark.sql.functions import udf
from pyspark.sql.types import BinaryType
import cv2
import numpy as np

class DistributedDataLoader:
    def __init__(self, spark_session):
        self.spark = spark_session
        
    def load_images(self, image_path):
        images_df = self.spark.read.format("image").load(image_path)
        
        @udf(returnType=BinaryType())
        def preprocess_image(binary_data):
            nparr = np.frombuffer(binary_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (224, 224))
            img = img / 255.0
            return img.tobytes()
        
        return images_df.withColumn("processed_image", 
                                  preprocess_image("image"))