import atexit
import os
import signal
import sys
from typing import Callable, List, Optional
from pathlib import Path
from pydantic import ValidationError

from logger import logger
from settings import COMMAND_DIR

from .collector.collector import init_collector
from ._typing import D, Collector, Process, Handler
from .config import Config
from .handler.handler import init_handlers
from .parser.parser import init_parser
from .rewriter.rewriter import init_rewriters


class Task:
    collector: Collector
    parser: Optional[Process] = None
    rewriters: Optional[List[Process]] = None
    handlers: List[Handler]

    @classmethod
    def daemonize(cls, command: str, stdin: str = '/dev/null', stdout: str = '/dev/null', stderr: str = '/dev/null') -> None:
        pidfile = f'/tmp/{command}'
        if os.path.exists(pidfile):
            logger.error('Already running')
            sys.exit(1)

        # First fork (detaches from parent)
        try:
            if os.fork() > 0:
                sys.exit(1)
        except OSError as e:
            logger.error('fork #1 failed.')
            sys.exit(1)

        os.chdir('/')
        os.umask(0)
        os.setsid()
        # Second fork (relinquish session leadership)
        try:
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            logger.error('fork #2 failed.')
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()

        with open(stdin, 'rb', 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open(stdout, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open(stderr, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stderr.fileno())

        # Write the PID file
        with open(pidfile, 'w') as f:
            print(os.getpid(), file=f)

        # Arrange to have the PID file removed on exit/signal
        atexit.register(lambda: os.remove(pidfile))

        # Signal handler for termination (required)
        def sigterm_handler(signo, frame):
            sys.exit(1)

        signal.signal(signal.SIGTERM, sigterm_handler)

    @classmethod
    def start(cls, command: str, params: Optional[List[str]] = None) -> None:
        command_dir = Path(COMMAND_DIR)
        try:
            file = next(command_dir.glob(f'{command}.*'))
        except StopIteration:
            logger.error(
                f'Failed to start {command}: Unit {command} not found.')
            sys.exit(1)

        try:
            if file.name.endswith('.json'):
                import json
                obj = json.loads(file.read_text())
            else:
                from importlib import import_module
                module_name = f'{command_dir.name}.{command}'
                module_obj = import_module(module_name)
                obj = module_obj.get_obj(*params)
        except Exception as e:
            logger.error(f'{command} Object loading failed', e)
            sys.exit(1)

        try:
            _config = Config.parse_obj(obj)
        except ValidationError as e:
            logger.error(e.errors())
            sys.exit(1)

        # cls.daemonize(command)
        cls.collector = init_collector(_config.collector)
        if _config.parser is not None:
            cls.parser = init_parser(_config.parser)
        if _config.rewriters is not None:
            cls.rewriters = init_rewriters(_config.rewriters)
        cls.handlers = init_handlers(_config.handlers)

        cls.run(command)

    @classmethod
    def run(cls, command: str):
        try:
            data = cls.collector()

            def _run(d: D) -> None:
                if cls.parser is not None:
                    d = cls.parser(d)
                if cls.rewriters is not None:
                    for rewriter in cls.rewriters:
                        d = rewriter(d)
                for handler in cls.handlers:
                    handler(d)

            if isinstance(data, list):
                for item in data:
                    _run(item)
            else:
                _run(data)
        except Exception as e:
            logger.error(f'{command} execution failed', e)

    @classmethod
    def stop(cls, command: str) -> None:
        pidfile = f'/tmp/{command}'
        if not os.path.exists(pidfile):
            logger.error(f'Failed to stop {command}: Unit {command} not loaded.')
            sys.exit(1)

        with open(pidfile, 'r') as f:
            pid = f.read()
        try:
            pid = int(pid)
        except ValueError:
            logger.error(f'Failed to stop {command}: Unit {command} not loaded.')
            sys.exit(1)
        os.kill(pid, 0)
        os.remove(pidfile)

    @classmethod
    def restart(cls, command: str) -> None:
        try:
            cls.stop(command)
        except SystemError as e:
            pass
        cls.start(command)

    @classmethod
    def get_action(cls, option: str) -> Callable[[str], None]:
        return {
            'start': cls.start,
            'stop': cls.stop,
            'restart': cls.restart
        }[option]
