import typing as _t

import numpy as np

from .fit_logic import FitLogic


class DampedExpParam(_t.NamedTuple):
    amplitude: float
    tau: float
    offset: float


class DampedExp(FitLogic[DampedExpParam]):
    param: _t.Type[DampedExpParam] = DampedExpParam

    @staticmethod
    def func(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, amplitude: float, tau: float, offset: float
    ):
        return np.exp(-x / tau) * amplitude + offset

    @staticmethod
    def _guess(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, y: np.ndarray, **kwargs
    ):
        return np.max(y) - np.min(y), (np.max(x) - np.min(x)) / 5, np.mean(y)
