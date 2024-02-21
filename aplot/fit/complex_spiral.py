import typing as _t

import numpy as np
import numpy.typing as npt

from .fit_logic import FitLogic, FLOAT


class ComplexSpiralParam(_t.NamedTuple):
    amplitude0: FLOAT
    phi0: FLOAT
    freq: FLOAT
    tau: FLOAT
    offset: FLOAT


class ComplexSpiral(FitLogic[ComplexSpiralParam]):
    param: _t.Type[ComplexSpiralParam] = ComplexSpiralParam

    @staticmethod
    def func(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray,
        amplitude0: FLOAT,
        phi0: FLOAT,
        freq: FLOAT,
        tau: FLOAT,
        offset: FLOAT,
    ):
        ampl: np.complex_ = amplitude0 * np.exp(1j * phi0)
        return ampl * np.exp(1j * freq * 2 * np.pi * x - x / tau) + offset + 1j * offset

    @staticmethod
    def _guess(  # pylint: disable=W0221 # type: ignore
        x: np.ndarray, z: np.ndarray, **kwargs
    ):
        the_fft: npt.NDArray[np.complex_] = np.fft.fft(z - z.mean())
        index_max: np.intp = np.argmax(np.abs(the_fft))
        freq: npt.NDArray[np.float_] = np.fft.fftfreq(len(z), d=x[1] - x[0])[index_max]
        ampl: np.float_ = the_fft[index_max]

        return [
            (np.max(np.real(z)) - np.min(np.real(z))) / 2,
            np.angle(ampl),
            freq,
            np.max(x) / 2,
            (np.max(np.real(z)) + np.min(np.real(z))) / 2,
        ]
