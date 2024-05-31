import matplotlib.pyplot as plt

import aplot as ap

from ..test_utils import ImageTest, get_data


class BasicFrontTest(ImageTest):
    # def test_simple_ax(self):
    #     # TODO: Implement ax test
    #     x, y = get_data()
    #     ax1 = ap.ax().plot(x, y)

    #     _, ax2 = plt.subplots()
    #     ax2.plot(x, y)

    #     self.assertFigEqual(ax1, ax2)
    #     plt.close()

    def test_simple_axs(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y)

        _, ax2 = plt.subplots()
        ax2.plot(x, y)

        self.assertFigEqual(ax1, ax2)

    def test_col_axs(self):
        x, y = get_data()
        ax1 = ap.axs(2, 1).plot(x, y)

        fig2, ax2 = plt.subplots(2, 1)
        ax2[0].plot(x, y)
        ax2[1].plot(x, y)

        self.assertFigEqual(ax1.figure, fig2)

    def test_row_axs(self):
        x, y = get_data()
        ax1 = ap.axs(1, 2).plot(x, y)

        fig2, ax2 = plt.subplots(1, 2)
        ax2[0].plot(x, y)
        ax2[1].plot(x, y)

        self.assertFigEqual(ax1.figure, fig2)

    def test_plot(self):
        x, y = get_data()
        ax1 = ap.axs().plot(x, y)

        _, ax2 = plt.subplots()
        ax2.plot(x, y)

        self.assertFigEqual(ax1, ax2)
        ap.close()
