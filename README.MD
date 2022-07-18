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

## Available commands

- **restore** - reads the `topaz.json` file and downloads them into `_topaz` folder. 
