import logging
from log import get_logger

logger = get_logger(__file__)
logger.setLevel(logging.INFO)

def m2_f():
    logger.debug("This will not appear since in module:m2 the log level is INFO")
    logger.info("This will appear since in module:m2 the log level is INFO")
