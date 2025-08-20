import importlib
import os
import pkgutil

import demo_reader.compressed

def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(
        ns_pkg.__path__,
        ns_pkg.__name__ + '.'
    )

compression_plugins = {
    importlib.import_module(module_name)
    for _, module_name, _ 
    in iter_namespace(demo_reader.compressed)
}

# This maps file extensions to corresponding open methods
extension_map = {
    module.extension: module.opener
    for module in compression_plugins
}