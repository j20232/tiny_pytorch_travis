import sys
from setuptools import setup, find_packages

sys.path.append("./src")
sys.path.append("./test")

setup(
    name="tiny_pytorch_travis",
    version="0.1",
    description="sample",
    packages=find_packages(),
    test_suite="torch_test.suite"
)
