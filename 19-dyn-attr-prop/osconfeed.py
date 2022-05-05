"""
    Пример 19.2. osconfeed.py: загрузка файла osconfeed.json (doctest-скрипты
    приведены в примере 19.3)
"""

from urllib.request import urlopen
import warnings
import os
import json

URL = 'https://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # <1>
        with urlopen(URL) as remote, open(JSON, 'wb') as local:  # <2>
            local.write(remote.read())
    with open(JSON) as fp:
        return json.load(fp)  # <3>
