import logging
from colorlog.colorlog import ColoredFormatter

from module1.m1 import f1
from module2.m2 import f2

logger = logging.getLogger(__name__)

def setup_logging():
    format_string = (
        '%(log_color)s%(asctime)s:%(name)s:%(levelname)s:'
        '%(filename)s:%(lineno)d:%(funcName)s:%(module)s:%(message)s'
    )

    '''
    We can use the logger.basicConfig, if we are not changing to colored formatter
    When we use the basicConfig, we donr have to do the rest of this function
    '''
    #logging.basicConfig(format=format_string,level=logging.CRITICAL)

    log_colors={
        'DEBUG':    'purple',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'blue',
        #'CRITICAL': 'red,bg_white',
        'CRITICAL': 'red',
    }

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.CRITICAL)
    handler = logging.StreamHandler()

    '''
    no matter what your logging level is, set handler level up 
    for DEBUG, which means it will be used for all levels. 
    Once this is done, then we merely have to
    change the logging level in the respective files 
    for more verbose logging
    '''
    handler.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(format_string, log_colors=log_colors, reset=True)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)


def f3():
    logger.debug('This is DEBUG message from m3,f3')
    logger.info('This is INFO message from m3,f3')
    logger.error('This is ERROR message from m3,f3')
    logger.warning('This is WARNING message from m3,f3')
    logger.critical('This is CRITICAL message from m3,f3')


def start():
    setup_logging()
    f1()
    f2()
    f3()

