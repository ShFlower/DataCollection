from setuptools import setup, find_packages

setup(name='HomeTrends',
       version =2.0,
       packages=find_packages(),
       install_requires=[
        'selenium',
        'webdriver-manager',
        'ipykernel',
        'pandas',
        'nltk',
        'Fraction'
       ])