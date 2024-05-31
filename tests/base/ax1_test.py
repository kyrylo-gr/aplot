import matplotlib.pyplot as plt

import aplot as ap

from ..test_utils import ImageTest, get_data


class BasicFrontTest(ImageTest):
    def test_simple_ax(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y)

        _, ax2 = plt.subplots()
        ax2.plot(x, y)

        self.assertFigEqual(ax1, ax2)

    def test_simple_ax_false(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y)

        _, ax2 = plt.subplots()
        ax2.plot(x, y**2)

        self.assertFigNotEqual(ax1, ax2)

    def test_set(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y).set(xlabel="X", ylabel="Y", title="Title")

        _, ax2 = plt.subplots()
        ax2.plot(x, y)
        ax2.set_xlabel("X")
        ax2.set_ylabel("X")
        ax2.set_title("Title")

        self.assertFigEqual(ax1, ax2)

    def test_set_false(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y).set(xlabel="X", ylabel="Y", title="Title")

        _, ax2 = plt.subplots()
        ax2.plot(x, y)

        self.assertFigNotEqual(ax1, ax2)
