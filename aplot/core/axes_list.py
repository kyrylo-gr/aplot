import typing as _t

import numpy as np

from .axes_class import AAxes
from .utils import filter_set_kwargs, pop_from_dict

# from matplotlib import pyplot as plt


_T = _t.TypeVar("_T", bound="AAxes|AxesList")


class AxesList(_t.List[_T]):
    def set(self, **kwargs):
        kwargs = filter_set_kwargs(AAxes, **kwargs)
        for k, v in kwargs.items():
            if isinstance(v, (list, tuple)) and len(self) == len(v):
                for ax, val in zip(self, v):
                    ax.set(**{k: val})
            else:
                for ax in self:
                    ax.set(**{k: v})
        return self

    # def __getitem__(self, k):

    def plot(self, x, data, *args, scalex: bool = True, scaley: bool = True, **kwargs):
        if len(x) != len(data):
            if len(data) != len(self):
                raise ValueError(
                    "Data should be the same length as x or the same length as the number of axes"
                )
            for i, ax in enumerate(self):
                ax.plot(x, data[i], *args, **kwargs)
        else:
            if len(data) != len(self):
                raise ValueError("Data should be the same length as the number of axes")
            for i, ax in enumerate(self):
                ax.plot(x[i], data[i], *args, **kwargs)
        return self

    def plot_z_1d(
        self: _t.List[AAxes],
        x: np.ndarray,
        z: np.ndarray,
        plot_format: _t.Literal["bode", "real_imag"] = "bode",
        unwrap: bool = False,
        **kwargs,
    ):
        # if not isinstance(self[0], AxesList):
        #     raise ValueError("This method should be called on an AxesList with 2 axes")

        if plot_format == "bode":
            data1 = np.abs(z)
            data2 = np.angle(z) * 180 / np.pi
            if unwrap:
                data2 = np.unwrap(data2, period=360)
            self[0].set_title("Amplitude")
            self[1].set_title("Phase")
        elif plot_format == "real_imag":
            data1 = np.real(z)
            data2 = np.imag(z)
            self[0].set_title("Real")
            self[1].set_title("Imag")
        else:
            raise ValueError("Plot_format should be either bode or real_imag")

        kwargs_without_xlabel = pop_from_dict(kwargs, "xlabel")
        self[0].plot(x, data1, **kwargs_without_xlabel)
        self[1].plot(x, data2, **kwargs)

        return self

    def plot_z_2d(
        self: "AxesList[AAxes]",
        x: np.ndarray,
        y: np.ndarray,
        z: np.ndarray,
        plot_format: _t.Literal["bode", "real_imag"] = "bode",
        unwrap: bool = True,
        # cmap: _t.Optional[str] = None,
        **kwargs,
    ):
        # if not isinstance(self[0], AAxes):
        #     raise ValueError("This method should be called on an AxesList with 2 axes")

        if plot_format == "bode":
            data1 = 20 * np.log10(np.abs(z))
            data2 = np.angle(z) * 180 / np.pi
            if unwrap:
                data2 = np.unwrap(data2, period=360)
            self[0].set_title("Amplitude")
            self[1].set_title("Phase")
        elif plot_format == "real_imag":
            data1 = np.real(z)
            data2 = np.imag(z)
            self[0].set_title("Real")
            self[1].set_title("Imag")
        else:
            raise ValueError("Plot_format should be either bode or real_imag")

        kwargs_without_xlabel = pop_from_dict(kwargs, "xlabel")
        self[0].pcolorfast(x=x, y=y, data=data1, **kwargs_without_xlabel)
        self[1].pcolorfast(x=x, y=y, data=data2, **kwargs)
        # im = self[0].pcolor(x, y, data1)
        # plt.colorbar(im, ax=self[0])

        # im = self[1].pcolor(x, y, data2)
        # plt.colorbar(im, ax=self[1])

        return self

    def imshow(self, data, *args, **kwargs):
        if len(data) == len(self):
            for i, ax in enumerate(self):
                ax.imshow(data=data[i], *args, **kwargs)
        else:
            if len(data) == 1:
                data = data[0]
            for i, ax in enumerate(self):
                ax.imshow(data=data, *args, **kwargs)
        return self

    def tight_layout(self, *, pad=1.08, h_pad=None, w_pad=None, rect=None):
        self.figure.tight_layout(pad=pad, h_pad=h_pad, w_pad=w_pad, rect=rect)  # type: ignore
        return self

    @property
    def figure(self):
        return self[0].figure

    @property
    def fig(self):
        return self.figure

    def map(self, func: _t.Callable[[AAxes], _t.Any]):
        for ax in self:
            func(ax)
        return self

    def suptitle(self, title):
        self.figure.suptitle(title)
        return self

    def legend(self: _T, *args, **kwargs) -> _T:
        for ax in self:
            ax.legend(*args, **kwargs)
        return self

    # TODO: if self[0] has a method, then call it on all axes
