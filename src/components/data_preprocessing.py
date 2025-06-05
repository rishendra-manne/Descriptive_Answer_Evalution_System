from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import tensorflow as tf
import os
import sys

@dataclass
class PreprocessingConfig:
    image_size=(224,224)
    normalizing_factor=225
    nun_channels=3
    shuffle_factor=100

class DataPreprocessing:

    def __init__(self):
        self.preprocessing_config=PreprocessingConfig()

    def process_img(self,path:str):
        logging.info("starting to load and preprocess the image")
        try:
            img=tf.io.read_file(path)
            img=tf.image.decode_jpeg(img,channels=self.preprocessing_config.nun_channels)
            img=tf.image.resize(img,self.preprocessing_config.image_size)
            img=img/self.preprocessing_config.normalizing_factor
            logging.info("preprocessing the image is success")
            return img

        except Exception as e:

            logging.info("failed to load the image")
            raise CustomException(e,sys)
    def get_image_paths(self,path:str):
        logging.info("trying to get the image paths....")
        try:
            train_images_paths=[os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]
            logging.info("obtaining image paths is successful")

            return train_images_paths

        except Exception as e:
            logging.info("failed to get the image paths")
            raise CustomException(e,sys)

    def load_and_combine_data(self,image_paths:list[str],batch_size:int):
        logging.info("starting data loading")
        try:

            data = tf.data.Dataset.from_tensor_slices(image_paths)
            data = data.map(lambda path: self.process_img(path),
                                      num_parallel_calls=tf.data.experimental.AUTOTUNE)
            dataset = data.batch(batch_size, drop_remainder=True).prefetch(tf.data.experimental.AUTOTUNE)
            dataset = dataset.shuffle(self.preprocessing_config.shuffle_factor)

            train_ds = tf.data.Dataset.zip((cover_dataset, hide_dataset))
            logging.info("data loading and combining are success")
            return train_ds
        except Exception as e:
            logging.info("data loading and combining failed")
            raise CustomException(e,sys)