"""this file is intended to create information about the operation of the program and write to the file"""

import functools
import logging

"""determine the format and installation options"""
formatt = "%(asctime)s: %(levelname)s: %(message)s"
logging.basicConfig(filename='rss_parser.log', filemode='a', level=logging.INFO, format=formatt)
logger = logging.getLogger()

"""variables for working with logging"""
log_stream = logging.StreamHandler()
log_stream.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatt)
log_stream.setFormatter(formatter)


def log_decorator(func):
    """decorator to create advanced information about the work of the program when calling --verbose"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"Start function  {func.__name__}. args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            logger.info(f"Finish function  {func.__name__}. args={args}, kwargs={kwargs} return  result {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__} args={args}, kwargs={kwargs}. exception: {str(e)}")

    return wrapper