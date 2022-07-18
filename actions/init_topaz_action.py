import argparse

topaz_default_contents = '''
{
    "topaz_version": "0.0.1",
    "git": []
}
'''

class InitTopazAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string) -> None:
        print("Initialized a template for the OPA policies. Open topaz.json and define some of your dependencies")
        topaz_json = open('topaz.json', 'a')
        topaz_json.write(topaz_default_contents)
        topaz_json.close()

