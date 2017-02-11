import logging
from log import get_logger

from m2.m2_file import m2_f

logger = get_logger(__file__)
logger.setLevel(logging.DEBUG)

def m1_f():
    logger.debug("This will appear since in module:m1 debug and above are enabled")
    m2_f()
    logger.info("This will appear since in module:m1 debug and above are enabled")
