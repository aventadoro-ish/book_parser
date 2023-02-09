import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="book_parser",
    version="0.0.1",
    author="aventadoro-ish",
    author_email="aventadoroqwerty@#gmail.com",
    description="Prefix-tree-based text story analyser",
    license="BSD",
    keywords="prefix tree parser text",
    # url="http://packages.python.org/an_example_pypi_project",
    packages=['book_parser', 'tests'],  # TODO: change to test package used
    long_description=read('README'),
    classifiers=[],
)

