#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="pypi-show-urls",
    version="1.1",

    description="Shows all the installation candidates for a list of packages",
    url="https://github.com/dstufft/pypi-show-urls",

    author="Donald Stufft",
    author_email="donald@stufft.io",

    install_requires=[
        "requests",
        "lxml",
    ],

    packages=find_packages(exclude=["tests"]),

    entry_points={
        "console_scripts": [
            "pypi-show-urls = pypi_show_urls.__main__:main",
        ],
    },
)
