#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='asynch',
    version='0.1.0',
    description='Async client for clickhouse',
    author='Abhinav',
    author_email='abhinav.23.april@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='LICENSE.txt',
    install_requires=[
        "backcall==0.2.0",
        "backports.zoneinfo==0.2.1",
        "ciso8601==2.2.0",
        "clickhouse-cityhash==1.0.2.3",
        "clickhouse-driver==0.2.1",
        "decorator==5.0.9",
        "jedi==0.18.0",
        "leb128==1.0.4",
        "lz4==3.1.3",
        "matplotlib-inline==0.1.2",
        "parso==0.8.2",
        "pexpect==4.8.0",
        "pickleshare==0.7.5",
        "prompt-toolkit==3.0.20",
        "ptyprocess==0.7.0",
        "Pygments==2.10.0",
        "pytz==2021.1",
        "toml==0.10.2",
        "traitlets==5.0.5",
        "tzlocal==2.1",
        "wcwidth==0.2.5",
        "zstd==1.5.0.2"
    ],
)