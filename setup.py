#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pydub', ]

test_requirements = []

setup(
    author="Kaikai Qi",
    author_email='iamkkqi@163.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        # "Programming Language :: Python :: 2",
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="语音操作快捷命令",
    entry_points={
        'console_scripts': [
            'sp=mcc.split:main',
            'sy=mcc.synthesize:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mcc',
    name='mcc',
    packages=find_packages(include=['mcc']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/iamkkqi/mcc',
    version='0.1.3',
    zip_safe=False,
)
