from src.logger import logging
from src.exception import  CustomException
from huggingface_hub import snapshot_download
from dataclasses import dataclass
import numpy as np
import cv2
import os
import sys

@dataclass
class IngestionConfig:
    image_store_path=os.path.join('Descriptive_Answer_Evaluation_System','artifacts','InputData')
    train_data_path=os.path.join('Descriptive_Answer_Evaluation_System','artifacts','training_data')

class DataIngestion:

    def __init__(self,repo_id:str,token:str):
        self.ingestion_config=IngestionConfig()
        self.repo_id=repo_id
        self.access_token=token

    def get_data(self):
        """

        :return: returns the tuple containing path of cover data and hide data
        """
        logging.info("starting to download the data from hugging face datasets")
        try:
            snapshot_download(
                repo_id=self.repo_id,
                repo_type="dataset",
                token=self.access_token,  # required for private datasets
                local_dir=self.ingestion_config.train_data_path
            )
            logging.info("dataset download successful")
            return self.ingestion_config.train_data_path

        except Exception as e:
            logging.info("failed to download the data")
            raise CustomException(e,sys)






