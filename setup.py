#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='structures_stats',
    version='0.1',
    description='A collection of collection visitor (pattern) helpers.',
    long_description='A set of classes allowing to traverse/walk abritrary python structures and collect different stats on them.',
    author='Pavel Trukhanov',
    author_email='curlup@yandex.ru',
    url='http://github.com/curlup/structures_stats',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
