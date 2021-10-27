from setuptools import find_packages, setup
setup(
    name='sqlite3_wrapper',
    packages=find_packages(include=['sqlite3_wrapper']),
    version='0.1.0',
    description='Wrapper for Sqlite3 in Python',
    author='Narek Boghozian',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
