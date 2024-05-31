# flake8: noqa: E302, E704
import typing as _t
from typing import List, overload

from .axes_class import AAxes
from .axes_list import AxesList
from .figure_class import AFigure

_S = _t.TypeVar("_S", bound=AxesList)

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
@overload
def axs() -> AAxes[None]: ...
@overload
def axs(nrows: _t.Literal[1], ncols: _t.Literal[1], **kwargs) -> AAxes[None]: ...  # type: ignore
@overload
def axs(nrows: _t.Literal[1], ncols: int, **kwargs) -> AxesList[AAxes[None]]: ...
@overload
def axs(nrows: int, ncols: _t.Literal[1], **kwargs) -> AxesList[AAxes[None]]: ...
@overload
def axs(nrows: int, ncols: int, **kwargs) -> AxesList[AxesList[AAxes[None]]]: ...
@overload
def axs(nrows: _S) -> _S: ...
@overload
def axs(nrows: List[AAxes]) -> AxesList[AAxes[None]]: ...
@overload
def axs(nrows: List[List[AAxes]]) -> AxesList[AxesList[AAxes[None]]]: ...
@overload
def axs(nrows: _t.Union[List[int], _t.Tuple[int]]) -> AxesList[AAxes[None]]: ...
def axs(nrows: int = 1, ncols: int = 1, **kwargs): ...
def subplot(*args, **kwargs) -> AAxes: ...
def ax(*args) -> AAxes: ...
def gcf() -> AFigure: ...
def close() -> None: ...
def show(*args, **kwargs) -> AAxes: ...
