#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Game",
    version="1.0.0",
    description="My first game",
    python_requires=">=3.7",
    install_requires=["pygame==1.9.6"],
    packages=["game"]
)