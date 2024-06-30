import typing as _t

import matplotlib.pyplot as plt
from matplotlib import _pylab_helpers
from matplotlib.projections import register_projection

from .axes_class import AAxes
from .axes_list import AxesList
from .figure_class import AFigure

register_projection(AAxes)


def figure(
    num=None,  # autoincrement if None, else integer from 1-N
    figsize=None,  # defaults to rc figure.figsize
    dpi=None,  # defaults to rc figure.dpi
    facecolor=None,  # defaults to rc figure.facecolor
    edgecolor=None,  # defaults to rc figure.edgecolor
    frameon=True,
    FigureClass=AFigure,
    clear=False,
    **kwargs,
):
    return plt.figure(
        num=num,
        figsize=figsize,
        dpi=dpi,
        facecolor=facecolor,
        edgecolor=edgecolor,
        frameon=frameon,
        FigureClass=FigureClass,
        clear=clear,
        **kwargs,
    )


def subplots(
    nrows: int = 1,
    ncols: int = 1,
    *,
    sharex=False,
    sharey=False,
    squeeze=True,
    width_ratios=None,
    height_ratios=None,
    subplot_kw=None,
    gridspec_kw=None,
    **fig_kw,
):
    fig_kw.update({"FigureClass": AFigure})

    fig, axes = plt.subplots(  # type: ignore
        nrows=nrows,
        ncols=ncols,
        sharex=sharex,
        sharey=sharey,
        squeeze=squeeze,
        width_ratios=width_ratios,
        height_ratios=height_ratios,
        subplot_kw=subplot_kw,  # type: ignore
        gridspec_kw=gridspec_kw,  # type: ignore
        **fig_kw,
    )
    if nrows == 1 and ncols == 1:
        return fig, axes
    if nrows == 1 or ncols == 1:
        return fig, AxesList(axes)
    res = []
    for row in axes:
        res.append(AxesList(row))
    return fig, AxesList(res)


def axs(
    nrows: _t.Union[int, AAxes, _t.List[AAxes], _t.List[int], "AxesList"] = 1,
    ncols: int = 1,
    /,
    **kwargs,
):
    if isinstance(nrows, (AAxes, AxesList)):
        return nrows
    if isinstance(nrows, _t.Iterable):
        if isinstance(nrows[0], int):
            axes = []
            for pos in nrows:
                axes.append(ax(pos))
            return AxesList(axes)
        return AxesList(list(nrows))

    _, axes = subplots(nrows=nrows, ncols=ncols, **kwargs)
    return axes


def subplot(*args, **kwargs) -> AAxes:
    gcf()  # important to not create new figure if one is existing
    return plt.subplot(*args, **kwargs)  # type: ignore


def ax(*args, **kwargs) -> AAxes:
    return subplot(*args, **kwargs)


def gcf():
    """
    Get the current figure.

    If there is currently no figure on the pyplot figure stack, a new one is
    created using `~.pyplot.figure()`.  (To test whether there is currently a
    figure on the pyplot figure stack, check whether `~.pyplot.get_fignums()`
    is empty.)
    """
    manager = _pylab_helpers.Gcf.get_active()
    if manager is not None:
        return manager.canvas.figure  # type: ignore
    else:
        return figure()


def show(*args, **kwargs):
    """Display all open figures.

    Same as plt.show().
    """
    plt.show(*args, **kwargs)


def close():
    """Close all open figures."""
    plt.close("all")
