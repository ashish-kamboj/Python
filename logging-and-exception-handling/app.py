from logger import logging_and_exception_handling
import math_module

log_obj = logging_and_exception_handling.Logger()
log = log_obj.setup_applevel_logger(file_name = "app_debug.log")

dividend = int(input("Enter Dividend : "))
divisor = int(input("Enter Divisor : "))

log.info(f"Calling module function")
quotient = math_module.division(dividend, divisor)

log.info(f"Result of {dividend} divide by {divisor} is {quotient} ")
log.info(f"Division Completed!")