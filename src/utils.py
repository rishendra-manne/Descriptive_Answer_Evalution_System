from src.exception import CustomException
import sys
import os

a=1
b=0
try:
    print(a/b)
except Exception as e:
    raise CustomException(e,sys)