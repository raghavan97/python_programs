import logging

logger = logging.getLogger(__name__)

def f1():
    logger.debug('This is DEBUG message from m1,f1')
    logger.info('This is INFO message from m1,f1')
    logger.error('This is ERROR message from m1,f1')
    logger.critical('This is CRITICAL message from m1,f1')

