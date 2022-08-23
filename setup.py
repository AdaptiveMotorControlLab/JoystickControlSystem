#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Joystick control system
© M.W. Mathis
https://github.com/AdaptiveMotorControlLab/JoystickControlSystem
Please see contributors.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="teensy_tasks",
    version="0.0.1",
    author="M.W. Mathis",
    author_email="mathis@rowland.harvard.edu",
    description="Systems neuroscience joystick control task suite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdaptiveMotorControlLab/JoystickControlSystem",
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "scikit-image",
        "scikit-learn",
        "scipy",
        "jupyter-book",
        "numpydoc",
    ],
    extras_require={
        "docs": ["numpydoc"],
        "docs": ["ghp-import"],
    },
    packages=setuptools.find_packages(),
    data_files=[
        (
            "teensy_tasks",
            [
                "teensy_tasks/docs/images/logo.png",
            ],
        )
    ],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    entry_points="""[console_scripts]
            unset=unset:main""",
)

# https://www.python.org/dev/peps/pep-0440/#compatible-release
