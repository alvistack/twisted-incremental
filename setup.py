# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='incremental',
    version='24.7.2',
    description='A CalVer version manager that supports the future.',
    maintainer_email='Amber Brown <hawkowl@twistedmatrix.com>, Tom Most <twm@freecog.net>',
    classifiers=[
        'Framework :: Hatch',
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'setuptools>=61.0',
        'tomli; python_version < "3.11"',
    ],
    extras_require={
        'scripts': [
            'click>=6.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'incremental = incremental.update:_main',
        ],
        'distutils.setup_keywords': [
            'use_incremental = incremental:_get_distutils_version',
        ],
        'hatch': [
            'incremental = incremental._hatch',
        ],
        'setuptools.finalize_distribution_options': [
            'incremental = incremental:_get_setuptools_version',
        ],
    },
    packages=[
        'incremental',
        'incremental.tests',
    ],
    package_dir={'': 'src'},
)
