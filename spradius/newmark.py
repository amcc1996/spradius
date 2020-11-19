"""Newmark method.

This module contains the implementation of the Newmar method.

1. Newmark NM. A Method of Computation for Structural Dynamics. ASCE Journal
of the Engineering Mechanics Division. 1959;85:67–94.


..module:: newmark
  :synopsis: Newmark Class

..moduleauthor:: A. M. Couto Carneiro <amcc@fe.up.pt>
"""
import mpmath

from spradius.alpha_family import alpha_family
from spradius.integrator import PRECISION


mpmath.mp = PRECISION


class newmark(alpha_family):
    def initialise(self, **kwargs):
        if len(kwargs) == 0:
            self.beta = mpmath.mpf(0.25)
            self.gamma = mpmath.mpf(0.5)
        else:
            self.beta = mpmath.mpf(kwargs["beta"])
            self.gamma = mpmath.mpf(kwargs["gamma"])
        self.alpha_m = 0
        self.alpha_f = 0

    @staticmethod
    def get_amplification_matrix_dim():
        return 2
