# flake8: noqa: E302, E704
import typing as _t
from typing import overload

from .axes_class import AAxes
from .axes_list import AxesList
from .figure_class import AFigure

def figure(
    num: int | None = None,
    figsize: _t.Tuple | None = None,
    dpi: int | None = None,
    facecolor: str | None = None,
    edgecolor: str | None = None,
    frameon: bool = True,
    FigureClass=AFigure,
    clear: bool = False,
    **kwargs
): ...
@overload
def subplots() -> _t.Tuple[AFigure, AAxes[None]]: ...
@overload
def subplots(  # type: ignore
    nrows: _t.Literal[1],
    ncols: _t.Literal[1],
    *,
    sharex=...,
    sharey=...,
    squeeze=...,
    subplot_kw=...,
    gridspec_kw=...,
    **fig_kw
) -> _t.Tuple[AFigure, AAxes[None]]: ...
@overload
def subplots(
    nrows: _t.Literal[1],
    ncols: int,
    *,
    sharex=...,
    sharey=...,
    squeeze=...,
    subplot_kw=...,
    gridspec_kw=...,
    **fig_kw
) -> _t.Tuple[AFigure, AxesList[AAxes[None]]]: ...
@overload
def subplots(
    nrows: int,
    ncols: _t.Literal[1],
    *,
    sharex=...,
    sharey=...,
    squeeze=...,
    subplot_kw=...,
    gridspec_kw=...,
    **fig_kw
) -> _t.Tuple[AFigure, AxesList[AAxes[None]]]: ...
@overload
def subplots(
    nrows: int,
    ncols: int,
    *,
    sharex=...,
    sharey=...,
    squeeze=...,
    subplot_kw=...,
    gridspec_kw=...,
    **fig_kw
) -> _t.Tuple[AFigure, AxesList[AxesList[AAxes[None]]]]: ...
@overload
def subplots(
    nrows: int = 1,
    ncols: int = 1,
    *,
    sharex: bool = ...,
    sharey: bool = ...,
    squeeze: bool = ...,
    subplot_kw: dict | None = ...,
    gridspec_kw: dict | None = ...,
    **fig_kw
): ...
def subplot(*args, **kwargs) -> AAxes: ...
def ax(*args) -> AAxes: ...
def gcf() -> AFigure: ...
