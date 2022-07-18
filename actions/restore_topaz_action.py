import argparse
import json

from git import Repo

class RestoreAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string) -> None:
        print("🪖 Restoring the policies...")
        try:
            topaz_json = open('topaz.json')
            json_contents = json.load(topaz_json)
            for git_repo in json_contents['git']:
                print("Cloning " + git_repo + "...")
                Repo.clone_from(git_repo, "./_topaz")
        except:
            print("No topaz.json was found. Try to use init command first")

