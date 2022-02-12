def tag(name, *content, cls=None, **attrs):
    """Генерирует один или несколько HTML-тегов"""

    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}

print(tag(**my_tag))

# Example 5.18
import inspect

sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)

for name, value in bound_args.arguments.items():
    print(name, '=', value)

del my_tag['name']
bound_args = sig.bind(**my_tag)


# Example 5.19
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()


# Example 5.22
from functools import reduce
from operator import mul


def fact(n):
    return reduce(mul, range(1, n + 1))


# Example 5.23
from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# Если передать функции itemgetter несколько индексов, то она построит функ-
# цию, которая возвращает кортеж, содержащий выбранные значения:
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# Example 5.24
from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

print(metro_areas[0].coord.lat)
from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

# Example 5.25
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
upcase(s)
hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)


# Example 5.26
from operator import mul
from functools import partial
triple = partial(mul, 3)

print(triple(7))
list(map(triple, range(1, 10)))