import numpy as np
import pandas as pd

import threading as th
import math


def approx_of_delta_function(energ_resolution, energ_of_state, energy_distribution):
    approx_value = 1 / math.pi * (
            energ_resolution / ((energ_of_state - energy_distribution) ** 2 + energ_resolution ** 2))

    return approx_value


