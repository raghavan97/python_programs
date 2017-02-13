import logging
from my_proj.m2.m2_src import m2f

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def m1f():
    logger.critical("Appearing since log level for {} >= DEBUG".format(__name__))
    logger.error("Appearing since log level for {} >= DEBUG".format(__name__))
    logger.warning("Appearing since log level for {} >= DEBUG".format(__name__))
    logger.info("Appearing since log level for {} >= DEBUG".format(__name__))
    logger.debug("Appearing since log level for {} >= DEBUG".format(__name__))
    m2f()
