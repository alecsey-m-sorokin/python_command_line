import sys
import argparse
from subprocess import call
from subprocess import Popen
import os

fileName_fs = 'fs.py'
fileName_basic = 'basic.py'
fileName_regular = 'regular.py'

def gameParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    mm5 = subparsers.add_parser('mm5')
    mm5.add_argument('--strategy', default='basic')
    mm5.add_argument('--sessions', type=int, default=1)
    mm5.add_argument('--rounds', type=int, default=5)

    mm6 = subparsers.add_parser('mm6')
    mm6.add_argument('--sessions', type=int, default=1)
    mm6.add_argument('--rounds', type=int, default=5)

    return parser


gameParams = gameParser()
namespace = gameParams.parse_args(sys.argv[1:])

if namespace.command == "mm5":
    print('using', sys.argv[0])
    print(namespace)
    print(f'strategy = {namespace.strategy}')
    print(f'sessions = {namespace.sessions}')
    print(f'rounds = {namespace.rounds}')

    if namespace.strategy == 'fs':
        os.system(f'python {fileName_fs} --strategy {namespace.strategy} --sessions {namespace.sessions} --rounds {namespace.rounds}')

    elif namespace.strategy == 'basic':
        os.system(f'python {fileName_basic} --strategy {namespace.strategy} --sessions {namespace.sessions} --rounds {namespace.rounds}')

    elif namespace.strategy == 'regular':
        os.system(f'python {fileName_regular} --strategy {namespace.strategy} --sessions {namespace.sessions} --rounds {namespace.rounds}')

elif namespace.command == "mm6":
    print(namespace)
    print(f'sessions = {namespace.sessions}')
    print(f'rounds = {namespace.rounds}')
    call(["python", "main2.py"])

else:
    print("Что-то пошло не так...")

    # call(["python", f"main.py --sessions {namespace.sessions} --rounds {namespace.rounds}"])
    # Popen(f'python main.py --sessions {namespace.sessions} --rounds {namespace.rounds}')
