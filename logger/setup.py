from setuptools import setup,find_packages

setup(
    name='my-pyapp',
    version='0.0.1',
    packages=find_packages(),
    scripts=['myapp',],
    license='Junk',
    install_requires = [
        'colorlog >= 2.6.0'
    ],
    long_description='junky'
)

