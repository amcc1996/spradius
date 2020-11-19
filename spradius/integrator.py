"""Main integratopm abstract class.

This is the main module of spradius. It contains the abstract definition
of any time integrations strategy to be implemented within this software
and the main routine for computing the spectral radius, based on the
numerical strategy presented in

1. Benítez JM, Montáns FJ. The value of numerical amplification matrices
in time integration methods. Computers & Structures. 2013 Nov 1;128:243–50.

Due to the characteristics of the numerical method, it is required a
significant numerical floating-point procedure. This comes from the fact
that a large number of time steps is needed for an accurate prediciton of
the spectral radius and, as a consequence, the eigenvalues of the
amplification matrix (typically with modulus smaller than 1) will
dangerously decrease to values close to 0. For this reason, the mpmath
package is used, at the cost of substantially reducing the speed.

The mass is set to 1, the damping to 0 and the stiffness to 4*pi^2.
This ensures that the natural period is 1, therefore the input time
step vector actually represents the vector of non-dimensional time
steps often written as Delta t / T_1.

..module:: integrator
  :synopsis: Integrator main class

..moduleauthor:: A. M. Couto Carneiro <amcc@fe.up.pt>
"""

from abc import ABC, abstractmethod

import mpmath
import numpy as np

from tqdm import tqdm


PRECISION = 30
mpmath.mp = PRECISION


class integrator(ABC):

    # Mass, damping and stiffness
    mass = mpmath.mpf(1)
    damp = mpmath.mpf(0)
    stif = 4 * mpmath.pi ** 2

    def __init__(self, dt_list, num_steps=600, **kwargs):
        self.initialise(**kwargs)
        self.spectral_radius = self.compute_spectral_radius(dt_list, num_steps)

    @abstractmethod
    def initialise(self, **kwargs):
        """Initialises the specific integrator with the given keyword
        arguments.
        """
        pass

    @abstractmethod
    def integrate(self, dt, num_steps, init_disp, init_vel, init_accel):
        """Main abstract routine for performing the time-integration.

        Parameters
        ----------
        dt : float
          Time step
        num_steps : int
          Number of time steps to compute
        init_disp : float
          Initial displacement
        init_vel : float
          Initial velocity
        init_accel : float
          Initial acceleration

        Returns
        -------
        disp_this : mfr
          Displacement at the last time step
        vel_this : mfr
          Displacement at the last time step
        accel_this : mfr
          Displacement at the last time step
        """
        pass

    @staticmethod
    @abstractmethod
    def get_amplification_matrix_dim():
        """Returns the dimension of the amplification matrix.

        Each time-integration method is associated with a specific
        dimension of the amplication matrix. This routine serves the
        purpose of controlling this aspect which is relevant in the
        computation of the associated eigenvalues and identification of
        the maximum (spectral radius).
        pass

        Returns
        -------
        ndim : int
          Dimension of the amplification matrix
        """

    def compute_spectral_radius(self, dt_list, num_steps):
        """Spectral radius computation routine.

        The spectral radius is computed approximately by integrating the
        equations of motion for initial unit displacement, velocity and
        acceleration. Each of these runs allows determining one columns of the
        amplification matrix powered to the number of time steps taken.
        The spectral radius of the amplification matrix can be identified by
        taking the n-th root of the eigenvalues of the powered matrix.

        Reference
        ---------
        1. Benítez JM, Montáns FJ. The value of numerical amplification
        matrices in time integration methods. Computers & Structures.
        2013 Nov 1;128:243–50.

        Parameters
        ----------
        dt_list : list /  array of float
          List of all time steps to be evaluated
        num_steps : int
          Number of time steps to perform

        Returns
        -------
        spectral_radius : array of float
          Vector of approximate spectral radius values
        """

        dt_array = np.array(dt_list)
        num_points = np.size(dt_array, axis=0)

        spectral_radius = np.zeros((num_points))
        print(" ")
        for i_dt in tqdm(range(num_points)):

            dt = dt_array[i_dt]

            # Integrate the equations of motion for unit intial conditiosn
            disp_unit_disp, vel_unit_disp, accel_unit_disp = self.integrate(
                dt, num_steps, 1, 0, 0
            )
            disp_unit_vel, vel_unit_vel, accel_unit_vel = self.integrate(
                dt, num_steps, 0, 1, 0
            )
            disp_unit_accel, vel_unit_accel, accel_unit_accel = self.integrate(
                dt, num_steps, 0, 0, 1
            )

            # Build the amplification matrix A^n
            amplification_matrix = mpmath.matrix(
                [
                    [disp_unit_disp, disp_unit_vel, disp_unit_accel],
                    [vel_unit_disp, vel_unit_vel, vel_unit_accel],
                    [accel_unit_disp, accel_unit_vel, accel_unit_accel],
                ]
            )

            # Take only the relevant components
            ndim = self.get_amplification_matrix_dim()
            amplification_matrix = amplification_matrix[0:ndim, 0:ndim]

            # Find the largest of the eigenvalues of A^n
            eigenvalues = mpmath.eig(
                amplification_matrix, left=False, right=False
            )
            modulus_eigenvalues = [mpmath.fabs(x) for x in eigenvalues]
            spectral_radius_to_n = max(modulus_eigenvalues)

            # Compute the spectral radius
            spectral_radius[i_dt] = mpmath.root(
                spectral_radius_to_n, num_steps
            )

        return spectral_radius
