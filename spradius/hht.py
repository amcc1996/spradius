"""Hilbert-Hugher-Taylor alpha method (HHT).

This module contains the implementation of the HHT-alpha transient
integrator.

1. Hilber HM, Hughes TJR, Taylor RL. Improved numerical dissipation
for time integration algorithms in structural dynamics. Earthquake
Engineering & Structural Dynamics. 1977;5(3):283–92.


..module:: hht
  :synopsis: HHT-alpha Classe

..moduleauthor:: A. M. Couto Carneiro <amcc@fe.up.pt>
"""
import mpmath

from spradius.alpha_family import alpha_family
from spradius.integrator import PRECISION


mpmath.mp = PRECISION


class hht(alpha_family):
    def initialise(self, **kwargs):
        self.alpha = kwargs["alpha"]
        self.alpha_f = mpmath.mpf(self.alpha)
        self.alpha_m = mpmath.mpf(0)
        self.beta = mpmath.mpf(1 + self.alpha_f) ** 2 / 4
        self.gamma = mpmath.mpf(1.0) / 2.0 + self.alpha_f
