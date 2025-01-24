from easyocr import Reader
import cv2
import numpy as np

class BillboardTextExtractor:
    def __init__(self):
        self.reader = Reader(['en', 'es'])
        
    def extract_text(self, image):
        preprocessed = self._preprocess_image(image)
        results = self.reader.readtext(preprocessed)
        return self._process_results(results)
        
    def _preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray)
        return denoised
        
    def _process_results(self, results):
        texts = [result[1] for result in results]
        return ' '.join(texts)