from setuptools import setup, find_packages

setup(
    name="secure-source-code-analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gitpython",
        "pyyaml",
        "requests",
    ],
) 