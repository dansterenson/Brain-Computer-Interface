from setuptools import setup, find_packages


setup(
    name = 'foobar',
    version = '0.1.0',
    author = 'Dan Sterenson',
    description = 'A project of a Brain Computer Interface for "Advance System Design" course in TAU.',
    packages = find_packages(),
    install_requires = ['click', 'flask'],
    tests_require = ['pytest', 'pytest-cov'],
)
