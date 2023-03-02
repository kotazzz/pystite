from .build import build
import argparse

parser = argparse.ArgumentParser(
    prog='Pystite',
    description='Static site generator',
    epilog=':)')
parser.add_argument('command')           # positional argument
# parser.add_argument('-c', '--count')      # option that takes a value
# parser.add_argument('-v', '--verbose',
#                     action='store_true')  # on/off flag
args = parser.parse_args()


def main(command):
    if command == 'build':
        build()
    else:
        parser.error('Unknown command')

if __name__ == "__main__":
    main(**vars(args))
