import sys
import argparse

def gameParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sessions', type=int, default=1)
    parser.add_argument('--rounds', type=int, default=25)
    return parser

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print('\nusing', sys.argv[0])
    print_hi('MM5')

    gameParams = gameParser()
    namespace = gameParams.parse_args(sys.argv[1:])
    sessions = namespace.sessions
    rounds = namespace.rounds
    print(f'sessions = {sessions}')
    print(f'rounds = {rounds}')
    print(namespace)
