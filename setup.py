from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='marketing',
    version=version,
    description='Marketing for Medical',
    author='wayzon',
    author_email='wayzon@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
