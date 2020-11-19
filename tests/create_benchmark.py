import os
import pathlib
import sys

import numpy as np

from spradius import generalised_alpha, hht, newmark


# From: https://stackoverflow.com/questions/3041986/apt-command-
# line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n"
            )


current_path = pathlib.Path(__file__).parent.absolute()
if len(os.listdir(os.path.join(current_path, "baseline"))) != 0:
    flag = query_yes_no(
        "The tests/baseline, were the reference results "
        "for code testing are store, is not emtpy.\nDo "
        "you really want to update the benchmarks?"
    )

if flag:
    # Generate benchmark cases
    dt = np.logspace(-3, 3, num=10, endpoint=True)

    case = newmark(dt, beta=0.3025, gamma=0.6)
    file = os.path.join(
        current_path,
        os.path.join("baseline", "{0}.txt".format(type(case).__name__)),
    )
    np.savetxt(file, case.spectral_radius)

    case = hht(dt, alpha=0.3)
    file = os.path.join(
        current_path,
        os.path.join("baseline", "{0}.txt".format(type(case).__name__)),
    )
    np.savetxt(file, case.spectral_radius)

    case = generalised_alpha(dt, rho_infty=0.2)
    file = os.path.join(
        current_path,
        os.path.join("baseline", "{0}.txt".format(type(case).__name__)),
    )
    np.savetxt(file, case.spectral_radius)
