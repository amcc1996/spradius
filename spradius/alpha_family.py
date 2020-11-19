"""Alpha-Family of time integrators.

This module contains the abstract definition of a general time
integration scheme of the alpha-family. The abstract defintion was
devised from the generalised-alpha method but the computation of
the integration parameters is individualised for each scheme.

Each method shall only specify the correct function to determined
the integration parameters.

1. Chung J, Hulbert GM. A Time Integration Algorithm for Structural
Dynamics With Improved Numerical Dissipation: The Generalized-alpha Method.
J Appl Mech. 1993 Jun 1;60(2):371–5.

..module:: alpha_family
  :synopsis: Alpha-family abstract class

..moduleauthor:: A. M. Couto Carneiro <amcc@fe.up.pt>
"""

from spradius.integrator import integrator


class alpha_family(integrator):
    """Alpha family abstract class

    Attributes
    ----------
    beta : mfr
      Beta parameter for Newmark interpolation
    gamma : mfr
      Gamma parameter for Newmark interpolation
    alpha_f : mfr
      Generalised midpoint for the evaluation of internal and damping
      forces
    alpha_m : mfr
      Generalised midpoint for the evaluation of the kinetic forces
    """

    @staticmethod
    def get_amplification_matrix_dim():
        return 3

    def update_velocity_acceleration(
        self, dt, disp_this, disp_last, vel_last, accel_last
    ):
        """Newmark velocity and acceleration update routine.

        Parameters
        ----------
        dt : mfr
          Time step
        disp_this : mfr
          Displacement at the current time step
        disp_last : mfr
          Displacement at the last time step
        vel_last : mfr
          Velocity at the last time step
        accel_last : mfr
          Acceleration at the last time step

        Returns
        -------
        vel_this : mfr
          Updated velocity at the current time step
        accel_this : mfr
          Updated acceleration at the current time step
        """

        vel_this = (
            self.gamma / (self.beta * dt) * (disp_this - disp_last)
            + (1 - self.gamma / self.beta) * vel_last
            + dt * (1 - self.gamma / (2 * self.beta)) * accel_last
        )

        accel_this = (
            1 / (self.beta * dt ** 2) * (disp_this - disp_last)
            - 1 / (self.beta * dt) * vel_last
            + (1 - 1 / (2 * self.beta)) * accel_last
        )

        return vel_this, accel_this

    def integrate(self, dt, num_steps, init_disp, init_vel, init_accel):
        """Implementation of the abstract interface for time integration
        for the case of alpha-family integrators.
        """

        # Initialise the kinetical quantities
        disp_last = init_disp
        vel_last = init_vel

        if init_accel != 0:
            accel_last = init_accel
        else:
            accel_last = -self.stif * init_disp

        disp_this = disp_last

        # Loop over the time steps
        for i in range(num_steps):
            # Update the velocity and acceleration with the previous solution
            vel_this, accel_this = self.update_velocity_acceleration(
                dt, disp_this, disp_last, vel_last, accel_last
            )

            # Evaluate the residual equation
            int_forces = self.stif * (
                (1 - self.alpha_f) * disp_this + self.alpha_f * disp_last
            )
            dmp_forces = self.damp * (
                (1 - self.alpha_f) * vel_this + self.alpha_f * vel_last
            )
            kin_forces = self.mass * (
                (1 - self.alpha_m) * accel_this + self.alpha_m * accel_last
            )

            residual = int_forces + dmp_forces + kin_forces

            # Set the dyanmics stiffness and solve the system of equations
            dynstiff = (
                (1 - self.alpha_m) / (self.beta * dt ** 2) * self.mass
                + (1 - self.alpha_f)
                * self.gamma
                / (self.beta * dt)
                * self.damp
                + (1 - self.alpha_f) * self.stif
            )

            incr_disp = -residual / dynstiff

            disp_this = disp_last + incr_disp

            # Update the velocity and acceleration with the correct solution
            vel_this, accel_this = self.update_velocity_acceleration(
                dt, disp_this, disp_last, vel_last, accel_last
            )

            disp_last = disp_this
            vel_last = vel_this
            accel_last = accel_this

        return disp_this, vel_this, accel_this
