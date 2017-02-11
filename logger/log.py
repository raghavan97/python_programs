import logging
from colorlog import ColoredFormatter


mapper = {}

def get_logger(phrase):
    if phrase in mapper:
        return mapper[phrase]

    formatter = ColoredFormatter(
        '%(log_color)s%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(reset)s %(message)s',
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )

    logger = logging.getLogger(phrase)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    mapper[phrase] = logger

    return logger

