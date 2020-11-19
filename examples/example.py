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
