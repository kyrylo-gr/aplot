from matplotlib.figure import Figure as MplFigure

from .axes_class import AAxes


class AFigure(MplFigure):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Custom method example
    def custom_draw_method(self):
        print("Custom drawing behavior here")

    def add_subplot(self, *args, **kwargs):
        # Ensuring that the custom axes class is used
        kwargs.update({"axes_class": AAxes})
        return super().add_subplot(*args, **kwargs)
