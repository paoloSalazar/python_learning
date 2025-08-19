# IMPLEMENTING PACKAGES
## Creating Packages
### PEP420 and __init__.py
* __init__.py optional in python 3.3 +
* Still Required in earlier python versions
* Powerful initialization tool
* Explicit is better than implicit

### Demo
Create a new directory *demo_reader* and add a __init__.py file in it
then execute python interpreter from directory above
```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo_reader
>>> type(demo_reader)
<class 'module'>
>>> demo_reader.__file__
'/workspaces/python_learning/Python3_OrganizingLargerPrograms/3_implementingPackages/program/demo_reader/__init__.py'

```
A package is a directory containing `__init__.py` file

Modify the `__init__.py` file content
```python
print("Demo Reader is being imported")
```
and then restart python REPL and import again
```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo_reader
Demo Reader is being imported
```

### Demo: Project MultiReader
* Read uncompressed text files
* Read gzip-compressed files
* Read bz2-compressed files

Create a new `multireader.py` file inside demo_reader directory
```python
class MultiReader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, 'rt')

    def close(self):
        self.f.close()
    
    def reader(self):
        return self.f.read()
    
```
then open REPL and import the modules
```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo_reader.multireader
>>> r = demo_reader.multireader.MultiReader("demo_reader/__init__.py")
>>> r.reader()
'# demo_reader/__init__.py'
```

## Creating a Subpackage
let's continue in the above demo

Create a new directory _compressed_ and add a `__init__.py` file

```bash
demo_reader/
├── __init__.py
├── compressed
│   ├── __init__.py
└── multireader.py
```

then import the module in the REPL
```bash
 $ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import demo_reader.compressed
>>> demo_reader.compressed.__file__
'/workspaces/python_learning/Python3_OrganizingLargerPrograms/3_implementingPackages/program/demo_reader/compressed/__init__.py'
```
Add a new file `gzipped.py`
```python
import gzip
import sys

opener = gzip.open # Alias for gzip.open (Decompressed during read)

if __name__ == '__main__': # Main Block
    f = gzip.open( # use gzip to create compressed file
        sys.argv[1], # path to new compressed file
        'wt') 
    f.write(' '.join( # join to space-separated string
        sys.argv[2:]) # The data to compress
    f.close()

```
At this point you should have the next tree directory
```bash
 $ tree demo_reader/
demo_reader/
├── __init__.py
│   └── multireader.cpython-312.pyc
├── compressed
│   ├── __init__.py
│   ├── bzipped.py
│   └── gzipped.py
└── multireader.py
```

Modify the multireader class 
```python
import os

from demo_reader.compressed import gzipped, bzipped

extension_map = {
    '.bz': bzipped.opener,
    '.gz': gzipped.opener
}

class MultiReader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()
    
    def reader(self):
        return self.f.read()
    
```

and test it in cmd
```bash
$ python -m demo_reader.compressed.bzipped tes
t.bz2 data compressed with bz2
$ python -m demo_reader.compressed.gzipped tes
t.gz data compressed with gz
# It is going to create new compressed files
$ ls
demo_reader  test.bz2  test.gz
```
Now let's read the above compressed files

```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from demo_reader.multireader import MultiReader
>>> r = MultiReader('test.gz')
>>> r.reader()
'data compressed with gz2'
```

## Relative Imports
__ABSOLUTE IMPORTS__
```python
# Both of these absolute imports mention
# both ``demo_reader`` and ``compressed``
import demo_reader.compressed.bzipped
from demo_reader.compressed import bzipped
```
### Relative Imports Syntax
```python
from ..module_name import name
```
### Important Rules for Relative Imports
* You can only use the `from module import name` form of import
* Relative imports can only be used to import modules within the current top-level package

Let's refactor the code by writting a new util module

```python
# demo_reader/util/writer.py
import sys

def main(opener):
    f = opener(sys.argv[1], 'wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()

```
Then modify the gzipped and bzipped files
```python
import gzip

from demo_reader.util import writer

opener = gzip.open

if __name__ == '__main__':
    writer.main(opener)
```

| Relative               | Absolute                                |
|------------------------|-----------------------------------------|
| from . import name     | from demo_reader.compressed import name |
| from .. import name    | from demo_reader import name            |
| from ..util import name| from demo_reader.util import name       |

so, we can use relative imports as next
```python
import bz2
# from demo_reader.util import writer
from .. import util

opener = bz2.open

if __name__ == '__main__':
    util.writer.main(opener)
```

Summary of Relative Imports
* Can reduce typing in deeply nested package structures
* Promote a certain form of modifiability 
* In general, prefer absolute imports

## Using `__all__` 
* Module Level Attribute
* controls `from module import *` behavior
* If not specified, import all public names
* Must be a list of strings
    * Each Entry is a name to import

Add the next code to `demo_reader/compressed/__init__.py`
```python
from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener 

```
Then go to python REPL
```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pprint import pprint
# pprint(locals()) print names in current scope
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f7000d2f060>}
 # Now import all compressed module using *
>>> from demo_reader.compressed import *
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'bz2_opener': <function open at 0x7f7000d73ce0>,
 'bzipped': <module 'demo_reader.compressed.bzipped' from '/workspaces/python_learning/Python3_OrganizingLargerPrograms/3_implementingPackages/program/demo_reader/compressed/bzipped.py'>,
 'gzip_opener': <function open at 0x7f7000d73a60>,
 'gzipped': <module 'demo_reader.compressed.gzipped' from '/workspaces/python_learning/Python3_OrganizingLargerPrograms/3_implementingPackages/program/demo_reader/compressed/gzipped.py'>,
 'pprint': <function pprint at 0x7f7000d2f060>}
```

Let's modify `demo_reader/compressed/__init__.py` file to add the `__all__` special variable
```python
from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener 

__all__ = ['bz2_opener', 'gzip_opener']
```

then let's check with python REPL
```bash
) $ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pprint import pprint
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x742ef13d3060>}
>>> from demo_reader.compressed import *
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'bz2_opener': <function open at 0x742ef1417c40>,
 'gzip_opener': <function open at 0x742ef1421580>,
 'pprint': <function pprint at 0x742ef13d3060>}
>>> 
```

Note only bz2_opener and gzip_opener have been imported

