from setuptools import setup, find_packages
import os

name = "pyxi_kafka_api"
description = "A basic restful service that acts as a Kafka proxy."
author = "Simon Stipcich"
author_email = "stipcich.simon@gmail.com"
url = "https://github.com/stiproot/pyxi-kafka-api"
license = "MIT"
keywords = ["python", "package", "kafka", "beta"]
version = "0.0.2"
install_requires = ["environs==9.5.0", "fastapi==0.101.1", "pyxi_kafka_client==0.0.3"]
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=name,
    version=version,
    packages=find_packages(where="src"),
    package_dir={"pyxi_kafka_api": "src/pyxi_kafka_api"},
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)
