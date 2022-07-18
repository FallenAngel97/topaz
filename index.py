#!/usr/bin/env python3

import argparse
import json

from git import Repo

def restore():
    print("🪖 Restoring the policies...")
    topaz_json = open('topaz.json')
    json_contents = json.load(topaz_json)
    for git_repo in json_contents['git']:
        print("Cloning " + git_repo + "...")
        Repo.clone_from(git_repo, "./_topaz")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('restore', nargs='?')
    args = parser.parse_args()
    if args.restore != None:
        restore()

if __name__ == "__main__":
   main()
