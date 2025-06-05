import os
import sys
from src.logger import logging

def display_error_message(error,error_deatil:sys):
    _,_,exc_tab=error_deatil.exc_info()
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_message=f"Error occured in python script name [{file_name}] line number [{exc_tab.tb_lineno}] error message[{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_msg = display_error_message(error_message,error_detail)
        logging.error(self.error_msg)

    def __str__(self):
        return self.error_msg

