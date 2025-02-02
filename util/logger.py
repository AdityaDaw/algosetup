import logging


class CustomLogger:
    @staticmethod
    def create_logger(name: str):
        logger = logging.getLogger(name)
        logger_format = "%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s - %(funcName)10s() : %(message)s"
        logging.basicConfig(format=logger_format, level=logging.DEBUG)
        return logger
