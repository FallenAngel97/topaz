#!/usr/bin/env python3

import argparse

from actions.init_topaz_action import InitTopazAction
from actions.restore_topaz_action import RestoreAction

topaz_description = '''
💎 Topaz is the CLI utility for the Open Policy Agent. 

Thegeneral idea is to introduce the package manager, which can perform basic tasks, such as managing the dependencies
in a more convenient way
'''

opa_link = '''
More about OPA: https://openpolicyagent.org
'''

def main():
    parser = argparse.ArgumentParser(
        description = topaz_description,
        epilog = opa_link
    )
    parser.add_argument('restore', nargs='?', action=RestoreAction)
    parser.add_argument('init', nargs='?', action=InitTopazAction)
    args = vars(parser.parse_args())
    if not any(args.values()):
        parser.error('No arguments provided.')

if __name__ == "__main__":
   main()
