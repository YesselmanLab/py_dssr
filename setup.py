import os
from setuptools import setup, find_packages

setup(
    name='pydssr',
    version='0.0.03',
    author='Joe Yesselman',
    author_email='jyesselm@unl.edu',
    packages=["pydssr"],
    py_modules=["pydssr/dssr", "pydssr/dssr_classes", "pydssr/parser", "pydssr/settings"],
    include_package_data=True
)