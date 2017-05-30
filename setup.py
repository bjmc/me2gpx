#!/usr/bin/env python

from setuptools import setup

with open('test_requirements.txt') as f:
    test_requirements = f.readlines()

setup(name='me2gpx',
      version='0.1',
      description='Python Distribution Utilities',
      author='Brendan McCollam',
      author_email='brendan@mccoll.am',
      url='https://github.com/bjmc/me2gpx',
      packages=['me2gpx'],
      test_suite='test.test_suite',
      tests_require=test_requirements,
     )
