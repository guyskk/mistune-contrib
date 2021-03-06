#!/usr/bin/env python
# coding: utf-8


try:
    # python setup.py test
    import multiprocessing
except ImportError:
    pass

import mistune_contrib
from setuptools import setup


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()

setup(
    name='mistune-contrib',
    version=mistune_contrib.__version__,
    url='https://github.com/lepture/mistune-contrib',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='Contribution for Mistune',
    long_description=fread('README.rst'),
    license='BSD',
    packages=['mistune_contrib'],
    install_requires=[
        "pyyaml>=3.11"
    ],
    zip_safe=False,
    platforms='any',
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Markup',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
