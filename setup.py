
from setuptools import setup, find_packages

from codecs import open
from os import path

setup(
    name='vim_power',
    version='1.0.0.dev1',
    description='Add a `vim` indicator on your shell\'s Powerline if you stepped in from vim via `:sh`',
    long_description='Add a `vim` indicator on your shell\'s Powerline if you stepped in from vim via `:sh`',
    url='https://github.com/bezhermoso/vim_power',
    author='Bez Hermoso',
    author_email='bezalelhermoso@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],
    keywords='powerline vim shell',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['powerline-status']
)
