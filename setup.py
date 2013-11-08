
from distutils.core import setup

setup(
    name='Wyther',
    version='0.1.0',
    author='Nirav Bhatia',
    author_email='bnirav23@gmail.com',
    packages=['wyther', 'wyther.test'],
    url='http://pypi.python.org/pypi/Wyther/',
    license='LICENSE.txt',
    description='A simple Python wrapper to the Yahoo Weather API',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.0.1",
    ],
)