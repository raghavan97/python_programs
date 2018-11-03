import os
import sys

from setuptools import setup
from setuptools import setup, Extension
from wheel.bdist_wheel import bdist_wheel
from setuptools import find_packages

class BinaryDistWheel(bdist_wheel):
    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = False

# This creates a list which is empty but returns a length of 1.
# Should make the wheel a binary distribution and platlib compliant.
class EmptyListWithLength(list):
    def __len__(self):
        return 1


def setup_packages():

    long_description=(
        "A Long description "
        " usually spans across multiple lines"
        "This is line 1"
    )

    meta_data = dict(
        name="minty",
        version='0.0.4',
        description='minty choclate',
        long_description=long_description,
        license='Apache License 2.0',
        author='Raghavan',
        author_email='raghavan.compilers2009@gmail.com',
        maintainer='Raghavan',
        maintainer_email='raghavan@mars.com',
        url='https://github.com/whatever',
        zip_safe = False,
        cmdclass={'bdist_wheel': BinaryDistWheel},

        package_dir = {
            'minty': 'minty'
        },
        package_data = {
            'minty': [
                'mstplib/libmyextn.so'
            ]
        },
        packages=['minty', 'minty.mstplib', 'minty.cool'],
        ext_modules=EmptyListWithLength(),


        install_requires=[
            "bacpypes"
        ]
    )
    setup(**meta_data)
        


if __name__ == '__main__':
    setup_packages()
