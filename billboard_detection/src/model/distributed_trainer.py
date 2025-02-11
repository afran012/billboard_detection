import tensorflow as tf
from src.config.model_config import HYPERPARAMETERS

class DistributedTrainer:
    def __init__(self, model, strategy, train_dataset, val_dataset):
        self.model = model
        self.strategy = strategy
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset

    def compile_model(self):
        with self.strategy.scope():
            self.model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=HYPERPARAMETERS['learning_rate']),
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )

    def train(self):
        with self.strategy.scope():
            history = self.model.fit(
                self.train_dataset,
                validation_data=self.val_dataset,
                epochs=HYPERPARAMETERS['epochs']
            )
        return history

# Usage example
def train_model(model, train_data, val_data):
    strategy = tf.distribute.MirroredStrategy()
    trainer = DistributedTrainer(model, strategy, train_data, val_data)
    trainer.compile_model()
    history = trainer.train()
    return history