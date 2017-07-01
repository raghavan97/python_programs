import logging

from module1.m1 import f1
from module2.m2 import f2

logger = logging.getLogger(__name__)

def setup_logging():
    format_string = (
        '%(asctime)s:%(name)s:%(levelname)s:'
        '%(filename)s:%(lineno)d:%(funcName)s:%(module)s:%(message)s'
    )
    logging.basicConfig(format=format_string,level=logging.DEBUG)

def myfunc1():
    f1()
    f2()

def f3():
    logger.debug('This is DEBUG message from m3,f3')
    logger.info('This is INFO message from m3,f3')
    logger.error('This is ERROR message from m3,f3')
    logger.critical('This is CRITICAL message from m3,f3')


def start():
    setup_logging()
    myfunc1()
    f3()

