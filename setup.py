import os
from setuptools import setup, find_packages

setup(
    name = "Remembrall",
    version = "0.0.3",
    author = "Saurabh AV",
    author_email = "saurabhav.torres@gmail.com",
    description = ("A terminal to-do list that reminds!"),
    license = "BSD",
    keywords = "remembrall to-do list",    
    packages=find_packages(),
    install_requires= [
        "docopt",
	   "python-crontab",
       "future"
    ],
    py_modules=[
        'main', 
        'initializer', 
        'constants', 
        'list'
    ],   
    entry_points={
        'console_scripts': ['remembrall=main:console_entry'],
    },
    zip_safe=True,
)
