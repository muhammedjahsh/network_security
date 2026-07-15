import sys
from network_security.logging import logger
class NetworkSecurityException(Exception):
    """Base class for network security exceptions."""
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename 

    def __str__(self):
        return "Error occurred in script: [{0}] at line number: [{1}] error message: [{2}]".format(self.file_name,self.lineno,self.error_message)
    

if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log message")
        a=1/0
        print("this will not be preinted",a)
    except Exception as e:
        raise NetworkSecurityException("This is a custom exception",sys) from e