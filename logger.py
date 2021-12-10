import logging
import os
from logging import Formatter, StreamHandler
from logging.handlers import RotatingFileHandler

from settings import IS_PRINT, LEVEL, LOG_PATH, MAX_BYTES, BACKUP_COUNT


logger = logging.getLogger(__name__)
logger.setLevel(LEVEL)
logger.propagate = False

fmt = Formatter(
    "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s")


if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

fh = RotatingFileHandler(
    filename=f'{LOG_PATH}/err.log', maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
fh.setFormatter(fmt)
fh.setLevel(LEVEL)
logger.addHandler(fh)

if IS_PRINT:
    sh = StreamHandler()
    sh.setLevel(LEVEL)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
