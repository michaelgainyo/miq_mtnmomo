from os import path
from setuptools import setup, find_packages


import miqmtn


here = path.abspath(path.dirname(__file__))


setup(
    name='miqmtn',
    version='1.0.0',
    description='MTN Mobile Money API wrapper',
    long_description='',
    # url='',
    author='marqetintl',
    author_email='michaelgainyo@gmail.com',
    keywords='mtn momo',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires=">=3.5",
    # test_suite='nose.collector',
    # tests_require=['nose'],
    # include_package_data=True
    zip_safe=False
)
