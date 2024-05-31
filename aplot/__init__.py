# flake8: noqa: F401

from . import analysis, styles
from .__config__ import __version__
from .core import ax, axs, figure, figure_class, subplot, subplots
from .core.axes_class import AAxes as Axes
from .core.figure_class import AFigure as Figure

s = styles

# from .plots import *
