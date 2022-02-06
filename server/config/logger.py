import logging


def factory_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    return logger


def get_logger():
    logger = logging.getLogger()
    return logger
