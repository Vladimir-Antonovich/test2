"""Module test2."""
from setuptools import setup
from setuptools import find_packages


setup(
    name='test2',
    version='0.1',
    author='Vladimir Antonovich',
    author_email='antonovich.vladimir@gmail.com',
    license='',
    zip_safe=False,
    packages=find_packages(exclude=['tests*']),
    install_requires=[
    ],
    test_requires=[
        'mock',
        'requests-mock'
    ]
)
