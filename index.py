#!/usr/bin/env python3

import argparse
import sys
import json

from git import Repo

from text_style import text_style

topaz_description = '''
💎 Topaz is the CLI utility for the Open Policy Agent. 

The general idea is to introduce the package manager, which can perform basic tasks, such as managing the dependencies
in a more convenient way
'''

opa_link = '''
More about OPA: https://openpolicyagent.org
'''

topaz_default_contents = '''
{
    "topaz_version": "0.0.1",
    "git": []
}
'''

class SelectModeAction(argparse.Action):
    def restore(self):
        print("🪖 Restoring the policies...")
        try:
            topaz_json = open('topaz.json')
            json_contents = json.load(topaz_json)
            for git_repo in json_contents['git']:
                print("Cloning " + git_repo + "...")
                cloned_repo = Repo.clone_from(git_repo, "./_topaz")
                print(cloned_repo.heads[0].commit.hexsha)
        except:
            print(f"⚠️  No topaz.json was found. Try to use {text_style.BOLD}init{text_style.END} command first")

    
    def init(self):
        print(f"Initialized a template for the OPA policies.✨\nOpen {text_style.BOLD}topaz.json{text_style.END} and define some of your dependencies")
        topaz_json = open('topaz.json', 'a')
        topaz_json.write(topaz_default_contents)
        topaz_json.close()

    def __call__(self, parser, namespace, values, option_string) -> None:
        if values == "init":
            self.init()
        if values == "restore":
            self.restore()

def main():
    parser = argparse.ArgumentParser(
        description = topaz_description,
        epilog = opa_link
    )
    parser.add_argument(
        'mode',
        choices=['restore', 'init'],
        action=SelectModeAction
    )
    parser.parse_args()

if __name__ == "__main__":
   main()
