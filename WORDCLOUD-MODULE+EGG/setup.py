from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1.0',
    description='WordCloud Generator',
    long_description='This function generates a WordCloud based on Reviews',
    author='Daksh Jain',
    author_email='daksh.jain00@gmail.com',
    packages=find_packages(exclude=['*tests*']),
)