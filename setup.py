#!/usr/bin/env python3
# flake8: noqa
'''
Setup script for the repository.
'''
from setuptools import setup, find_packages, Distribution
from optimized_routing.version import __version__

def read_requirements():
    """
    TODO: currently does not read URLs correctly.
    """
    with open('requirements.txt') as req:
        requirements = req.read().split('\n')
    return requirements

setup(name='optimized-routing',
      version=__version__,
      description='Optimization library for solving qubit-routing problems',
      distclass=Distribution,
      install_requires=[], #read_requirements(),
      packages=find_packages(include=['optimized_routing', 'optimized_routing.*']),
      zip_safe=False,
)