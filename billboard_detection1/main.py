from src.config.spark_config import create_spark_session
from src.data.data_loader import DistributedDataLoader
from src.model.distributed_trainer import DistributedTrainer
from src.model.cnn_model import create_model

def main():
    spark = create_spark_session()
    
    data_loader = DistributedDataLoader(spark)
    
    processed_data = data_loader.load_images("path/to/images")
    
    model = create_model()
    
    trainer = DistributedTrainer(spark, model)
    
    training_data = trainer.prepare_training_data(processed_data)
    
    trainer.train(training_data)

if __name__ == "__main__":
    main()