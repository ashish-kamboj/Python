#import logger

from logger import logging_and_exception_handling

log_obj = logging_and_exception_handling.Logger()
#raise_obj = logging_and_exception_handling.value_exception(None, None)


#log = logger.get_logger(__name__)
log = log_obj.get_logger()

def division(numerator, denominator): # just multiply two numbers
    if(denominator == 0):
        log.error(f"Denominator is O, Divison is not possible!!")
        raise logging_and_exception_handling.ValueException("Denominator is O, Divison is not possible", None)
    else:
        log.info(f"Executing division function")
        return numerator/denominator