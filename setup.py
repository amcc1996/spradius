"""Setup file for spradius package
"""
# Import modules
# --------------
import os

from setuptools import find_packages, setup


# Get path of the package, where steup.py is located
here = os.path.abspath(os.path.dirname(__file__))

# Read the verison number
with open(os.path.join(here, "VERSION")) as versionFile:
    version = versionFile.read().strip()

# Store the README.md file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    longDescription = f.read()

setup(
    # Project name
    name="spradius",
    # Version from the version file
    version=version,
    # Short description
    description="A spectral radius package for time-integration in solid dynamics",
    # Long descriptionf from README.md
    long_description=longDescription,
    long_description_content_type="text/markdown",
    # Github url
    url="https://github.com/amcc1996/spradius",
    download_url="https://github.com/amcc1996/spradius/releases/tag/"
    + version,
    # Authors
    author="António Manuel Couto Carneiro @FEUP",
    author_email="amcc@fe.up.pt",
    # Licensing
    licence="MIT",
    # Classifiers (selected from https://pypi.org/classifiers/)
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    # Keywords
    keywords="time-integration dynamics spectral-radius python3",
    # Project URLs
    project_urls={
        "Source": "https://github.com/amcc1996/spradius",
        "Tracker": "https://github.com/amcc1996/spradius/issues",
    },
    # Include packages in distribution archives
    packages=find_packages(),
    # Python version compatibility
    python_requires=">=3.6, <3.9",
    install_requires=["mpmath>=1.1.0", "numpy>=1.19.4", "tqdm>=4.52.0"],
)
