# flake8: noqa: E302, E704
import datetime
from typing import Callable, Generic, Literal, Sequence, TypeVar, Union, overload

import numpy as np
from matplotlib.artist import Artist
from matplotlib.axes import Axes as MplAxes
from matplotlib.axes._secondary_axes import SecondaryAxis
from matplotlib.axis import XAxis, YAxis
from matplotlib.backend_bases import MouseButton, RendererBase
from matplotlib.backend_tools import Cursors
from matplotlib.collections import (
    BrokenBarHCollection,
    Collection,
    EventCollection,
    LineCollection,
    PathCollection,
    PolyCollection,
    QuadMesh,
)
from matplotlib.colors import Colormap, Normalize
from matplotlib.container import (
    BarContainer,
    Container,
    ErrorbarContainer,
    StemContainer,
)
from matplotlib.contour import QuadContourSet
from matplotlib.figure import Figure
from matplotlib.image import AxesImage, PcolorImage
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
from matplotlib.patches import FancyArrow, Patch, Polygon, Rectangle, StepPatch, Wedge
from matplotlib.quiver import Barbs, Quiver
from matplotlib.scale import ScaleBase
from matplotlib.spines import Spines
from matplotlib.table import Table
from matplotlib.text import Annotation, Text
from matplotlib.ticker import Formatter
from matplotlib.transforms import Bbox, BboxTransformTo, Transform
from numpy.typing import ArrayLike

# from matplotlib._typing import ArrayLike, Color, Scalar
Color = tuple[float, float, float] | str
Scalar = str | int | float | bool | np.int_ | np.float_ | np.bool_

_Axes = Union[MplAxes, "AAxes"]
_T = TypeVar("_T")
_S = TypeVar("_S")

