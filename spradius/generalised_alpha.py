"""Generalised-alpha method.

This module contains the implementation of the generalised alpha
integrator.

1. Chung J, Hulbert GM. A Time Integration Algorithm for Structural
Dynamics With Improved Numerical Dissipation: The Generalized-alpha Method.
J Appl Mech. 1993 Jun 1;60(2):371–5.

..module:: generalised_alpha
  :synopsis: Generalised-Alpha Class

..moduleauthor:: A. M. Couto Carneiro <amcc@fe.up.pt>
"""

import mpmath

from spradius.alpha_family import alpha_family
from spradius.integrator import PRECISION


mpmath.mp = PRECISION


class generalised_alpha(alpha_family):
    def initialise(self, **kwargs):
        self.rho_infty = kwargs["rho_infty"]
        self.alpha_m = mpmath.mpf((2 * self.rho_infty - 1)) / (
            self.rho_infty + 1
        )
        self.alpha_f = mpmath.mpf(self.rho_infty) / (self.rho_infty + 1)
        self.beta = (
            mpmath.mpf(1.0) / 4.0 * (1 - self.alpha_m + self.alpha_f) ** 2
        )
        self.gamma = mpmath.mpf(1.0) / 2.0 - self.alpha_m + self.alpha_f
