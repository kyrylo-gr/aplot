import typing as _t

import numpy as np

# from ffit import FIT_FUNCTIONS
# from ffit.fit_results import FitResult
from matplotlib.axes import Axes as MplAxes
from matplotlib.collections import QuadMesh
from matplotlib.image import AxesImage
from mpl_toolkits.axes_grid1 import make_axes_locatable

from .typing import NoneType, noneType
from .utils import (
    filter_none,
    filter_none_types,
    filter_set_kwargs,
    get_auto_args,
    imshow_kwds,
)

_T = _t.TypeVar("_T")
if _t.TYPE_CHECKING:
    from .figure_class import AFigure


WRAPPER_METHODS = {
    "legend",
    "inset_axes",
    "indicate_inset",
    "indicate_inset_zoom",
    "secondary_xaxis",
    "secondary_yaxis",
    "text",
    "annotate",
    "axhline",
    "axvline",
    "axline",
    "axhspan",
    "axvspan",
    "hlines",
    "vlines",
    "eventplot",
    "plot",
    "plot_date",
    "loglog",
    "semilogx",
    "semilogy",
    "acorr",
    "xcorr",
    "step",
    "bar",
    "barh",
    "bar_label",
    "broken_barh",
    "stem",
    "pie",
    "errorbar",
    "boxplot",
    "bxp",
    "scatter",
    "hexbin",
    "arrow",
    "quiverkey",
    "quiver",
    "barbs",
    "fill",
    "fill_between",
    "fill_betweenx",
    "imshow",
    "pcolor",
    "pcolormesh",
    "pcolorfast",
    "contour",
    "contourf",
    "clabel",
    "hist",
    "stairs",
    "hist2d",
    "psd",
    "csd",
    "magnitude_spectrum",
    "phase_spectrum",
    "cohere",
    "specgram",
    "spy",
    "matshow",
    "violinplot",
    "violin",
    "reset_position",
    "sharex",
    "sharey",
    "clear",
    "cla",
    "apply_aspect",
    "add_artist",
    "add_child_axes",
    "add_collection",
    "add_image",
    "add_line",
    "add_patch",
    "add_table",
    "add_container",
    "relim",
    "update_datalim",
    "autoscale",
    "autoscale_view",
    "draw",
    "draw_artist",
    "redraw_in_frame",
    "grid",
    "ticklabel_format",
    "locator_params",
    "tick_params",
    "invert_xaxis",
    "invert_yaxis",
    "minorticks_on",
    "minorticks_off",
    "start_pan",
    "end_pan",
    "drag_pan",
    "twinx",
    "twiny",
}

FILTER_KWARGS = {"hist2d", QuadMesh}


