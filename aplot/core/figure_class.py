from copy import copy
from typing import (
    TYPE_CHECKING,
    Any,
    List,
    Literal,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import matplotlib.pyplot as plt
from matplotlib.figure import Figure as MplFigure

if TYPE_CHECKING:
    from matplotlib.projections.polar import PolarAxes as MplPolarAxes
    from mpl_toolkits.mplot3d.axes3d import Axes3D as MplAxes3D

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
        labels: Union[
            Literal["vertical", "horizontal"], List[str], List[int]
        ] = "horizontal",
        *,
        axes: Optional["AxesList"] = None,
        label_position: Union[Tuple[float, float], List[Tuple[float, float]]] = (
            0.02,
            0.95,
        ),
        fontsize: Optional[Union[int, float, List[Union[float, int]]]] = None,
        capitalize: bool = False,
        **kwargs,
    ) -> _F:
        """Label the axes of the figure.

        Args:
            labels (Union[Literal[&quot;vertical&quot;, &quot;horizontal&quot;], List[str]], optional):
                - "vertical": Label the axes vertically first, then horizontally.
                - "horizontal": Label the axes horizontally first, then vertically.
                - List[str]: List of labels to use for each axes.
                - List[int]: Order of axes in which to label.
                    For example, [2, 0, 1] will label the third axes first, then the first, and finally the second.
                Defaults to "horizontal".
            axes (Optional[&quot;AxesList&quot;], optional): _description_. Defaults to None.
            label_position (Union[Tuple[float, float], List[Tuple[float, float]]], optional):
                The (x, y) position of the label. Defaults to (0.02, 0.95).
                If a list of tuples is provided, each tuple will be used for each axes.
            fontsize (Optional[Union[int, float, List[Union[float, int]]]], optional):
                Fontsize of the labels. Defaults to None.
                If a list of font sizes is provided, each font size will be used for each axes.
            capitalize (bool, optional): Capitalize the labels. Defaults to False.
            **kwargs: Additional keyword arguments to pass to the text function.

        Raises:
            NotImplementedError: Raised if labels is set to "vertical"

        Returns:
            _F: Figure itself

        Example:
            ```
                import numpy as np
                import aplot as ap

                x = np.linspace(0, 10, 100)
                y = np.sin(x)
                ax = ap.axs(2, 2, figsize=(10, 8))
                ax.plot(x, y)

                ax.fig.label_axes().show()
            ```
        """
        if axes is None:
            axes = self.axes
        axes_list = axes.flat()
        axes_list = [ax for ax in axes_list if not detect_minor_axes(ax)]
        if isinstance(labels, list):
            if len(labels) != len(axes_list):
                raise ValueError(
                    "Length of labels should be equal to the number of axes"
                )
            if isinstance(labels[0], int):
                labels = [f"({chr(65+((int(i)-1)%len(axes_list)))})" for i in labels]
        elif labels == "horizontal":
            labels = [f"({chr(65+i)})" for i in range(len(axes_list))]
        elif labels == "vertical":
            raise NotImplementedError("Vertical labels not yet implemented")

        if len(label_position) == 2 and isinstance(label_position[0], (int, float)):
            label_position_each = False
        else:
            label_position_each = True
        for i, (ax, label) in enumerate(zip(axes_list, labels)):
            text_kwargs = copy(kwargs)
            x_pos: float = label_position[i][0] if label_position_each else label_position[0]  # type: ignore
            y_pos: float = label_position[i][1] if label_position_each else label_position[1]  # type: ignore
            if fontsize is not None:
                fs = fontsize[i] if isinstance(fontsize, (list, tuple)) else fontsize
                text_kwargs.setdefault("fontsize", fs)
            text_kwargs.setdefault("transform", ax.transAxes)
            text_kwargs.setdefault("va", "top")

            label = str(label).upper() if capitalize else str(label).lower()

            ax.text(
                x_pos,
                y_pos,
                label,
                **text_kwargs,
            )

        return self


def detect_minor_axes(ax: "AAxes") -> bool:
    """Detect if the axes are minor axes.

    Args:
        axes (AxesList[AAxes]): List of axes

    Returns:
        bool: True if the axes are minor axes
    """
    if hasattr(ax, "_colorbar"):
        return True
    return False
