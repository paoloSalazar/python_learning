from setuptools import setup, find_packages

setup(
    name="demo_reader",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    description="A demo package for reading compressed files",
    python_requires=">=3.7",
)