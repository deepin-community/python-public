#!/usr/bin/python3

import os
import sys


# Create a module we can import.
lib = os.path.join(os.environ['AUTOPKGTEST_TMP'], 'lib')
os.makedirs(lib)

path = os.path.join(lib, 'module.py')
with open(path, 'w', encoding='utf-8') as fp:
    print("""\
from public import public

@public
class Foo:
    pass

@public
def foo():
    pass

class Bar:
    pass

def bar():
    pass
""", file=fp)


sys.path.insert(0, lib)
import module

if module.__all__ == ['Foo', 'foo']:
    print('__all__ good')
    sys.exit(0)
else:
    print('__all__:', module.__all__)
    sys.exit(1)
