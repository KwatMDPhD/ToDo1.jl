from setuptools import find_packages, setup
from clean_ipynb import NAME, VERSION

setup(
    name=NAME,
    version=VERSION,
    url="https://github.com/KwatME/{}".format(NAME),
    author="Kwat Medetgul-Ernar",
    author_email="kwatme8@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['clean_ipynb=clean_ipynb.cli:main']
    },
    python_requires=">=3.6",
    install_requires=("black", "wasabi", "isort", "jupyter", "autoflake", "plac"),
)