class AAxes(
    MplAxes,
    _t.Generic[_T],
):
    name = "AAxis"  # Give a name for the matplotlib registry
    _last_result = None
    # _fit_result: FitResult | None = None
    # __all__ = MplAxes.__all__ + ["fit", "last_result", "fit_result", "res", "set"]
    # __dict__ = MplAxes.__dict__  ("fit", "last_result", "fit_result", "res", "set")

    # def fit(self, func: str, *args, **kwargs):
    #     lines = self.get_lines()
    #     if not lines:
    #         raise ValueError("No lines found in the axes.")
    #     line = lines[0]
    #     x = np.array(line.get_xdata())
    #     y = np.array(line.get_ydata())

    #     if isinstance(func, str):
    #         if func not in FIT_FUNCTIONS:
    #             raise ValueError(
    #                 f"Function {func} not found in the fit functions."
    #                 f"Possible fit functions ara {list(FIT_FUNCTIONS.keys())}."
    #                 "You can also pass a callable function."
    #             )
    #         fit_func = FIT_FUNCTIONS[func]
    #         self._fit_result = fit_func.fit(x=x, data=y, *args, **kwargs).plot(ax=self, **kwargs)
    #     else:
    #         raise NotImplementedError("Custom fit functions are not implemented yet.")
    #     return self

    @property
    def last_result(self) -> _T:
        return self._last_result  # type: ignore

    # @property
    # def fit_result(self) -> FitResult | None:
    #     return self._fit_result

    @property
    def res(self) -> _T:
        return self._last_result  # type: ignore

    @property
    def fig(self):
        return self.figure

    def __getattribute__(self, name: str):
        # if hasattr(self, name):
        #     raise AttributeError(f"Attribute {name} not found in {self.name}")
        # print(name)

        if name.startswith("set") or name in WRAPPER_METHODS:
            func = super().__getattribute__(name)

            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if isinstance(result, (MplAxes, AAxes)):
                    return result
                self._last_result = result
                return self

            return wrapper
        # TODO: if plot function kwargs should be filtered
        return super().__getattribute__(name)

    def set(  # type: ignore
        self,
        title: str | None | NoneType = noneType,
        xlabel: str | None | NoneType = noneType,
        ylabel: str | None | NoneType = noneType,
        grid: bool | None = None,
        **kwargs,
    ):
        kwargs = filter_set_kwargs(AAxes, **kwargs)
        if grid is not None:
            self.grid(grid)
        kwargs.update(
            {
                "title": title,
                "xlabel": xlabel,
                "ylabel": ylabel,
            }
        )
        super().set(**filter_none_types(kwargs))
        return self

    def hist2d(
        self,
        x,
        y=None,
        bins=10,
        range=None,  # pylint: disable=redefined-builtin
        density=False,
        weights=False,
        cmin=None,
        cmax=None,
        **kwargs,
    ):
        if y is None:
            x = np.array(x)
            x = x[:, 0]
            y = x[:, 1]
        return super().hist2d(x, y, bins, range, density, weights, cmin, cmax, **kwargs)

    def z_parametric(self, z, **kwargs):
        self.plot(np.real(z), np.imag(z), **kwargs)
        return self

    def z_historograms(self, z, **kwargs):
        self.hist2d(np.real(z), np.imag(z), **kwargs)
        return self

    def imshow(  # type: ignore
        self,
        data,
        x=None,
        y=None,
        cmap=None,
        norm=None,
        *,
        aspect=None,
        interpolation=None,
        alpha=None,
        vmin=None,
        vmax=None,
        origin=None,
        extent=None,
        interpolation_stage=None,
        filternorm=True,
        filterrad=4.0,
        resample=None,
        url=None,
        colorbar: bool = True,
        **kwargs,
    ):
        if x is not None and y is not None and (len(data) != len(y) or len(data[0]) != len(x)):
            raise ValueError(f"Wrong shapes. {len(data)} != {len(y)} or {len(data[0])} != {len(x)}")

        imshow_kwargs: dict = imshow_kwds(x, y)
        imshow_kwargs.update(
            **filter_none(
                cmap=cmap,
                norm=norm,
                aspect=aspect,
                interpolation=interpolation,
                alpha=alpha,
                vmin=vmin,
                vmax=vmax,
                origin=origin,
                extent=extent,
                interpolation_stage=interpolation_stage,
                filternorm=filternorm,
                filterrad=filterrad,
                resample=resample,
                url=url,
            )
        )

        im = super().imshow(
            data,
            **imshow_kwargs,
            **filter_set_kwargs(AxesImage, **kwargs),
        )

        if colorbar:
            divider = make_axes_locatable(self)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            fig: _t.Optional[AFigure] = self.get_figure()  # type: ignore
            if fig is None:
                raise ValueError("The figure is None cannot add colorbar")
            cbar = fig.colorbar(im, cax=cax, orientation="vertical")
            cbar.ax.set_ylabel(kwargs.get("bar_label", ""))
        else:
            cbar = None

        return self

    def pcolorfast(  # type: ignore
        self,
        *args,
        x: _t.Optional[np.ndarray] = None,
        y: _t.Optional[np.ndarray] = None,
        data: _t.Optional[np.ndarray] = None,
        labels: _t.Optional[dict] = None,
        colorbar: bool = True,
        **kwargs,
    ):
        if len(args) == 1:
            data = args[0]
        elif len(args) == 3:
            x, y, data = args
        elif len(args) > 0:
            raise ValueError(f"Wrong number of arguments: {len(args)}. Should be 0, 1 or 3.")

        if data is None:
            raise ValueError("Data should be provided")
        if x is not None and y is not None:
            im = super().pcolorfast(
                x,
                y,
                data,
                # **filter_set_kwargs(AxesImage, **kwargs),
            )
        else:
            im = super().pcolorfast(
                data,
                # **filter_set_kwargs(AxesImage, **kwargs),
            )

        # utils.set_params(ax, **kwargs)
        divider = make_axes_locatable(self)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        fig = self.get_figure()
        if fig is None:
            raise ValueError("The figure is None cannot add colorbar")
        if colorbar:
            cbar = fig.colorbar(im, cax=cax, orientation="vertical")
            cbar.ax.set_ylabel(kwargs.get("bar_label", ""))
        return self

    def autoaxis(self, level: int = 0, func_name="plot") -> "AAxes":
        variables = get_auto_args(level, func_name)
        # print(variables)
        if variables and len(variables) >= 2:
            self.set(xlabel=variables[0], ylabel=variables[1])
        return self

    def tight_layout(self, *, pad=1.08, h_pad=None, w_pad=None, rect=None):
        self.figure.tight_layout(pad=pad, h_pad=h_pad, w_pad=w_pad, rect=rect)  # type: ignore

    def plot(self, *args, keep_xlims: bool = False, keep_ylims: bool = False, **kwargs):
        xlims = self.get_xlim() if keep_xlims else None
        ylims = self.get_ylim() if keep_ylims else None
        res = super().plot(*args, **kwargs)
        if xlims is not None:
            self.set_xlim(*xlims)
        if ylims is not None:
            self.set_ylim(*ylims)
        return res

    def __add__(self, other):
        from .axes_list import AxesList

        if isinstance(other, list):
            return AxesList([self] + other)  # type: ignore
        return AxesList([self, other])  # type: ignore
