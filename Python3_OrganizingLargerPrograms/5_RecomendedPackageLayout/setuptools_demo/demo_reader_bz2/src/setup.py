import setuptools

setuptools.setup(
    name='demo_reader_bz2_plugin',
    version='0.0.0',
    description='A demo plugin for reading bz2 compressed files',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_reader.compression_plugins': [
            'bz2 = demo_reader_bz2.bzipped'
        ]
    }
)