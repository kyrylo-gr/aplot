import typing as _t

import numpy as np

from .fit_logic import FitLogic

FLOAT = _t.Union[float, np.float_]


class HyperbolaParam(_t.NamedTuple):
    semix: FLOAT
    semiy: FLOAT
    x0: FLOAT
    y0: FLOAT


class Hyperbola(FitLogic[HyperbolaParam]):
    param: _t.Type[HyperbolaParam] = HyperbolaParam
    _offset: float = 0

    @staticmethod
    def func(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, semix: FLOAT, semiy: FLOAT, x0: FLOAT, y0: FLOAT
    ):
        return y0 + np.sign(semiy) * np.sqrt(
            semiy**2 + (semiy**2 / semix**2) * (x - x0) ** 2
        )

    @staticmethod
    def _guess(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, y: np.ndarray, **kwargs
    ):
        if len(y) == 0 or len(x) == 0:
            return HyperbolaParam(
                semix=0.0,
                semiy=1.0,
                x0=0.0,
                y0=0.0,
            )
        direction = kwargs.get("direction")
        if direction is None:
            cumsum_len = len(y) // 10
            if cumsum_len == 0:
                cumsum_len = 1

            smoth_y = np.convolve(y, np.ones(cumsum_len) / cumsum_len, mode="valid")
            smoth_y = np.diff(smoth_y)
            direction = (
                1
                if np.mean(smoth_y[:cumsum_len]) > np.mean(smoth_y[-cumsum_len:])
                else -1
            )
        # print("direction", direction)
        x0: FLOAT = x[np.argmax(y)] if direction > 0 else x[np.argmin(y)]
        y0: FLOAT = np.max(y) if direction > 0 else np.min(y)
        return HyperbolaParam(
            semix=np.std(x),
            semiy=-np.std(y) * direction,
            x0=x0,
            y0=y0,  # np.mean(y),
        )
