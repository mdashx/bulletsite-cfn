from setuptools import find_packages, setup

setup(
    name="bulletsite",
    version="0.0.1",
    description="Build CloudFormation template for deploying a static site.",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    include_package_data=True,
    install_requires=["troposphere"],
)
