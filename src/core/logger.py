import logging
import os
import sys
from root_path import get_project_root

""""
Logger name is the input name
The log file is created with the same name.
Its location is root_directory / logs / <logger name>.log

print_on_stdio = true if want to print the output at stdio as well.
"""
def get_logger(logger_name: str, print_on_stdio: bool = False):
    # create if log directory doesn't exists
    _create_if_logger_dir_not_exists(get_project_root() / 'logs')

    # create log file path
    _log_path = os.path.join(get_project_root() / 'logs', logger_name)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    if not logger.handlers:
        _file_handler = logging.FileHandler(_log_path)
        _file_handler.setFormatter(formatter)
        logger.addHandler(_file_handler)

    if print_on_stdio:
        _stream_handler = logging.StreamHandler(sys.stdout)
        _stream_handler.setFormatter(formatter)
        logger.addHandler(_stream_handler)
    return logger

def _create_if_logger_dir_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)

logger = get_logger('log.log', True)
logger.info('test again')