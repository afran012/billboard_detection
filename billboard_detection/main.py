from src.data.data_loader import load_data
from src.data.preprocessing import preprocess_data
from src.detection.billboard_detector import BillboardDetector
from src.model.cnn_model import CNNModel
from src.model.distributed_trainer import train_model

def main():
    # Load the data
    raw_data = load_data('data/raw/')
    
    # Preprocess the data
    processed_data = preprocess_data(raw_data)
    
    # Initialize the model
    model = CNNModel(input_shape=(224, 224, 3), num_classes=10)
    
    # Train the model
    train_model(model.model, processed_data, None)
    
    # Detect billboards in new images
    detector = BillboardDetector(model.model)
    results = detector.detect_billboards('path/to/new/images/')
    
    # Output results
    print("Detection results:", results)

if __name__ == "__main__":
    main()