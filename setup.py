from setuptools import setup, find_packages


setup(
    name = 'Brain_Computer_Interface',
    version = '0.1.0',
    author = 'Daniel Sterenson',
    description = 'A project of a Brain Computer Interface for "Advance System Design" course in TAU.',
    packages = find_packages(),
    install_requires = ['click', 'flask', 'pillow'],
    tests_require = ['pytest', 'pytest-cov'],
)