class AAxes(MplAxes, Generic[_T]):

    dataLim: Bbox
    viewLim: Bbox
    figure: Figure
    transAxes: BboxTransformTo
    transData: Transform
    xaxis: XAxis
    yaxis: YAxis
    spines: Spines
    fmt_xdata: None | Formatter = ...
    fmt_ydata: None | Formatter = ...
    cursor_to_use: Cursors = ...

    def set_title(  # type: ignore
        self,
        label: str,
        fontdict: dict = ...,
        loc: Literal["center", "left", "right"] = ...,
        pad: float = ...,
        *,
        y: float = ...,
        **kwargs
    ) -> "AAxes": ...
    def legend(self, *args, **kwargs) -> "AAxes": ...  # type: ignore
    def inset_axes(
        self, bounds: Sequence[float], *, transform: Transform = ..., zorder: float = ..., **kwargs
    ) -> "AAxes": ...
    def indicate_inset(  # type: ignore
        self,
        bounds: Sequence[float],
        inset_ax: _Axes = ...,
        *,
        transform: Transform = ...,
        facecolor: Color = ...,
        edgecolor: Color = ...,
        alpha: float = ...,
        zorder: float = ...,
        **kwargs
    ) -> "AAxes": ...
    def indicate_inset_zoom(self, inset_ax: _Axes, **kwargs) -> "AAxes[Rectangle]": ...  # type: ignore
    def secondary_xaxis(  # type: ignore
        self,
        location: Literal["top", "bottom", "left", "right"] | float,
        *,
        functions=...,
        **kwargs
    ) -> "AAxes[SecondaryAxis]": ...
    def secondary_yaxis(  # type: ignore
        self,
        location: Literal["top", "bottom", "left", "right"] | float,
        *,
        functions=...,
        **kwargs
    ) -> "AAxes[SecondaryAxis]": ...
    def text(self, x: float, y: float, s: str, fontdict: dict = ..., **kwargs) -> "AAxes[Text]": ...  # type: ignore
    def annotate(  # type: ignore
        self,
        text: str,
        xy: Sequence[float],
        xytext: Sequence[float] = ...,
        xycoords: str | Artist | Transform | Callable = ...,
        textcoords: str | Artist | Transform | Callable = ...,
        arrowprops: dict = ...,
        annotation_clip: bool | None = ...,
        **kwargs
    ) -> "AAxes[Annotation]": ...
    def axhline(  # type: ignore
        self, y: float = 0, xmin: float = 0, xmax: float = 1, **kwargs
    ) -> "AAxes[Line2D]": ...
    def axvline(  # type: ignore
        self, x: float = ..., ymin: float = ..., ymax: float = ..., **kwargs
    ) -> "AAxes[Line2D]": ...
    def axline(  # type: ignore
        self,
        xy1: tuple[float, float],
        xy2: tuple[float, float] = ...,
        *,
        slope: float = ...,
        **kwargs
    ) -> "AAxes[Line2D]": ...
    def axhspan(  # type: ignore
        self, ymin: float, ymax: float, xmin: float = ..., xmax: float = ..., **kwargs
    ) -> "AAxes[Polygon]": ...
    def axvspan(  # type: ignore
        self, xmin: float, xmax: float, ymin: float = 0, ymax: float = 1, **kwargs
    ) -> "AAxes[Polygon]": ...
    def hlines(  # type: ignore
        self,
        y: float | ArrayLike,
        xmin: float | ArrayLike,
        xmax: float | ArrayLike,
        colors: list[Color] = ...,
        linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
        label: str = ...,
        **kwargs
    ) -> "AAxes[LineCollection]": ...
    def vlines(  # type: ignore
        self,
        x: float | ArrayLike,
        ymin: float | ArrayLike,
        ymax: float | ArrayLike,
        colors: list[Color] = ...,
        linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
        label: str = ...,
        **kwargs
    ) -> "AAxes[LineCollection]": ...
    def eventplot(  # type: ignore
        self,
        positions: ArrayLike | list[ArrayLike],
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        lineoffsets: float | ArrayLike = 1,
        linelengths: float | ArrayLike = 1,
        linewidths: float | ArrayLike = ...,
        colors: Color | list[Color] = ...,
        linestyles: str | tuple | list = ...,
        **kwargs
    ) -> "AAxes[list[EventCollection]]": ...
    def plot(self, *args, scalex=..., scaley=..., data=..., **kwargs) -> "AAxes[list[Line2D]]": ...  # type: ignore
    def plot_date(  # type: ignore
        self,
        x: ArrayLike,
        y: ArrayLike,
        fmt: str = ...,
        tz: datetime.tzinfo = ...,
        xdate: bool = ...,
        ydate: bool = ...,
        **kwargs
    ) -> "AAxes[list[Line2D]]": ...
    def loglog(self, *args, **kwargs) -> "AAxes[list[Line2D]]": ...  # type: ignore
    def semilogx(self, *args, **kwargs) -> "AAxes[list[Line2D]]": ...  # type: ignore
    def semilogy(self, *args, **kwargs) -> "AAxes[list[Line2D]]": ...  # type: ignore
    def acorr(self, x: ArrayLike, **kwargs) -> "AAxes[None]": ...  # type: ignore
    def xcorr(  # type: ignore
        self,
        x,
        y,
        normed: bool = True,
        detrend: Callable = ...,
        usevlines: bool = True,
        maxlags: int = 10,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, bool, int]]": ...
    def step(  # type: ignore
        self,
        x: ArrayLike,
        y: ArrayLike,
        *args,
        where: Literal["pre", "post", "mid"] = ...,
        data=...,
        **kwargs
    ) -> "AAxes[list[Line2D]]": ...
    def bar(  # type: ignore
        self,
        x: float | ArrayLike,
        height: float | ArrayLike,
        width: float | ArrayLike = ...,
        bottom: float | ArrayLike = ...,
        *,
        align: Literal["center", "edge"] = "center",
        **kwargs
    ) -> "AAxes[BarContainer]": ...
    def barh(  # type: ignore
        self,
        y: float | ArrayLike,
        width: float | ArrayLike,
        height: float | ArrayLike = ...,
        left: float | ArrayLike = ...,
        *,
        align: Literal["center", "edge"] = "center",
        **kwargs
    ) -> "AAxes[BarContainer]": ...
    def bar_label(  # type: ignore
        self,
        container: BarContainer,
        labels: ArrayLike = ...,
        *,
        fmt: str = "%g",
        label_type: Literal["edge", "center"] = "edge",
        padding: float = 0,
        **kwargs
    ) -> "AAxes[list[Text]]": ...
    def broken_barh(  # type: ignore
        self, xranges: Sequence[tuple[float, float]], yrange: tuple[float, float], **kwargs
    ) -> "AAxes[BrokenBarHCollection]": ...
    def stem(  # type: ignore
        self,
        *args,
        linefmt: str = ...,
        markerfmt: str = ...,
        basefmt: str = "C3-",
        bottom: float = 0,
        label: str | None = None,
        use_line_collection: bool = True,
        orientation: str = "verical"
    ) -> "AAxes[StemContainer]": ...
    def pie(  # type: ignore
        self,
        x,
        explode: ArrayLike | None = None,
        labels: list | None = None,
        colors: ArrayLike | None = None,
        autopct: None | str | Callable = None,
        pctdistance: float = 0.6,
        shadow: bool = False,
        labeldistance: float | None = 1.1,
        startangle: float = 0,
        radius: float = 1,
        counterclock: bool = True,
        wedgeprops: dict | None = None,
        textprops: dict | None = None,
        center: tuple[float, float] = (0, 0),
        frame: bool = False,
        rotatelabels: bool = False,
        *,
        normalize: bool = True
    ) -> "AAxes[tuple[list[Wedge], list[Text], list[Text]]]": ...
    def errorbar(  # type: ignore
        self,
        x: float | ArrayLike,
        y: float | ArrayLike,
        yerr: float | ArrayLike = ...,
        xerr: float | ArrayLike = ...,
        fmt: str = "",
        ecolor: Color | None = None,
        elinewidth: float | None = None,
        capsize: float = ...,
        barsabove: bool = False,
        lolims: bool = False,
        uplims: bool = False,
        xlolims: bool = False,
        xuplims: bool = False,
        errorevery: int = 1,
        capthick: float | None = None,
        **kwargs
    ) -> "AAxes[ErrorbarContainer]": ...
    def boxplot(  # type: ignore
        self,
        x: ArrayLike,
        notch: bool = False,
        sym: str = ...,
        vert: bool = True,
        whis: float = 1.5,
        positions: ArrayLike = ...,
        widths: float | ArrayLike = ...,
        patch_artist: bool = False,
        bootstrap: int = ...,
        usermedians=...,
        conf_intervals: ArrayLike = ...,
        meanline: bool = False,
        showmeans=...,
        showcaps=...,
        showbox=...,
        showfliers=...,
        boxprops=...,
        labels: Sequence = ...,
        flierprops=...,
        medianprops=...,
        meanprops=...,
        capprops=...,
        whiskerprops=...,
        manage_ticks: bool = True,
        autorange: bool = False,
        zorder: float = 2,
        capwidths=...,
    ) -> "AAxes[dict[str, list[Line2D]]]": ...
    def bxp(  # type: ignore
        self,
        bxpstats: list[dict],
        positions: ArrayLike = ...,
        widths: float | ArrayLike | None = None,
        vert: bool = True,
        patch_artist: bool = False,
        shownotches: bool = False,
        showmeans: bool = False,
        showcaps: bool = True,
        showbox: bool = True,
        showfliers: bool = True,
        boxprops: dict = ...,
        whiskerprops: dict = ...,
        flierprops: dict = ...,
        medianprops: dict = ...,
        capprops: dict = ...,
        meanprops: dict = ...,
        meanline: bool = False,
        manage_ticks: bool = True,
        zorder: float = 2,
        capwidths: float | ArrayLike | None = None,
    ) -> "AAxes[dict[str, list[Line2D]]]": ...
    def scatter(  # type: ignore
        self,
        x: float | ArrayLike,
        y: float | ArrayLike,
        s: float | ArrayLike = ...,
        c: ArrayLike | list[Color] | Color = ...,
        marker: MarkerStyle = ...,
        cmap: str | Colormap = ...,
        norm: Normalize | None = None,
        vmin: float | None = None,
        vmax: float | None = None,
        alpha: float | None = None,
        linewidths: float | ArrayLike = ...,
        *,
        edgecolors: Color = ...,
        plotnonfinite: bool = False,
        **kwargs
    ) -> "AAxes[PathCollection]": ...
    def hexbin(  # type: ignore
        self,
        x: ArrayLike,
        y: ArrayLike,
        C: ArrayLike = ...,
        gridsize: int = 100,
        bins: Literal["log"] | int | Sequence | None = None,
        xscale: Literal["linear", "log"] = "linear",
        yscale: Literal["linear", "log"] = "linear",
        extent: Sequence[float] | None = None,
        cmap=...,
        norm=...,
        vmin=...,
        vmax=...,
        alpha=...,
        linewidths=...,
        edgecolors=...,
        reduce_C_function=...,
        mincnt: int | None = None,
        marginals: bool = False,
        **kwargs
    ) -> "AAxes[PolyCollection]": ...
    def arrow(self, x: float, y: float, dx: float, dy: float, **kwargs) -> "AAxes[FancyArrow]": ...  # type: ignore
    def quiverkey(  # type: ignore
        self, Q: Quiver, X: float, Y: float, U: float, label: str, **kwargs
    ) -> "AAxes[None]": ...
    def quiver(self, *args, **kwargs) -> "AAxes[Quiver]": ...  # type: ignore
    def barbs(self, *args, **kwargs) -> "AAxes[Barbs]": ...  # type: ignore
    def fill(self, *args, data=..., **kwargs) -> "AAxes[list[Polygon]]": ...  # type: ignore
    def fill_between(  # type: ignore
        self,
        x,
        y1: Scalar,
        y2: Scalar = ...,
        where: ArrayLike = ...,
        interpolate: bool = ...,
        step: Literal["pre", "post", "mid"] = ...,
        **kwargs
    ) -> "AAxes[PolyCollection]": ...
    def fill_betweenx(  # type: ignore
        self,
        y,
        x1: Scalar,
        x2: Scalar = ...,
        where: ArrayLike = ...,
        step: Literal["pre", "post", "mid"] = ...,
        interpolate: bool = ...,
        **kwargs
    ) -> "AAxes[PolyCollection]": ...
    def imshow(  # type: ignore
        self,
        X: ArrayLike,
        cmap: str | Colormap = ...,
        norm: Normalize = ...,
        aspect: Literal["equal", "auto"] | float = ...,
        interpolation: str = ...,
        alpha: float | ArrayLike = ...,
        vmin: float = ...,
        vmax: float = ...,
        origin: Literal["upper", "lower"] = ...,
        extent: Sequence[float] = ...,
        *,
        interpolation_stage: Literal["data", "rgba"] = ...,
        filternorm: bool = True,
        filterrad: float = 4,
        resample: bool = ...,
        url: str = ...,
        **kwargs
    ) -> "AAxes[AxesImage]": ...
    def pcolor(  # type: ignore
        self,
        *args,
        shading: Literal["flat", "nearest", "auto"] = ...,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        **kwargs
    ) -> "AAxes[Collection]": ...
    def pcolormesh(  # type: ignore
        self,
        *args,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        shading: Literal["flat", "nearest", "gouraud", "auto"] = ...,
        antialiased=...,
        **kwargs
    ) -> "AAxes[QuadMesh]": ...
    def pcolorfast(  # type: ignore
        self,
        *args,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        **kwargs
    ) -> "AAxes[tuple[AxesImage, PcolorImage, QuadMesh]]": ...
    def contour(self, *args, **kwargs) -> "AAxes[QuadContourSet]": ...  # type: ignore
    def contourf(self, *args, **kwargs) -> "AAxes[QuadContourSet]": ...  # type: ignore
    def clabel(self, CS, levels: ArrayLike = ..., **kwargs) -> "AAxes[None]": ...  # type: ignore
    @overload
    def hist(
        self,
        x: Sequence[ArrayLike],
        bins: int | ArrayLike | str = ...,
        range: tuple | None = ...,
        density: bool = ...,
        weights: None = ...,
        cumulative: bool | Literal[-1] = ...,
        bottom=...,
        histtype: Literal["bar", "barstacked", "step", "stepfilled"] = ...,
        align: Literal["left", "mid", "right"] = ...,
        orientation: Literal["vertical", "horizontal"] = ...,
        rwidth: float | None = ...,
        log: bool = ...,
        color: Color | None = ...,
        label: str | None = ...,
        stacked: bool = ...,
        **kwargs
    ) -> "AAxes[tuple[list[list[float]], list[float], BarContainer | list]]": ...
    @overload
    def hist(  # type: ignore
        self,
        x: ArrayLike,
        bins: int | ArrayLike | str = ...,
        range: tuple[float, float] | None = None,
        density: bool = False,
        weights: ArrayLike | None = None,
        cumulative: bool | Literal[-1] = False,
        bottom: ArrayLike | Scalar | None = None,
        histtype: Literal["bar", "barstacked", "step", "stepfilled"] = "bar",
        align: Literal["left", "mid", "right"] = "mid",
        orientation: Literal["vertical", "horizontal"] = "vertical",
        rwidth: float | None = None,
        log: bool = False,
        color: Color | None = None,
        label: str | None = None,
        stacked: bool = False,
        **kwargs
    ) -> "AAxes[tuple[list[float], list[float], BarContainer | list]]": ...
    def stairs(  # type: ignore
        self,
        values: ArrayLike,
        edges: ArrayLike = ...,
        *,
        orientation: Literal["vertical", "horizontal"] = "vertical",
        baseline: float | ArrayLike | None = 0,
        fill: bool = False,
        **kwargs
    ) -> "AAxes[StepPatch]": ...
    def hist2d(  # type: ignore
        self,
        x,
        y,
        bins: None | int | ArrayLike = ...,
        range=...,
        density: bool = False,
        weights=...,
        cmin: float | None = None,
        cmax: float | None = None,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, np.ndarray, tuple[float, float] | None]]": ...
    def psd(  # type: ignore
        self,
        x: Sequence,
        NFFT: int = ...,
        Fs: float = ...,
        Fc: int = 0,
        detrend: Literal["none", "mean", "linear"] | Callable = ...,
        window: Callable | np.ndarray = ...,
        noverlap: int = 0,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: bool = ...,
        return_line: bool = False,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, Line2D]]": ...
    def csd(  # type: ignore
        self,
        x: ArrayLike,
        y: ArrayLike,
        NFFT: int = ...,
        Fs: float = ...,
        Fc: int = 0,
        detrend: Literal["none", "mean", "linear"] | Callable = ...,
        window: Callable | np.ndarray = ...,
        noverlap: int = 0,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: bool = ...,
        return_line: bool = False,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, Line2D]]": ...
    def magnitude_spectrum(  # type: ignore
        self,
        x: Sequence,
        Fs: float = ...,
        Fc: int = ...,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale: Literal["default", "linear", "dB"] = "linear",
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, Line2D]]": ...
    def angle_spectrum(  # type: ignore
        self,
        x: Sequence,
        Fs: float = ...,
        Fc: int = 0,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, Line2D]]": ...
    def phase_spectrum(  # type: ignore
        self,
        x: Sequence,
        Fs: float = ...,
        Fc: int = 0,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, Line2D]]": ...
    def cohere(  # type: ignore
        self,
        x,
        y,
        NFFT: int = ...,
        Fs: float = ...,
        Fc: int = 0,
        detrend: Literal["none", "mean", "linear"] | Callable = ...,
        window: Callable | np.ndarray = ...,
        noverlap: int = 0,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: bool = ...,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray]]": ...
    def specgram(  # type: ignore
        self,
        x: Sequence,
        NFFT: int = ...,
        Fs: float = ...,
        Fc: int = 0,
        detrend: Literal["none", "mean", "linear"] | Callable = ...,
        window: Callable | np.ndarray = ...,
        noverlap: int = 128,
        cmap: Colormap = ...,
        xextent=...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale_by_freq: bool = ...,
        mode: Literal["default", "psd", "magnitude", "angle", "phase"] = "psd",
        scale: Literal["default", "linear", "dB"] = "dB",
        vmin=...,
        vmax=...,
        **kwargs
    ) -> "AAxes[tuple[np.ndarray, np.ndarray, np.ndarray, AxesImage]]": ...
    def spy(  # type: ignore
        self,
        Z,
        precision: float | Literal["present"] = 0,
        marker=...,
        markersize=...,
        aspect: Literal["equal", "auto", None] | float = "equal",
        origin: Literal["upper", "lower"] = ...,
        **kwargs
    ) -> "AAxes[AxesImage | Line2D]": ...  # type: ignore
    def matshow(self, Z: ArrayLike, **kwargs) -> "AAxes[AxesImage]": ...  # type: ignore
    def violinplot(  # type: ignore
        self,
        dataset: ArrayLike,
        positions: ArrayLike = ...,
        vert: bool = True,
        widths: ArrayLike | float = 0.5,
        showmeans: bool = False,
        showextrema: bool = True,
        showmedians: bool = False,
        quantiles: ArrayLike | None = None,
        points: int = 100,
        bw_method: str | Scalar | Callable | None = None,
    ) -> "AAxes[dict[str, Collection]]": ...
    def violin(  # type: ignore
        self,
        vpstats: list[dict],
        positions: ArrayLike = ...,
        vert: bool = True,
        widths: ArrayLike | float = 0.5,
        showmeans: bool = False,
        showextrema: bool = True,
        showmedians: bool = False,
    ) -> "AAxes[dict[str, Collection]]": ...
    def set_figure(self, fig: Figure) -> "AAxes[None]": ...  # type: ignore
    def set_position(  # type: ignore
        self,
        pos: Sequence[float] | Bbox,
        which: Literal["both", "active", "original"] = ...,
    ) -> "AAxes[None]": ...
    def reset_position(self) -> "AAxes[None]": ...  # type: ignore
    def set_axes_locator(self, locator: Callable[[_Axes, RendererBase], Bbox]) -> "AAxes[None]": ...  # type: ignore
    def sharex(self, other: _Axes) -> "AAxes[None]": ...  # type: ignore
    def sharey(self, other: _Axes) -> "AAxes[None]": ...  # type: ignore
    def clear(self) -> "AAxes[None]": ...  # type: ignore
    def cla(self) -> "AAxes[None]": ...  # type: ignore
    def set_facecolor(self, color: Color) -> "AAxes[None]": ...  # type: ignore
    def set_prop_cycle(self, *args, **kwargs) -> "AAxes[None]": ...  # type: ignore
    def set_aspect(  # type: ignore
        self,
        aspect: Literal["auto", "equal"] | float,
        adjustable: None | Literal["box", "datalim"] = ...,
        anchor: None | str | Sequence[float] = ...,
        share: bool = False,
    ) -> "AAxes[None]": ...
    def set_adjustable(  # type: ignore
        self, adjustable: Literal["box", "datalim"], share: bool = False
    ) -> "AAxes[None]": ...
    def set_box_aspect(self, aspect: float | None = ...) -> "AAxes[None]": ...  # type: ignore
    def set_anchor(  # type: ignore
        self,
        anchor: Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        share: bool = False,
    ) -> "AAxes[None]": ...
    def apply_aspect(self, position=...) -> "AAxes[None]": ...  # type: ignore
    def add_artist(self, a: Artist) -> "AAxes[Artist]": ...  # type: ignore
    def add_child_axes(self, ax: _Axes) -> "AAxes[AAxes]": ...  # type: ignore
    def add_collection(self, collection: Collection, autolim=...) -> "AAxes[Collection]": ...  # type: ignore
    def add_image(self, image: AxesImage) -> "AAxes[AxesImage]": ...  # type: ignore
    def add_line(self, line: Line2D) -> "AAxes[Line2D]": ...  # type: ignore
    def add_patch(self, p: Patch) -> "AAxes[Patch]": ...  # type: ignore
    def add_table(self, tab: Table) -> "AAxes[Table]": ...  # type: ignore
    def add_container(self, container: Container) -> "AAxes[Container]": ...  # type: ignore
    def relim(self, visible_only: bool = ...) -> "AAxes[None]": ...  # type: ignore
    def update_datalim(self, xys, updatex: bool = ..., updatey: bool = ...) -> "AAxes[None]": ...  # type: ignore
    def set_autoscale_on(self, b: bool) -> "AAxes[None]": ...  # type: ignore
    def set_xmargin(self, m: float) -> "AAxes[None]": ...  # type: ignore
    def set_ymargin(self, m: float) -> "AAxes[None]": ...  # type: ignore
    def set_rasterization_zorder(self, z: float | None) -> "AAxes[None]": ...  # type: ignore
    def autoscale(  # type: ignore
        self,
        enable: bool | None = ...,
        axis: Literal["both", "x", "y"] = ...,
        tight: bool | None = ...,
    ) -> "AAxes[None]": ...
    def autoscale_view(  # type: ignore
        self, tight: bool | None = ..., scalex: bool = True, scaley: bool = True
    ) -> "AAxes[None]": ...
    def draw(self, renderer) -> "AAxes[None]": ...  # type: ignore
    def draw_artist(self, a: Artist) -> "AAxes[None]": ...  # type: ignore
    def redraw_in_frame(self) -> "AAxes[None]": ...  # type: ignore
    def set_frame_on(self, b: bool) -> "AAxes[None]": ...  # type: ignore
    def set_axisbelow(self, b: bool | Literal["line"]) -> "AAxes[None]": ...  # type: ignore
    def grid(  # type: ignore
        self,
        visible: bool | None = ...,
        which: Literal["major", "minor", "both"] = ...,
        axis: Literal["both", "x", "y"] = ...,
        **kwargs
    ) -> "AAxes[None]": ...
    def ticklabel_format(  # type: ignore
        self,
        *,
        axis: Literal["x", "y", "both"] = ...,
        style: Literal["sci", "scientific", "plain"] = ...,
        scilimits=...,
        useOffset: bool | float = ...,
        useLocale: bool = ...,
        useMathText: bool = ...
    ) -> "AAxes[None]": ...
    def locator_params(  # type: ignore
        self, axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
    ) -> "AAxes[None]": ...
    def tick_params(self, axis: Literal["x", "y", "both"] = ..., **kwargs) -> "AAxes[None]": ...  # type: ignore
    def set_axis_off(self) -> "AAxes[None]": ...  # type: ignore
    def set_axis_on(self) -> "AAxes[None]": ...  # type: ignore
    def set_xlabel(  # type: ignore
        self,
        xlabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["left", "center", "right"] = ...,
        **kwargs
    ) -> "AAxes[None]": ...
    def invert_xaxis(self) -> "AAxes[None]": ...  # type: ignore
    def set_xbound(self, lower: float | None = ..., upper: float | None = ...) -> "AAxes[None]": ...  # type: ignore
    @overload
    def set_xlim(  # type: ignore
        self,
        left: tuple[float | np.datetime64, float | np.datetime64],
        *,
        emit: bool = ...,
        auto: bool | None = ...,
        xmin: float = ...,
        xmax: float = ...
    ) -> "AAxes[tuple[float, float]]": ...
    @overload
    def set_xlim(  # type: ignore
        self,
        left: float | np.datetime64 = ...,
        right: float | np.datetime64 = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        xmin: float = ...,
        xmax: float = ...
    ) -> "AAxes[tuple[float, float]]": ...
    def set_xscale(self, value: ..., **kwargs) -> "AAxes[None]": ...  # type: ignore
    def set_ylabel(  # type: ignore
        self,
        ylabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["bottom", "center", "top"] = ...,
        **kwargs
    ) -> "AAxes[None]": ...
    def invert_yaxis(self) -> "AAxes[None]": ...  # type: ignore
    def set_ybound(self, lower: float | None = ..., upper: float | None = ...) -> "AAxes[None]": ...  # type: ignore
    def set_ylim(  # type: ignore
        self,
        bottom: float = ...,
        top: float = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        ymin: float = ...,
        ymax: float = ...
    ) -> "AAxes[None]": ...
    def set_yscale(  # type: ignore
        self, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    ) -> "AAxes[None]": ...
    def minorticks_on(self) -> "AAxes[None]": ...  # type: ignore
    def minorticks_off(self) -> "AAxes[None]": ...  # type: ignore
    def set_navigate(self, b: bool) -> "AAxes[None]": ...  # type: ignore
    def set_navigate_mode(self, b: str | None) -> "AAxes[None]": ...  # type: ignore
    def start_pan(self, x: float, y: float, button: MouseButton) -> "AAxes[None]": ...  # type: ignore
    def end_pan(self) -> "AAxes[None]": ...  # type: ignore
    def drag_pan(  # type: ignore
        self, button: MouseButton, key: str | None, x: float, y: float
    ) -> "AAxes[None]": ...
    def twinx(self) -> "AAxes[AAxes]": ...
    def twiny(self) -> "AAxes[AAxes]": ...
    def set(self: _S, **kwargs) -> _S: ...  # type: ignore
    def fit(self: _S, func: str | Callable, *args, **kwargs) -> _S: ...
    last_result: _T = ...
    fit_result = ...
    res: _T = ...
    def z_parametric(self, z: ArrayLike, **kwargs) -> "AAxes[Line2D]": ...
    def autoaxis(self, level: int = 0, func_name: str = ...): ...
    def tight_layout(
        self,
        *,
        pad: float = ...,
        h_pad: float = ...,
        w_pad: float = ...,
        rect: Sequence[float] = ...
    ): ...
