import argparse

from task import Task


parser = argparse.ArgumentParser(prog='ZABBIX_SCRIPTS')
parser.add_argument('command', type=str)
parser.add_argument('params', action='extend', nargs='+', help='The script requires parameters')

if __name__ == '__main__':
    args = parser.parse_args()
    Task.start(args.command, args.params)

