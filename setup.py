
from distutils.core import setup

setup(
    name='Wyther',
    version='0.1.0',
    author='Nirav Bhatia',
    author_email='bnirav23@gmail.com',
    packages=['wyther'],
    url='https://github.com/niravb1992/Wyther',
    license='LICENSE.txt',
    description='A simple Python wrapper to the Yahoo Weather API',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.0.1",
    ],
)