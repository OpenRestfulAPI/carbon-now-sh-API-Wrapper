#!/usr/bin/env python
import setuptools

from carbonnow import __version__

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='carbonnow',
    version=__version__,
    description='carbon.now.sh API Wrapper powered by Carbonara',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    author='Pokurt',
    author_email='poki@pokurt.me',
    url='https://github.com/OpenRestfulAPI/carbon-now-sh-API-Wrapper',
    packages=setuptools.find_packages(exclude='example.py'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['aiohttp==3.7.3', 'asyncio==3.4.3'],
    python_requires='>=3.6',
)
