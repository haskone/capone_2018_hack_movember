# capone_2018_hack_movember
A solution for Movember problems from Capital One Hackathon 2018

- download last python https://www.python.org/downloads/
- create venv: ```python -m venv venv```
- activate venv (depends on OS): https://docs.python.org/3/library/venv.html
- install dependencies: ```python -m pip install -r requirements.txt```
- run with ```python index.py```
- ```config.json``` contains host/port for cloud running, remove these parameters from config in case of local run, so leave just:

```json
{
    "secret_key": "any_very_secret_key"
}
```
