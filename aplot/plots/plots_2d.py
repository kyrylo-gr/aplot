import typing as _t

import matplotlib as mpl
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import make_axes_locatable

from . import utils


class ImageResult(_t.NamedTuple):
    axes: _t.Union[Axes, _t.List[Axes], _t.List[_t.List[Axes]]]
    im: mpl.image.AxesImage
    cbar: _t.Any


def imshow_kwds(
    x: _t.Optional[_t.Union[np.ndarray, list]] = None,
    y: _t.Optional[_t.Union[np.ndarray, list]] = None,
):
    """Return a dictionary of kwds that can be used to make
    imshow(z, **imshow_kwds(xarray, yarray)) look the same as pcolor(xarray, yarray, z)
    imshow will be way faster than pcolor, however, it will give the correct result only
    if xarray and yarray are regularly spaced arrays."""
    extent = [x[0], x[-1], y[0], y[-1]] if x is not None and y is not None else None
    return dict(aspect="auto", origin="lower", interpolation="None", extent=extent)


@utils.plot_decorator
def imshow(
    ax: _t.Union[Axes, _t.List[Axes], _t.List[_t.List[Axes]]],
    data: np.ndarray,
    x: _t.Optional[np.ndarray] = None,
    y: _t.Optional[np.ndarray] = None,
    labels: _t.Optional[dict] = None,
    **kwargs,
):
    utils.push_labels_to_kwargs(labels, kwargs)

    if isinstance(ax, (tuple, list, np.ndarray)):
        return utils.run_plot_on_axes_list(imshow, ax, data, x=x, y=y, **kwargs)

    if x is not None and y is not None and (len(data) != len(y) or len(data[0]) != len(x)):
        raise ValueError(f"Wrong shapes. {len(data)} != {len(y)} or {len(data[0])} != {len(x)}")

    im = ax.imshow(
        data,
        **imshow_kwds(x, y),
        **utils.filter_set_kwargs(mpl.image.AxesImage, ["vmin", "vmax", "norm"], **kwargs),  # type: ignore
    )
    if kwargs.get("colorbar", True):
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        fig: _t.Optional[Figure] = ax.get_figure()
        if fig is None:
            raise ValueError("The figure is None cannot add colorbar")
        cbar = fig.colorbar(im, cax=cax, orientation="vertical")
        cbar.ax.set_ylabel(kwargs.get("bar_label", ""))
    utils.set_params(ax, **kwargs)
    return ImageResult(ax, im, cbar)


@utils.plot_decorator
def pcolorfast(
    ax: Axes,
    x: _t.Optional[np.ndarray],
    y: _t.Optional[np.ndarray],
    data: np.ndarray,
    labels: _t.Optional[dict] = None,
    **kwargs,
):
    utils.push_labels_to_kwargs(labels, kwargs)

    if isinstance(ax, (tuple, list, np.ndarray)):
        return utils.run_plot_on_axes_list(pcolorfast, ax, data, x=x, y=y, **kwargs)

    im = ax.pcolorfast(
        x=x,
        y=y,
        data=data,
        **utils.filter_set_kwargs(mpl.image.AxesImage, **kwargs),
    )
    utils.set_params(ax, **kwargs)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    if fig is None:
        raise ValueError("The figure is None cannot add colorbar")
    cbar = fig.colorbar(im, cax=cax, orientation="vertical")
    cbar.ax.set_ylabel(kwargs.get("bar_label", ""))
    return ImageResult(ax, im, cbar)
