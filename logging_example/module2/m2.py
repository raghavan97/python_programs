import logging

logger = logging.getLogger(__name__)

def f2():
    logger.setLevel(logging.ERROR)
    logger.debug('This is DEBUG message from m2,f2')
    logger.info('This is INFO message from m2,f2')
    logger.error('This is ERROR message from m2,f2')
    logger.critical('This is CRITICAL message from m2,f2')
