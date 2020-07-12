#!/usr/bin/env python

import setuptools  # type: ignore


setuptools.setup(
    name="cps",
    url="https://github.com/stefanbatalka/chinese_poker_solver",
    packages=setuptools.find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
)
