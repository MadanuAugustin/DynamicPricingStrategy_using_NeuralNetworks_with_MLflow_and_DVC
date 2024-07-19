import os
import sys
import logging

####################################--------------Logger File-----------------------###############################################

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"


log_dir = 'logs'

log_filepath = os.path.join(log_dir, 'running_logs.log')

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('dynamicPricingStrategy')


####################################---------Exception Class------------------##################################################3



class CustomException(Exception):
    def __init__(self, errormsg , system_error : sys):
        super().__init__(errormsg)
        self.errormsg = errormsg_function(errormsg = errormsg, system_error = system_error)


    def __str__(self):
        
        return self.errormsg
    


def errormsg_function(errormsg , system_error: sys):
    _,_,exc_tb = system_error.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    errormsg = "Error has been raised in the filename of {} and the linenbr is {} errormsg : {}".format(filename, lineno, str(errormsg))
    return errormsg