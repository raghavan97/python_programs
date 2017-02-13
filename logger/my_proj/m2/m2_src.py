import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def m2f():
    logger.critical("Appearing since log level for {} >= INFO".format(__name__))
    logger.error("Appearing since log level for {} >= INFO".format(__name__))
    logger.warning("Appearing since log level for {} >= INFO".format(__name__))
    logger.info("Appearing since log level for {} >= INFO".format(__name__))
    logger.debug("Not Appearing since log level for {} >= INFO".format(__name__))
