# RECOMENDED PACKAGE LAYOUT
## Overview
* A project structure for most projects
* Project description files
* Extending packages with plugins
* Different methods for implementing plugins

Project structure
```bash
project_name/.                 # Project root - not the package
    README.rst.                # Overview documentation
    docs/.                     # Project documentation 
    src/                       # Package/production code
        package_name/.  
            __init__.py
            more_source.py
            subpackage1/
                __init__.py
    tests/                     # All tests for the project
        test_code.py
    setup.py
```
 ### Documentation
 * Can come in many forms(e.g. Sphinx)
 * It should be easy to find
 * RutEADME.rst should be in project root
    * Common convention
    * Often refers to docs directory

### Src Directory
The `src` directory ensures that you develop against _installed versions_ of your packages

### Separation of test and production code
* Test and production code serve different purposes
* Usually don't want tests installed with package
* Avoid tools treating tests as production code
* Be Pragmatic! put tests in production code if necessary

## A concrete example: `demo_reader`
```bash
$ tree demo_reader --dirsfirst
demo_reader
├── src
│   ├── compressed
│   │   ├── __init__.py
│   │   ├── bzipped.py
│   │   └── gzipped.py
│   ├── util
│   │   ├── __init__.py
│   │   └── writer.py
│   ├── __init__.py
│   ├── __main__.py
│   └── multireader.py
├── tests
│   └── test_multireader.py
├── README.rst
└── setup.py

5 directories, 11 files
```

## Implementing Plugins with Namespace Packages
### Extending Packages with Plugins
* Packages define _extensions points_
* Extensions are implemented outside the package
* Extensions are discovered at runtime
* We'll look at two methods
    * Namespace packages and `pkgutil`
    * setuptools _entry points_

- Core package designates subpackages as extension points
- Core package at runtime to discover plugins
- Plugins augment the namespace package's extensible subpackages

```python

```