import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Remembrall",
    version = "0.0.1",
    author = "Saurabh AV",
    author_email = "saurabhav.torres@gmail.com",
    description = ("A terminal to-do list that reminds!"),
    license = "BSD",
    keywords = "remembrall to-do list",    
    packages=find_packages(),
    install_requires= [
        "docopt",
	   "python-crontab",
    ],
    py_modules=[
        'main', 
        'initializer', 
        'constants', 
        'list'
    ],
    long_description=read('README.md'),    
    entry_points={
        'console_scripts': ['remembrall=main:console_entry'],
    },
    zip_safe=True,
)
