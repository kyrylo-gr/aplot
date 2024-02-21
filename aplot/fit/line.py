import typing as _t

import numpy as np

from .fit_logic import FitLogic, FLOAT


class LineParam(_t.NamedTuple):
    amplitude: float
    offset: float


class Line(FitLogic[LineParam]):
    param: _t.Type[LineParam] = LineParam

    @staticmethod
    def func(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, amplitude: FLOAT, offset: FLOAT
    ) -> np.ndarray:
        return amplitude * x + offset

    @staticmethod
    def _guess(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, z: np.ndarray, **kwargs
    ) -> LineParam:
        average_size = max(len(z) // 10, 1)
        y1 = np.average(z[:average_size])
        y2 = np.average(z[-average_size:])

        amplitude = (y2 - y1) / (x[-1] - x[0])
        offset = y1 - x[0] * amplitude

        return LineParam(amplitude, offset)
