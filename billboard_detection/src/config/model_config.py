# Configuration settings for the model

MODEL_PATH = "data/models/billboard_model.h5"
HYPERPARAMETERS = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 50,
    "input_shape": (224, 224, 3),
    "num_classes": 10
}