import numpy as np


def get_data(length: int = 100, func=np.sin):
    x = np.linspace(0, 2 * np.pi, length)
    y = func(x) * (0.9 + 0.2 * np.random.rand(length))
    return x, y
