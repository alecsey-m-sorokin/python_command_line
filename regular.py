import sys
import argparse

def gameParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strategy', default='basic')
    parser.add_argument('--sessions', type=int, default=1)
    parser.add_argument('--rounds', type=int, default=5)

    return parser

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print('\nusing', sys.argv[0])
    print_hi('MM5')

    gameParams = gameParser()
    namespace = gameParams.parse_args(sys.argv[1:])
    print(namespace)
    print(f'strategy = {namespace.strategy}')
    print(f'sessions = {namespace.sessions}')
    print(f'rounds = {namespace.rounds}')
