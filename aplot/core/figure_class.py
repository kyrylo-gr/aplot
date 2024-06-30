from typing import TYPE_CHECKING, Any, Literal, Optional, TypeVar, overload

import matplotlib.pyplot as plt
from matplotlib.figure import Figure as MplFigure

if TYPE_CHECKING:
    from mpl_toolkits.mplot3d.axes3d import Axes3D as MplAxes3D
    from matplotlib.projections.polar import PolarAxes as MplPolarAxes

from .axes_class import AAxes

_T = TypeVar("_T")


class AFigure(MplFigure):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Custom method example
    def custom_draw_method(self):
        print("Custom drawing behavior here")

    def add_subplot(self, *args, **kwargs) -> AAxes:  # type: ignore
        # Ensuring that the custom axes class is used
        if "projection" not in kwargs and "polar" not in kwargs:
            kwargs.update({"axes_class": AAxes})
        return super().add_subplot(*args, **kwargs)

    def savefig(self, fname: Any, *, transparent=None, **kwargs):  # type: ignore
        super().savefig(fname, transparent=transparent, **kwargs)
        return self

    def tight_layout(self, *args, **kwargs):  # type: ignore
        super().tight_layout(*args, **kwargs)
        return self

    @overload
    def add_axes(self, rect, projection: Literal["3d"]) -> "MplAxes3D": ...  # type: ignore
    @overload
    def add_axes(self, rect, projection: Literal["polar"]) -> "MplPolarAxes": ...  # type: ignore
    @overload
    def add_axes(self, rect, polar: Literal[True]) -> "MplPolarAxes": ...  # type: ignore
    @overload
    def add_axes(self, rect, projection: Optional[str], polar: bool) -> AAxes: ...  # type: ignore
    @overload
    def add_axes(self, ax: _T) -> _T: ...  # type: ignore

    def add_axes(self, *args, **kwargs):  # type: ignore
        if "projection" not in kwargs and "polar" not in kwargs:
            kwargs.update({"axes_class": AAxes})
        return super().add_axes(*args, **kwargs)  # type: ignore

    def show(self):  # type: ignore
        plt.show(self)
