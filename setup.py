from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python packages I created',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Keletso/pythonpackage',
    author='Keletso Dithebe',
    author_email='keletsodthb@gmail.com')
