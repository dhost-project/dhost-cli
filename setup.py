#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests']

setup_requirements = [
    'pytest-runner',
    'colorama',
]

test_requirements = [
    'pytest>=3',
]

setup(
    author="Dhost CLI",
    author_email='contact@dhost.dev',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="CLI to access the DHost services.",
    entry_points={
        'console_scripts': [
            'dhost-cli=dhost_cli.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dhost-cli',
    name='dhost-cli',
    packages=find_packages(include=['dhost_cli', 'dhost_cli.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dhost-project/dhost-cli',
    project_urls={
        "Bug Tracker": "https://github.com/dhost-project/dhost-cli/issues",
    },
    version='0.1.3',
    zip_safe=False,
)
