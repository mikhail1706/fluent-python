"""
    Dict
    5 ways to create dict
    setdefault - Example 3.2, Example 3.4
    defaultdict -

    Метод __missing__
    Example 3.7 StrKey
    Example 3.8 StrKeyDict
    Example 3.8 MappingProxyType
"""

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# Example 3.1 dictcomp
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}

other_dict = {code: country for country, code in country_code.items()
              if code < 66}

# Example 3.2
import sys
import re
import collections

WORD_RE = re.compile('\w+')
index = {}
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # Некрасивый вариант
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

            # Красивый вариант setdefault
            index.setdefault(word, []).append(location)

            # Вариант c defaultdict
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# Example 3.7
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# Example 3.8
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setattr__(self, key, value):
        self.data[str(key)] = value


# Example 3.9
from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)
print(d_proxy[1])
d[2] = 'B'

print(d_proxy)
