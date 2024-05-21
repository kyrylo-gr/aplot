# flake8: noqa: E302, E704
import datetime
from typing import (
    Any,
    Callable,
    List,
    Literal,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import numpy as np
from matplotlib.artist import Artist
from matplotlib.axes import Axes as MplAxes
from matplotlib.axis import XAxis, YAxis
from matplotlib.backend_bases import MouseButton, RendererBase
from matplotlib.backend_tools import Cursors
from matplotlib.collections import Collection
from matplotlib.colors import Colormap, Normalize
from matplotlib.container import BarContainer, Container
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
from matplotlib.patches import Patch
from matplotlib.quiver import Quiver
from matplotlib.scale import ScaleBase
from matplotlib.spines import Spines
from matplotlib.table import Table
from matplotlib.ticker import Formatter
from matplotlib.transforms import Bbox, BboxTransformTo, Transform
from numpy.typing import ArrayLike

from .axes_class import AAxes
from .figure_class import AFigure

# from matplotlib._typing import ArrayLike, Color, Scalar
Color = tuple[float, float, float] | str
Scalar = str | int | float | bool | np.int_ | np.float_ | np.bool_

_Axes = Union[MplAxes, "AAxes"]
_T = TypeVar("_T")
_S = TypeVar("_S")

class AxesList(List[_T]):

    dataLim: Bbox
    viewLim: Bbox
    transAxes: BboxTransformTo
    transData: Transform
    xaxis: XAxis
    yaxis: YAxis
    spines: Spines
    fmt_xdata: None | Formatter = ...
    fmt_ydata: None | Formatter = ...
    cursor_to_use: Cursors = ...

    figure: AFigure = ...  # type: ignore
    fig: AFigure = ...

    def set_title(  # type: ignore
        self: _S,
        label: str,
        fontdict: dict = ...,
        loc: Literal["center", "left", "right"] = ...,
        pad: float = ...,
        *,
        y: float = ...,
        **kwargs,
    ) -> _S: ...
    def legend(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def inset_axes(  # type: ignore
        self: _S,
        bounds: Sequence[float],
        *,
        transform: Transform = ...,
        zorder: float = ...,
        **kwargs,
    ) -> _S: ...
    def indicate_inset(  # type: ignore
        self: _S,
        bounds: Sequence[float],
        inset_ax: _Axes = ...,
        *,
        transform: Transform = ...,
        facecolor: Color = ...,
        edgecolor: Color = ...,
        alpha: float = ...,
        zorder: float = ...,
        **kwargs,
    ) -> _S: ...
    def indicate_inset_zoom(self: _S, inset_ax: _Axes, **kwargs) -> _S: ...  # type: ignore
    def secondary_xaxis(  # type: ignore
        self: _S,
        location: Literal["top", "bottom", "left", "right"] | float,
        *,
        functions=...,
        **kwargs,
    ) -> _S: ...
    def secondary_yaxis(  # type: ignore
        self: _S,
        location: Literal["top", "bottom", "left", "right"] | float,
        *,
        functions=...,
        **kwargs,
    ) -> _S: ...
    def text(self: _S, x: float, y: float, s: str, fontdict: dict = ..., **kwargs) -> _S: ...  # type: ignore
    def annotate(  # type: ignore
        self: _S,
        text: str,
        xy: Sequence[float],
        xytext: Sequence[float] = ...,
        xycoords: str | Artist | Transform | Callable = ...,
        textcoords: str | Artist | Transform | Callable = ...,
        arrowprops: dict = ...,
        annotation_clip: bool | None = ...,
        **kwargs,
    ) -> _S: ...
    def axhline(  # type: ignore
        self: _S, y: float = 0, xmin: float = 0, xmax: float = 1, **kwargs
    ) -> _S: ...
    def axvline(  # type: ignore
        self: _S, x: float = ..., ymin: float = ..., ymax: float = ..., **kwargs
    ) -> _S: ...
    def axline(  # type: ignore
        self: _S,
        xy1: tuple[float, float],
        xy2: tuple[float, float] = ...,
        *,
        slope: float = ...,
        **kwargs,
    ) -> _S: ...
    def axhspan(  # type: ignore
        self: _S, ymin: float, ymax: float, xmin: float = ..., xmax: float = ..., **kwargs
    ) -> _S: ...
    def axvspan(  # type: ignore
        self: _S, xmin: float, xmax: float, ymin: float = 0, ymax: float = 1, **kwargs
    ) -> _S: ...
    def hlines(  # type: ignore
        self: _S,
        y: float | ArrayLike,
        xmin: float | ArrayLike,
        xmax: float | ArrayLike,
        colors: list[Color] = ...,
        linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
        label: str = ...,
        **kwargs,
    ) -> _S: ...
    def vlines(  # type: ignore
        self: _S,
        x: float | ArrayLike,
        ymin: float | ArrayLike,
        ymax: float | ArrayLike,
        colors: list[Color] = ...,
        linestyles: Literal["solid", "dashed", "dashdot", "dotted"] = ...,
        label: str = ...,
        **kwargs,
    ) -> _S: ...
    def eventplot(  # type: ignore
        self: _S,
        positions: ArrayLike | list[ArrayLike],
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        lineoffsets: float | ArrayLike = 1,
        linelengths: float | ArrayLike = 1,
        linewidths: float | ArrayLike = ...,
        colors: Color | list[Color] = ...,
        linestyles: str | tuple | list = ...,
        **kwargs,
    ) -> _S: ...
    def plot(self: _S, *args, scalex=..., scaley=..., data=..., **kwargs) -> _S: ...  # type: ignore
    def plot_date(  # type: ignore
        self: _S,
        x: ArrayLike,
        y: ArrayLike,
        fmt: str = ...,
        tz: datetime.tzinfo = ...,
        xdate: bool = ...,
        ydate: bool = ...,
        **kwargs,
    ) -> _S: ...
    def loglog(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def semilogx(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def semilogy(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def acorr(self: _S, x: ArrayLike, **kwargs) -> _S: ...  # type: ignore
    def xcorr(  # type: ignore
        self: _S,
        x,
        y,
        normed: bool = True,
        detrend: Callable = ...,
        usevlines: bool = True,
        maxlags: int = 10,
        **kwargs,
    ) -> _S: ...
    def step(  # type: ignore
        self: _S,
        x: ArrayLike,
        y: ArrayLike,
        *args,
        where: Literal["pre", "post", "mid"] = ...,
        data=...,
        **kwargs,
    ) -> _S: ...
    def bar(  # type: ignore
        self: _S,
        x: float | ArrayLike,
        height: float | ArrayLike,
        width: float | ArrayLike = ...,
        bottom: float | ArrayLike = ...,
        *,
        align: Literal["center", "edge"] = "center",
        **kwargs,
    ) -> _S: ...
    def barh(  # type: ignore
        self: _S,
        y: float | ArrayLike,
        width: float | ArrayLike,
        height: float | ArrayLike = ...,
        left: float | ArrayLike = ...,
        *,
        align: Literal["center", "edge"] = "center",
        **kwargs,
    ) -> _S: ...
    def bar_label(  # type: ignore
        self: _S,
        container: BarContainer,
        labels: ArrayLike = ...,
        *,
        fmt: str = "%g",
        label_type: Literal["edge", "center"] = "edge",
        padding: float = 0,
        **kwargs,
    ) -> _S: ...
    def broken_barh(  # type: ignore
        self: _S, xranges: Sequence[tuple[float, float]], yrange: tuple[float, float], **kwargs
    ) -> _S: ...
    def stem(  # type: ignore
        self: _S,
        *args,
        linefmt: str = ...,
        markerfmt: str = ...,
        basefmt: str = "C3-",
        bottom: float = 0,
        label: str | None = None,
        use_line_collection: bool = True,
        orientation: str = "verical",
    ) -> _S: ...
    def pie(  # type: ignore
        self: _S,
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
        normalize: bool = True,
    ) -> _S: ...
    def errorbar(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def boxplot(  # type: ignore
        self: _S,
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
    ) -> _S: ...
    def bxp(  # type: ignore
        self: _S,
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
    ) -> _S: ...
    def scatter(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def hexbin(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def arrow(self: _S, x: float, y: float, dx: float, dy: float, **kwargs) -> _S: ...  # type: ignore
    def quiverkey(  # type: ignore
        self: _S, Q: Quiver, X: float, Y: float, U: float, label: str, **kwargs
    ) -> _S: ...
    def quiver(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def barbs(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def fill(self: _S, *args, data=..., **kwargs) -> _S: ...  # type: ignore
    def fill_between(  # type: ignore
        self: _S,
        x,
        y1: Scalar,
        y2: Scalar = ...,
        where: ArrayLike = ...,
        interpolate: bool = ...,
        step: Literal["pre", "post", "mid"] = ...,
        **kwargs,
    ) -> _S: ...
    def fill_betweenx(  # type: ignore
        self: _S,
        y,
        x1: Scalar,
        x2: Scalar = ...,
        where: ArrayLike = ...,
        step: Literal["pre", "post", "mid"] = ...,
        interpolate: bool = ...,
        **kwargs,
    ) -> _S: ...
    def imshow(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def pcolor(  # type: ignore
        self: _S,
        *args,
        shading: Literal["flat", "nearest", "auto"] = ...,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        **kwargs,
    ) -> _S: ...
    def pcolormesh(  # type: ignore
        self: _S,
        *args,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        shading: Literal["flat", "nearest", "gouraud", "auto"] = ...,
        antialiased=...,
        **kwargs,
    ) -> _S: ...
    def pcolorfast(  # type: ignore
        self: _S,
        *args,
        alpha: float | None = None,
        norm: Normalize = ...,
        cmap: str | Colormap = ...,
        vmin: float | None = None,
        vmax: float | None = None,
        **kwargs,
    ) -> _S: ...
    def contour(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def contourf(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def clabel(self: _S, CS, levels: ArrayLike = ..., **kwargs) -> _S: ...  # type: ignore
    @overload
    def hist(
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    @overload
    def hist(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def stairs(  # type: ignore
        self: _S,
        values: ArrayLike,
        edges: ArrayLike = ...,
        *,
        orientation: Literal["vertical", "horizontal"] = "vertical",
        baseline: float | ArrayLike | None = 0,
        fill: bool = False,
        **kwargs,
    ) -> _S: ...
    def hist2d(  # type: ignore
        self: _S,
        x,
        y,
        bins: None | int | ArrayLike = ...,
        range=...,
        density: bool = False,
        weights=...,
        cmin: float | None = None,
        cmax: float | None = None,
        **kwargs,
    ) -> _S: ...
    def psd(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def csd(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def magnitude_spectrum(  # type: ignore
        self: _S,
        x: Sequence,
        Fs: float = ...,
        Fc: int = ...,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        scale: Literal["default", "linear", "dB"] = "linear",
        **kwargs,
    ) -> _S: ...
    def angle_spectrum(  # type: ignore
        self: _S,
        x: Sequence,
        Fs: float = ...,
        Fc: int = 0,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        **kwargs,
    ) -> _S: ...
    def phase_spectrum(  # type: ignore
        self: _S,
        x: Sequence,
        Fs: float = ...,
        Fc: int = 0,
        window: Callable | np.ndarray = ...,
        pad_to: int = ...,
        sides: Literal["default", "onesided", "twosided"] = ...,
        **kwargs,
    ) -> _S: ...
    def cohere(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def specgram(  # type: ignore
        self: _S,
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
        **kwargs,
    ) -> _S: ...
    def spy(  # type: ignore
        self: _S,
        Z,
        precision: float | Literal["present"] = 0,
        marker=...,
        markersize=...,
        aspect: Literal["equal", "auto", None] | float = "equal",
        origin: Literal["upper", "lower"] = ...,
        **kwargs,
    ) -> _S: ...  # type: ignore
    def matshow(self: _S, Z: ArrayLike, **kwargs) -> _S: ...  # type: ignore
    def violinplot(  # type: ignore
        self: _S,
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
    ) -> _S: ...
    def violin(  # type: ignore
        self: _S,
        vpstats: list[dict],
        positions: ArrayLike = ...,
        vert: bool = True,
        widths: ArrayLike | float = 0.5,
        showmeans: bool = False,
        showextrema: bool = True,
        showmedians: bool = False,
    ) -> _S: ...
    def set_figure(self: _S, fig: Figure) -> _S: ...  # type: ignore
    def set_position(  # type: ignore
        self: _S,
        pos: Sequence[float] | Bbox,
        which: Literal["both", "active", "original"] = ...,
    ) -> _S: ...
    def reset_position(self: _S) -> _S: ...  # type: ignore
    def set_axes_locator(self: _S, locator: Callable[[_Axes, RendererBase], Bbox]) -> _S: ...  # type: ignore
    def sharex(self: _S, other: _Axes) -> _S: ...  # type: ignore
    def sharey(self: _S, other: _Axes) -> _S: ...  # type: ignore
    def clear(self: _S) -> _S: ...  # type: ignore
    def cla(self: _S) -> _S: ...  # type: ignore
    def set_facecolor(self: _S, color: Color) -> _S: ...  # type: ignore
    def set_prop_cycle(self: _S, *args, **kwargs) -> _S: ...  # type: ignore
    def set_aspect(  # type: ignore
        self: _S,
        aspect: Literal["auto", "equal"] | float,
        adjustable: None | Literal["box", "datalim"] = ...,
        anchor: None | str | Sequence[float] = ...,
        share: bool = False,
    ) -> _S: ...
    def set_adjustable(  # type: ignore
        self: _S, adjustable: Literal["box", "datalim"], share: bool = False
    ) -> _S: ...
    def set_box_aspect(self: _S, aspect: float | None = ...) -> _S: ...  # type: ignore
    def set_anchor(  # type: ignore
        self: _S,
        anchor: Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        share: bool = False,
    ) -> _S: ...
    def apply_aspect(self: _S, position=...) -> _S: ...  # type: ignore
    def add_artist(self: _S, a: Artist) -> _S: ...  # type: ignore
    def add_child_axes(self: _S, ax: _Axes) -> _S: ...  # type: ignore
    def add_collection(self: _S, collection: Collection, autolim=...) -> _S: ...  # type: ignore
    def add_image(self: _S, image: AxesImage) -> _S: ...  # type: ignore
    def add_line(self: _S, line: Line2D) -> _S: ...  # type: ignore
    def add_patch(self: _S, p: Patch) -> _S: ...  # type: ignore
    def add_table(self: _S, tab: Table) -> _S: ...  # type: ignore
    def add_container(self: _S, container: Container) -> _S: ...  # type: ignore
    def relim(self: _S, visible_only: bool = ...) -> _S: ...  # type: ignore
    def update_datalim(self: _S, xys, updatex: bool = ..., updatey: bool = ...) -> _S: ...  # type: ignore
    def set_autoscale_on(self: _S, b: bool) -> _S: ...  # type: ignore
    def set_xmargin(self: _S, m: float) -> _S: ...  # type: ignore
    def set_ymargin(self: _S, m: float) -> _S: ...  # type: ignore
    def set_rasterization_zorder(self: _S, z: float | None) -> _S: ...  # type: ignore
    def autoscale(  # type: ignore
        self: _S,
        enable: bool | None = ...,
        axis: Literal["both", "x", "y"] = ...,
        tight: bool | None = ...,
    ) -> _S: ...
    def autoscale_view(  # type: ignore
        self: _S, tight: bool | None = ..., scalex: bool = True, scaley: bool = True
    ) -> _S: ...
    def draw(self: _S, renderer) -> _S: ...  # type: ignore
    def draw_artist(self: _S, a: Artist) -> _S: ...  # type: ignore
    def redraw_in_frame(self: _S) -> _S: ...  # type: ignore
    def set_frame_on(self: _S, b: bool) -> _S: ...  # type: ignore
    def set_axisbelow(self: _S, b: bool | Literal["line"]) -> _S: ...  # type: ignore
    def grid(  # type: ignore
        self: _S,
        visible: bool | None = ...,
        which: Literal["major", "minor", "both"] = ...,
        axis: Literal["both", "x", "y"] = ...,
        **kwargs,
    ) -> _S: ...
    def ticklabel_format(  # type: ignore
        self: _S,
        *,
        axis: Literal["x", "y", "both"] = ...,
        style: Literal["sci", "scientific", "plain"] = ...,
        scilimits=...,
        useOffset: bool | float = ...,
        useLocale: bool = ...,
        useMathText: bool = ...,
    ) -> _S: ...
    def locator_params(  # type: ignore
        self: _S, axis: Literal["both", "x", "y"] = ..., tight: bool | None = ..., **kwargs
    ) -> _S: ...
    def tick_params(self: _S, axis: Literal["x", "y", "both"] = ..., **kwargs) -> _S: ...  # type: ignore
    def set_axis_off(self: _S) -> _S: ...  # type: ignore
    def set_axis_on(self: _S) -> _S: ...  # type: ignore
    def set_xlabel(  # type: ignore
        self: _S,
        xlabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["left", "center", "right"] = ...,
        **kwargs,
    ) -> _S: ...
    def invert_xaxis(self: _S) -> _S: ...  # type: ignore
    def set_xbound(self: _S, lower: float | None = ..., upper: float | None = ...) -> _S: ...  # type: ignore
    @overload
    def set_xlim(  # type: ignore
        self: _S,
        left: tuple[float | np.datetime64, float | np.datetime64],
        *,
        emit: bool = ...,
        auto: bool | None = ...,
        xmin: float = ...,
        xmax: float = ...,
    ) -> _S: ...
    @overload
    def set_xlim(  # type: ignore
        self: _S,
        left: float | np.datetime64 = ...,
        right: float | np.datetime64 = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        xmin: float = ...,
        xmax: float = ...,
    ) -> _S: ...
    def set_xscale(self: _S, value: ..., **kwargs) -> _S: ...  # type: ignore
    def set_ylabel(  # type: ignore
        self: _S,
        ylabel: str,
        fontdict=...,
        labelpad: float = ...,
        *,
        loc: Literal["bottom", "center", "top"] = ...,
        **kwargs,
    ) -> _S: ...
    def invert_yaxis(self: _S) -> _S: ...  # type: ignore
    def set_ybound(self: _S, lower: float | None = ..., upper: float | None = ...) -> _S: ...  # type: ignore
    def set_ylim(  # type: ignore
        self: _S,
        bottom: float = ...,
        top: float = ...,
        emit: bool = ...,
        auto: bool | None = ...,
        *,
        ymin: float = ...,
        ymax: float = ...,
    ) -> _S: ...
    def set_yscale(  # type: ignore
        self: _S, value: Literal["linear", "log", "symlog", "logit"] | ScaleBase, **kwargs
    ) -> _S: ...
    def minorticks_on(self: _S) -> _S: ...  # type: ignore
    def minorticks_off(self: _S) -> _S: ...  # type: ignore
    def set_navigate(self: _S, b: bool) -> _S: ...  # type: ignore
    def set_navigate_mode(self: _S, b: str | None) -> _S: ...  # type: ignore
    def start_pan(self: _S, x: float, y: float, button: MouseButton) -> _S: ...  # type: ignore
    def end_pan(self: _S) -> _S: ...  # type: ignore
    def drag_pan(  # type: ignore
        self: _S, button: MouseButton, key: str | None, x: float, y: float
    ) -> _S: ...
    def twinx(self: _S) -> _S: ...  # type: ignore
    def twiny(self: _S) -> _S: ...  # type: ignore
    def set(self: _S, **kwargs) -> _S: ...  # type: ignore
    def fit(self: _S, func: str | Callable, *args, **kwargs) -> _S: ...
    last_result: _T = ...
    fit_result = ...
    res: _T = ...
    def z_parametric(self: _S, z: ArrayLike, **kwargs) -> _S: ...
    def tight_layout(
        self: _S,
        *,
        pad: float = ...,
        h_pad: float = ...,
        w_pad: float = ...,
        rect: Sequence[float] = ...,
    ) -> _S: ...
    def __add__(self: _S, other) -> _S: ...  # type: ignore
    def plot_z_1d(
        self: _S,
        x: ArrayLike,
        z: ArrayLike,
        plot_format: Literal["bode", "real_imag"] = "bode",
        unwrap: bool = False,
        **kwargs,
    ) -> _S: ...
    def plot_z_2d(
        self: _S,
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike,
        plot_format: Literal["bode", "real_imag"] = "bode",
        unwrap: bool = True,
        **kwargs,
    ) -> _S: ...
    def map(self: _S, func: Callable[[AAxes], Any]) -> _S: ...
    def suptitle(self: _S, title: str) -> _S: ...
    def __getitem__(
        self,
        key: Union[int, Tuple[Union[int, slice], ...], slice],
    ) -> _T: ...  # type: ignore
