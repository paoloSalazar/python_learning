# NAMESPACE AND EXECUTABLE PACKAGES
## Overview
* Introduce namespace packages
* Demonstrate executable directories
* Execute code from zipped directories
* Make executable packages

__PEP 420: Implicit Namespace Packages__
"Namespace packages are a mechanism for splitting a single python package across
Multimple directories on disk"

Namespace packages may not have `__init__.py`

### Namespace Package Discovery Algorithm
- Scan each directory in `sys.path`
- Import standard package if found
- Import standard module if found
- Otherwise, all matching directories contribute to a namespace package

To understand the namespace packages organize your code in the next form
```bash
 $ tree namespace_pkg/
namespace_pkg/
├── path1
│   └── demo_reader
│       ├── multireader.py
│       └── util
│           ├── __init__.py
│           └── writer.py
└── path2
    └── demo_reader
        └── compressed
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-312.pyc
            │   ├── bzipped.cpython-312.pyc
            │   └── gzipped.cpython-312.pyc
            ├── bzipped.py
            └── gzipped.py

8 directories, 9 files
(venv) @paoloSalazar ➜ /workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages (develop) $ 
(venv) @paoloSalazar ➜ /workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages (develop) $ tree namespace_pkg/
namespace_pkg/
├── path1
│   └── demo_reader
│       ├── multireader.py
│       └── util
│           ├── __init__.py
│           └── writer.py
└── path2
    └── demo_reader
        └── compressed
            ├── __init__.py
            ├── bzipped.py
            └── gzipped.py
```
Note the demo_reader is distributed across path1 and path2 folders, and there are no `__init__.py`
Now let's check in python REPL
```bash
$ python
Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
# Add path1 and path2 to sys.path
>>> sys.path.extend(['./path1','./path2'])
>>> import demo_reader
>>> demo_reader.__path__
_NamespacePath(['/workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages/namespace_pkg/path1/demo_reader', '/workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages/namespace_pkg/path2/demo_reader'])
>>> import demo_reader.util
>>> import demo_reader.compressed
>>> demo_reader.util.__path__
['/workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages/namespace_pkg/path1/demo_reader/util']
>>> demo_reader.compressed.__path__
['/workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages/namespace_pkg/path2/demo_reader/compressed']
>>> 
```

## Executable Directories
let's organize the code by adding `demo_reader` folder to `multi-reader-program`
```bash
$ tree multi-reader-program/
multi-reader-program/
└── demo_reader
    ├── __init__.py
    ├── compressed
    │   ├── __init__.py
    │   ├── bzipped.py
    │   └── gzipped.py
    ├── multireader.py
    └── util
        ├── __init__.py
        └── writer.py

4 directories, 7 files
```
Then try to execute the folder `multi-reader-program`
```bash
$ python multi-reader-program/
/workspaces/venv/bin/python: can't find '__main__' module in '/workspaces/python_learning/Python3_OrganizingLargerPrograms/4_NameSpaceAndExecutablePackages/multi-reader-program/'
```

You can execute a directory if it contains `__main__.py`
`__main__.py` will be executed
```bash
 $ tree multi-reader-program/
multi-reader-program/
├── __main__.py
└── demo_reader
    ├── __init__.py
    ├── compressed
    │   ├── __init__.py
    │   ├── bzipped.py
    │   └── gzipped.py
    ├── multireader.py
    └── util
        ├── __init__.py
        └── writer.py

```
Now you can run the folder

```bash
$ python multi-reader-program/
executing multi-reader-program/__main__.py
```

### Using `__main__.py` and `sys.path`
1. Added to sys.path
```bash
program/
    __main__.py
```
2. Executed by "Python Program"

Let's modify the `__main__.py` file

```python
import sys

from demo_reader.multireader import MultiReader

filename = sys.argv[1]
r = MultiReader(filename)
print(r.reader())
r.close()
```

```bash
$ python multi-reader-program test.gz 
data compressed with gz2
```

## Executable Zip Files
The zip file contains the same contents as the directory, not the directory itself

let's create a zip python executable
```bash
$ cd multi-reader-program/
$ python -m zipfile -c ../multi-reader-program.zip * 
$ cd
$ ls multi-reader-program.zip 
multi-reader-program.zip
$ python multi-reader-program.zip test.gz 
data compressed with gz2
```
Ideal to distribute packages in some cases..
the advantage is you don't need to install any package

