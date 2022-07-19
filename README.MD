# 💎 tOPAz - package manager for the [Open Policy agent](https://www.openpolicyagent.org)

The goal of topaz is to manage dependencies in a convenient way,
that can be utilized by the rego language

## Local installation

I would suggest to make a virtualenv to not pollute the global packages

```bash
python3 -m venv topaz-env
source topaz-env/bin/activate
pip install -r requirements.txt
```

## File specification

```json
{
    "topaz_version": "0.0.1",
    "git": [
        "https://github.com/path/to/rego"
    ]
}
```

Place into "git" section links ro repositories, which should be downloaded
and placed into the current folder

## Available commands

- **restore** - reads the `topaz.json` file and downloads them into `_topaz` folder. 
After restore ahve been completed, it will also create a topaz.lock file, which have
the necessary versions of repositories

- **init** - creates the `topaz.json` with the default values
