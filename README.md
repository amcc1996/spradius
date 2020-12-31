<p align="center">
  <a href=""><img alt="spradius" src="https://gist.githubusercontent.com/amcc1996/05147008dcfa4da0dcd886c7f9093e01/raw/3f25eeb0f8011326dd4e2ba7c68393e4e5ddf7c4/spradius.svg" width="60%"></a>
  <p align="center">A spectral radius package for time-integration in solid dynamics.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/spradius.svg?style=flat)](https://pypi.org/project/spradius)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/spradius.svg?style=flat)](https://pypi.org/pypi/spradius/)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/amcc1996/spradius/badge)](https://www.codefactor.io/repository/github/amcc1996/spradius)
[![codecov](https://codecov.io/gh/amcc1996/spradius/branch/main/graph/badge.svg?token=PIU6UDGBGO)](https://codecov.io/gh/amcc1996/spradius)
[![gh-actions](https://img.shields.io/github/workflow/status/amcc1996/spradius/ci?style=flat)](https://github.com/amcc1996/spradius/actions?query=workflow%3Aci)

spRadius is a *not-so-fast* spectral radius numerical computation package for Python specialised in time-integration algorithm for solid dynamics.
It is based on the work of [Benítez and Montáns](https://www.sciencedirect.com/science/article/pii/S0045794913002101?via%3Dihub), who propose an algorithm for computing the amplification matrix and, therefore, the spectral radius, by computing the mechanical response of the system to unit initial conditions.

As clearly mentioned in that work, in general, the spectral radius needs to be computed from the displacement solution during a large number of time steps, owing to the inconsistent initial acceleration evaluation. Since the numerical computation of the spectral radius involves a root with order equal to the number of steps, typical double machine precision is quickly surpassed. To circumvent this pitfall, the arbitrary precision floating-point arithmetic library [mpmath
](http://mpmath.org/) is utilised, at expense of a drastic reduction in performance.

## Installation
Clone this repository into your system
```
git clone git@github.com:amcc1996/spradius.git
```
and install the Python package with `pip3`, running the following command inside spRadius root directory, where the `setup.py` is located
```
pip3 install .
```
Alternatively, you can install it directly from PyPI with
```
pip3 install spradius
```
At this point, spRadius can be imported into your Python scripts and modules the usual Python-way
```python
import spradius
```
## Example
```python
import matplotlib.pyplot as plt
import numpy as np

from spradius import generalised_alpha, hht, newmark


dt = np.logspace(-3, 3, num=100)

rho_newmark = newmark(dt)
rho_newmark2 = newmark(dt, beta=0.3025, gamma=0.6)
rho_hht = hht(dt, alpha=0.05)
rho_hht2 = hht(dt, alpha=0.3)
rho_gen_alpha = generalised_alpha(dt, rho_infty=0.8)
rho_gen_alpha2 = generalised_alpha(dt, rho_infty=0.2)

fig, ax = plt.subplots(
    1, 1, num="spradius example", constrained_layout=True, figsize=(6, 6)
)
ax.semilogx(
    dt,
    rho_newmark.spectral_radius,
    label=r"Newmkark $\beta=0.25$ $\gamma=0.5$",
    clip_on=True,
)
ax.semilogx(
    dt,
    rho_newmark2.spectral_radius,
    label=r"Newmkark $\beta=0.3025$ $\gamma=0.6$",
    clip_on=True,
)
ax.semilogx(
    dt, rho_hht.spectral_radius, label=r"HHT $\alpha=0.05$", clip_on=True
)
ax.semilogx(
    dt, rho_hht2.spectral_radius, label=r"HHT $\alpha=0.3$", clip_on=True
)
ax.semilogx(
    dt,
    rho_gen_alpha.spectral_radius,
    label=r"GEN-$\alpha$ $\rho_{\infty}=0.8$",
    clip_on=True,
)
ax.semilogx(
    dt,
    rho_gen_alpha2.spectral_radius,
    label=r"GEN-$\alpha$ $\rho_{\infty}=0.2$",
    clip_on=True,
)
ax.set_xlabel(r"Non-dimensional time step, $\Delta t / T_1$")
ax.set_ylabel(r"Spectral radius, $\rho$")
ax.set_xlim(dt[0], dt[-1])
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid()

plt.show()
```

<p align="center">
  <a href=""><img alt="spradius_example" src="https://gist.githubusercontent.com/amcc1996/ad55d0995bd37c289a954e31fa2703b3/raw/aac579b35de2243e063b617d5f10aae3bf4aed98/spradius_example.svg" width="50%"></a>
  <p align="center">Example spectral radius plot obtained with spRadius.</p>
</p>

## Running the tests

spRadius [tests](tests) can by run with [pytest](https://docs.pytest.org/en/stable/contents.html) so start by installing the framework
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

## References
1. Benítez JM, Montáns FJ. The value of numerical amplification matrices in time integration methods. Computers & Structures. 2013 Nov 1;128:243–50. 
