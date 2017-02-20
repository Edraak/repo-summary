#!/usr/bin/env python

from setuptools import setup

setup(
    name='repo-summary',
    version='0.1',
    description='Edraak repo summarizer.',
    author='Edraak',
    author_email='dev@qrf.org',
    url='https://github.com/Edraak/repo-summary',
    packages=[
        'repo_summary',
    ],
    install_requires=[
        'pyyaml==3.12',
    ],
    entry_points={
        'console_scripts': [
            'mods_list = repo_summary.mods_list:main',
        ],
    },
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
