import logging
from colorlog import ColoredFormatter
from my_proj.m1.m1_src import m1f
from my_proj.m2.m2_src import m2f

def setup_logger():
    formatter = ColoredFormatter(
        '%(log_color)s%(asctime)s:%(levelname)s:%(name)s:%(lineno)s'
        ':%(reset)s%(message)s'
    )

    logger = logging.getLogger('my_proj')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

def main():
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    logger.critical("Appearing since log level for {} >= ERROR".format(__name__))
    logger.error("Appearing since log level for {} >= ERROR".format(__name__))
    logger.warning("Not appearing since log level for {} >= ERROR".format(__name__))
    logger.info("Not appearing since log level for {} >= ERROR".format(__name__))
    logger.debug("Not appearing since log level for {} >= ERROR".format(__name__))
    m1f()
    print logging.getLogger().manager.loggerDict.keys()


