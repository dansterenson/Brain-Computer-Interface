import logging


def create_logger(file_name, level=logging.INFO, formatter='%(asctime)s:%(levelname)s:%(message)s'):
    logging.basicConfig(filename=f'./log_files/{file_name}.log', level=level, format=formatter)
    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(level)
    # set a format which is simpler for console use
    formatter = logging.Formatter(formatter)
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    return logging.getLogger(__name__)