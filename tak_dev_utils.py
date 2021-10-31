import getpass
import os

HOME = f"/home/{getpass.getuser()}"
LOG_FILE_PATH = f"{HOME}/log-files"
BOT_LOG_FILE_NAME = f"{os.path.basename(os.getcwd())}.log"
# BOT_LOG_FILE_NAME_AND_PATH = f"{LOG_FILE_PATH}/{BOT_LOG_FILE_NAME}"
BOT_LOG_FILE_NAME_AND_PATH = f"{BOT_LOG_FILE_NAME}"
