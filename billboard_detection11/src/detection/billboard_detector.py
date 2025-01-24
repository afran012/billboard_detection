from tensorflow import keras
import cv2
import numpy as np

class BillboardDetector:
    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)
        
    def detect(self, image):
        preprocessed = self._preprocess(image)
        predictions = self.model.predict(preprocessed)
        return self._process_predictions(predictions)
        
    def _preprocess(self, image):
        img = cv2.resize(image, (224, 224))
        img = img / 255.0
        return np.expand_dims(img, axis=0)
        
    def _process_predictions(self, predictions):
        # Process predictions and return bounding boxes
        return predictions