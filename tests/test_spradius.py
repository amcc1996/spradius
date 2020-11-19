import os
import pathlib

import numpy as np
import pytest

from numpy.testing import assert_allclose

from spradius import generalised_alpha, hht, newmark


dt = np.logspace(-3, 3, num=10, endpoint=True)
current_path = pathlib.Path(__file__).parent.absolute()


@pytest.mark.parametrize(
    "scheme",
    [newmark(dt, beta=0.3025, gamma=0.6)]
    + [hht(dt, alpha=0.3)]
    + [generalised_alpha(dt, rho_infty=0.2)],
)
def test_integrator(scheme):
    """Test if an integrator predicts the same reference values."""
    file = os.path.join(
        current_path,
        os.path.join("baseline", "{0}.txt".format(type(scheme).__name__)),
    )

    reference_values = np.loadtxt(file)
    print(scheme.spectral_radius)
    print(reference_values)

    assert_allclose(
        scheme.spectral_radius, reference_values, rtol=1e-7, atol=0
    )
