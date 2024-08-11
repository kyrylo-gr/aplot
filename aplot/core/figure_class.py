from typing import TYPE_CHECKING, Any, List, Literal, Optional, TypeVar, Union, overload


import matplotlib.pyplot as plt
from matplotlib.figure import Figure as MplFigure

if TYPE_CHECKING:
    from mpl_toolkits.mplot3d.axes3d import Axes3D as MplAxes3D
    from matplotlib.projections.polar import PolarAxes as MplPolarAxes

from .axes_class import AAxes
from .axes_list import AxesList

_T = TypeVar("_T")
_F = TypeVar("_F", bound="AFigure")

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
    @property
    def axes(self) -> "AxesList[AAxes]":  # type: ignore
        return AxesList(self._axstack.as_list())  # type: ignore

    def label_axes(
        self: _F,
        labels: Union[Literal["vertical", "horizontal"], List[str]] = "horizontal",
        *,
        axes: Optional["AxesList"] = None,
    ) -> _F:
        if axes is None:
            axes = self.axes
        axes_list = axes.flat()
        if labels == "horizontal":
            labels = [f"({chr(65+i)})" for i in range(len(axes_list))]
        elif labels == "vertical":
            raise NotImplementedError("Vertical labels not yet implemented")
        for ax, label in zip(axes_list, labels):
            ax.text(
                0.02,
                0.95,
                label,
                transform=ax.transAxes,
                fontsize=14,
                va="top",
            )

        return self
