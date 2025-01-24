from src.config.spark_config import create_spark_session
from src.data.data_loader import DistributedDataLoader
from src.detection.billboard_detector import BillboardDetector
from src.detection.size_calculator import BillboardSizeCalculator
from src.detection.text_extractor import BillboardTextExtractor

def main():
    # Inicializar Spark
    spark = create_spark_session()
    
    # Crear instancias
    data_loader = DistributedDataLoader(spark)
    detector = BillboardDetector('path/to/model')
    camera_params = {'camera_matrix': ..., 'dist_coeffs': ...}  # Define camera parameters
    size_calculator = BillboardSizeCalculator(camera_params)
    text_extractor = BillboardTextExtractor()
    
    # Cargar y procesar imágenes
    images = data_loader.load_images('path/to/images')
    
    # Procesar cada imagen
    for image in images.collect():
        # Detectar valla
        bbox = detector.detect(image)
        
        # Calcular dimensiones
        width, height = size_calculator.calculate_real_size(
            bbox, distance=10.0
        )
        
        # Extraer texto
        text = text_extractor.extract_text(image)
        
        print(f"Dimensiones: {width}cm x {height}cm")
        print(f"Texto: {text}")

if __name__ == "__main__":
    main()