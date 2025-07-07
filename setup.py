from setuptools import setup

setup(
    name='remotecommand',
    version=1.0,
    packages=['remotecommand'],
    install_requires=['pytest'],
    entry_points={'console_scripts': ['remotecommand = remotecommand.cli.main:main']}
)