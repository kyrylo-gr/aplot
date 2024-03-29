import typing as _t

import numpy as np

from .fit_logic import FitLogic, FLOAT


class LorentzParam(_t.NamedTuple):
    f0: float
    amplitude: float
    bandwidth: float
    phi0: float
    amplitude0: float
    delay: float
    amplitude_phase: float


class LorentzComplex(FitLogic[LorentzParam]):
    param: _t.Type[LorentzParam] = LorentzParam

    @staticmethod
    def func(  # pylint: disable=W0221 # type: ignore
        freqs: np.ndarray,
        f0: FLOAT,
        ampl: FLOAT,
        bandwidth: FLOAT,
        phi0: FLOAT,
        ampl0: FLOAT,
        delay: FLOAT,
        phaseampl,
    ):
        orig = ampl0 * np.exp(1j * phi0)
        return (
            orig - np.exp(1j * phaseampl) * ampl / (1j * (freqs - f0) / (bandwidth) + 1)
        ) * 1
        # np.exp(1j * 2 * np.pi * (freqs - f0) * delay)

    @staticmethod
    def _guess(  # pylint: disable=W0221 # type: ignore
        freqs: np.ndarray, zs: np.ndarray, **kwargs
    ):
        """
        Estimate the parameters for fitting a model to the given frequency and impedance data.

        Parameters:
        - freqs (array-like): Array of frequency values.
        - zs (array-like): Array of impedance values.

        Returns:
        - f0 (float): Estimated center frequency.
        - ampl (float): Estimated amplitude.
        - bandwidth (float): Estimated bandwidth.
        - phi0 (float): Estimated phase at center frequency.
        - ampl0 (float): Estimated amplitude at center frequency.
        - delay (float): Estimated electrical delay.
        - amplitude_phase (float): Estimated average phase of the impedance.


        References:
        - https://github.com/UlysseREGLADE/abcd_rf_fit#3-estimation-of-the-electrical-delay
        """
        f0 = np.mean(freqs)
        ampl = max(np.abs(zs)) - min(np.abs(zs))
        bandwidth = np.sign(freqs[0]) * (freqs[-1] - freqs[0]) / 10
        phi0 = np.mean(np.angle(zs))
        ampl0 = np.mean(np.abs(zs))

        delay = 0
        amplitude_phase = np.mean(np.angle(zs))

        return f0, ampl, bandwidth, phi0, ampl0, delay, amplitude_phase
