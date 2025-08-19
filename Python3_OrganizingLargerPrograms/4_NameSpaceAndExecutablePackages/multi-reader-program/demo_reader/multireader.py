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
    

    