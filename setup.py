from os import path
from setuptools import setup, find_packages


import miqmomo


here = path.abspath(path.dirname(__file__))


setup(
    name='miqmomo',
    version=miqmomo.__version__,
    description='MTN Mobile Money API wrapper',
    long_description='',
    # url='',
    author=miqmomo.__author__,
    author_email=miqmomo.__email__,
    keywords='mtn momo',
    # license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires=">=3.5",
    # test_suite='nose.collector',
    # tests_require=['nose'],
    # include_package_data=True
    zip_safe=False
)
