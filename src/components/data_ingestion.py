from src.logger import logging
from src.exception import  CustomException
from dataclasses import dataclass
import numpy as np
import cv2
import os
import sys

@dataclass
class IngestionConfig:
    image_store_path=os.path.join('Descriptive_Answer_Evaluation_System','artifacts','InputData')

