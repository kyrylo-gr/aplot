import typing as _t

import numpy as np

from .axes_class import AAxes
from .utils import filter_set_kwargs, pop_from_dict

# from matplotlib import pyplot as plt


_T = _t.TypeVar("_T", bound="AAxes[_t.Any]|AxesList[AxesList]|AxesList[AAxes]")
_L = _t.TypeVar("_L", bound="AxesList[AAxes]|AxesList[AxesList]")


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

    # def __getitem__(self, item):
    #     # print(item, len(self))
    #     if item >= len(self):
    #         return self.__getitem__(item % len(self))[item // len(self)]
    #     return super().__getitem__(item)

    def plot(self, x, data, *args, axes=None, **kwargs):
        if axes is not None:
            ax = self[axes]
            ax.plot(x, data, *args, **kwargs)
            return self

        if len(x) != len(data):
            if len(data) != len(self):
                raise ValueError(
                    "Data should be the same length as x or the same length as the number of axes"
                )
            for i, ax in enumerate(self):
                ax.plot(x, data[i], *args, **kwargs)
        else:
            if len(data) != len(self):
                for ax in self:
                    ax.plot(x, data, *args, **kwargs)
            else:
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
            for _, ax in enumerate(self):
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
            if isinstance(ax, AxesList):
                ax.map(func)
            else:
                func(ax)
        return self

    def suptitle(self, title: str):
        self.figure.suptitle(title)
        return self

    def legend(self: _L, *args, **kwargs) -> _L:
        for ax in self:
            ax.legend(*args, **kwargs)
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}:{super().__repr__()}"

    def __add__(self, other):  # type: ignore
        if issubclass(type(other), list):
            return self.__class__(super().__add__(other))
        return self.__class__(super().__add__([other]))

    def __getattr__(self, key):
        # print("getattr", key)
        def mapping(*args, **kwargs):
            for ax in self:
                getattr(ax, key)(*args, **kwargs)
            return self

        return mapping
        # return super().__getattribute__(key)

    def __getitem__(self, key: _t.Union[int, _t.Tuple[int, ...]]):  # type: ignore
        if isinstance(key, tuple):
            res = self
            if len(key) == 1:
                res = self[key[0]]
            elif len(key) == 2:
                key1, key2 = key
                res = self[key1]
                if isinstance(key1, slice):
                    res2 = []
                    for r in res:
                        rr = r[key2]
                        if not isinstance(rr, AxesList):
                            rr = AxesList(rr)
                        res2.append(rr)
                    res = res2
                else:
                    res = res[key2]
            else:
                raise ValueError("tuple len should <= 2")
            if not isinstance(res, AxesList):
                return AxesList(res)
            return res
        return super().__getitem__(key)
