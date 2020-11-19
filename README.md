<p align="center">
  <a href=""><img alt="spradius" src="https://gist.github.com/amcc1996/05147008dcfa4da0dcd886c7f9093e01" width="60%"></a>
  <p align="center">A spectral radius package for time-integration in solid dynamics.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/spradius.svg?style=flat)](https://pypi.org/project/spradius)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/spradius.svg?style=flat-square)](https://pypi.org/pypi/spradius/)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/amcc1996/spradius/badge/master?s=aa7aec16e5c3c7c74f96d414568d7c4a2d2227f2)](https://www.codefactor.io/repository/github/amcc1996/spradius/overview/master)
[![codecov](https://codecov.io/gh/amcc1996/spradius/branch/master/graph/badge.svg?token=2JLOK50CJJ)](https://codecov.io/gh/amcc1996/spradius)
[![gh-actions](https://img.shields.io/github/workflow/status/amcc1996/spradius/ci?style=flat)](https://github.com/amcc1996/spradius/actions?query=workflow%3Aci)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amcc1996/bending-playground/master?filepath=bending-diagrams.ipynb)

spRadius is a *not-so fast* spectral radius computation package for Python.

## Installation

### Installing from source
Clone this repository into your system
```
git clone git@github.com:amcc1996/spradius.git
```
and install the Python package with `pip3`, running the following command inside spRadius root directory, where the `setup.py` is located
```
pip3 install .
```
At this point, spRadius can be imported into your Python scripts and modules the usual Python-way
```python
import spradius
```

## Running the tests

SymBeam [tests](tests) can by run with [pytest](https://docs.pytest.org/en/stable/contents.html) so start by installing the framework
```
pip3 install pytest
pip3 install pytest-cov # optional, to generate coverage reports
```
and launch the testing utility from spRadius root directory
```
make tests
```

The coverage reports can be generated with
```
make coverage
```
which will run the test and create the coverage information in `htmlcov`.

## License
Copyright 2020, António Carneiro

spRadius is free and open-source software and is published [MIT License](https://opensource.org/licenses/MIT).
