import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def f2():
    logger.debug('This is DEBUG message from m2,f2')
    logger.info('This is INFO message from m2,f2')
    logger.error('This is ERROR message from m2,f2')
    logger.warning('This is WARNING message from m3,f3')
    logger.critical('This is CRITICAL message from m2,f2')
