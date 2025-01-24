from pyspark.sql.functions import col
import tensorflow as tf

class DistributedTrainer:
    def __init__(self, spark_session, model):
        """
        Inicializa el entrenador distribuido.
        
        Parameters:
            spark_session: Sesión activa de Spark
            model: Modelo de TensorFlow
        """
        self.spark = spark_session
        self.model = model
        
    def prepare_training_data(self, processed_df):
        """
        Prepara los datos procesados para el entrenamiento.
        
        Parameters:
            processed_df: DataFrame de Spark con imágenes procesadas
        """
        def convert_to_tf_dataset(partition):
            for row in partition:
                image = tf.io.decode_raw(row.processed_image, tf.float32)
                image = tf.reshape(image, [224, 224, 3])
                yield image, row.label
        
        dataset = processed_df.rdd.mapPartitions(convert_to_tf_dataset)
        return dataset.collect()
    
    def train(self, training_data, epochs=10, batch_size=32):
        """
        Entrena el modelo usando los datos distribuidos.
        
        Parameters:
            training_data: Datos de entrenamiento preparados
            epochs: Número de épocas de entrenamiento
            batch_size: Tamaño del batch
        """
        tf_dataset = tf.data.Dataset.from_tensor_slices(training_data)
        tf_dataset = tf_dataset.batch(batch_size)
        
        self.model.fit(tf_dataset, epochs=epochs)