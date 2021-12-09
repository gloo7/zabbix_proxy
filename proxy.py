import argparse

from task import Task


parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('option', choices=['start', 'stop', 'restart'])
parser.add_argument('command', type=str)


if __name__ == '__main__':
    args = parser.parse_args()
    Task.get_action(args.option)(args.command)
