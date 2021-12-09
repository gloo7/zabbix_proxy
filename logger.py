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

log_path = os.path.join(LOG_PATH, __name__)

if not os.path.exists(log_path):
    os.makedirs(log_path)

fh = RotatingFileHandler(
    filename=f'{log_path}/err', maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
fh.setFormatter(fmt)
fh.setLevel(LEVEL)
logger.addHandler(fh)

if IS_PRINT:
    sh = StreamHandler()
    sh.setLevel(LEVEL)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
