import logging
import os


BASE_DIR = os.path.dirname(__file__)
COMMAND_DIR = os.path.join(BASE_DIR, 'command')
PIDFILE = '/tmp/'

# logging
LOG_PATH = f'{BASE_DIR}/logs'
LEVEL = logging.DEBUG
IS_PRINT = False
MAX_BYTES = 1024*1024*10
BACKUP_COUNT = 10
