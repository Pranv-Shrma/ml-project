# this will be common for all the scripts in this code in every try catch block

import sys 
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()   # we dont need the first two values, we need the third value which is the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))   # [{n}] - these are placeholders, they will be replaced by values in the order we pass them

    return error_message

class CustomException(Exception):  # inheriting from Exception class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # this will call the constructor of the parent class (Exception class)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message



# TESTING
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)
    
