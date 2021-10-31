# setup_logger.py
import logging

from tak_dev_utils import BOT_LOG_FILE_NAME, BOT_LOG_FILE_NAME_AND_PATH

formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                              '%m-%d %H:%M:%S')

logging.basicConfig(filename=BOT_LOG_FILE_NAME_AND_PATH,
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in function %(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.WARNING
                    )
logger = logging.getLogger(BOT_LOG_FILE_NAME)
