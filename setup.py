#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except:
    from distutils.core import setup

try:
    with open('README.rst') as readme_file:
        readme = readme_file.read()
except IOError:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme_file:
        readme = readme_file.read()

requirements = ['progressbar-latest']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Johannes Buchner",
    author_email='johannes.buchner.acad@gmx.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="Shows rsync file progress and total progress as a progress bar.",
    install_requires=requirements,
    license="MIT",
    long_description=readme,
    keywords='rsync-progress',
    name='rsync-progress',
    scripts=['rsync-progress.py'],
    setup_requires=setup_requirements,
    url='https://github.com/JohannesBuchner/rsync-progress.py',
    version='1.0.0',
)
