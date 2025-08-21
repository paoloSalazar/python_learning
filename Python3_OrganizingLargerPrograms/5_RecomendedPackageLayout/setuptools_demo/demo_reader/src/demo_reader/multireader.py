import os
import pkg_resources

compression_plugins = {
    entry_point.load()
    for entry_point
    in pkg_resources.iter_entry_points('demo_reader.compression_plugins')
}

extension_map = {
    module.extension: module.opener
    for module in compression_plugins
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