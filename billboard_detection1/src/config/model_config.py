# Model configuration settings for the billboard detection project

class ModelConfig:
    def __init__(self):
        self.input_shape = (224, 224, 3)  # Input shape for the model
        self.num_classes = 10  # Number of output classes
        self.learning_rate = 0.001  # Learning rate for the optimizer
        self.batch_size = 32  # Batch size for training
        self.epochs = 10  # Number of training epochs
        self.dropout_rate = 0.5  # Dropout rate for regularization

    def get_model_parameters(self):
        return {
            "input_shape": self.input_shape,
            "num_classes": self.num_classes,
            "learning_rate": self.learning_rate,
            "batch_size": self.batch_size,
            "epochs": self.epochs,
            "dropout_rate": self.dropout_rate,
        }