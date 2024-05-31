import os
import shutil
import unittest

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .compare_images import images_are_similar

TEST_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TEST_DIR, "tmp_test_data")

COLORS = ["#0066cc", "#ffcc00", "#ff7400", "#962fbf"]


class ImageTest(unittest.TestCase):
    data_dir = DATA_DIR
    file_prefix = ""

    def setUp(self):
        # if not os.path.exists(DATA_DIR):
        # shutil.rmtree(DATA_DIR)
        os.makedirs(DATA_DIR, exist_ok=True)
        self.file_prefix = self.__class__.__name__

    def assertFigEqual(self, fig_or_ax_1: "Figure | Axes", fig_or_ax_2: "Figure| Axes"):

        fig1: "Figure" = fig_or_ax_1.figure if hasattr(fig_or_ax_1, "figure") else fig_or_ax_1  # type: ignore
        fig2: "Figure" = fig_or_ax_2.figure if hasattr(fig_or_ax_2, "figure") else fig_or_ax_2  # type: ignore

        self._assertFigEqual(fig1, fig2, True)

    def assertFigNotEqual(self, fig_or_ax_1: "Figure | Axes", fig_or_ax_2: "Figure| Axes"):
        fig1: "Figure" = fig_or_ax_1.figure if hasattr(fig_or_ax_1, "figure") else fig_or_ax_1  # type: ignore
        fig2: "Figure" = fig_or_ax_2.figure if hasattr(fig_or_ax_2, "figure") else fig_or_ax_2  # type: ignore

        self._assertFigEqual(fig1, fig2, False)

    def _assertFigEqual(
        self,
        fig1: "Figure",
        fig2: "Figure",
        assert_to_equal: bool,
    ):
        path1 = os.path.join(self.data_dir, f"{self.file_prefix}_{self._testMethodName}_fig1.png")
        path2 = os.path.join(self.data_dir, f"{self.file_prefix}_{self._testMethodName}_fig2.png")
        fig1.savefig(path1)
        fig2.savefig(path2)

        return self.assertImageEqual(path1, path2, assert_to_equal)

    def assertImageEqual(self, path1: str, path2: str, assert_to: bool):
        if assert_to:
            self.assertTrue(images_are_similar(path1, path2))
        else:
            self.assertFalse(images_are_similar(path1, path2))

    def run(self, result=None):
        """Don't run tearDown when testMethod failed.

        The only difference between this and the original run method is that
        it will not run tearDown if there is an error in the test method.
        It allows to debug by keeping the images that failed the test.
        """
        testMethod = getattr(self, self._testMethodName)

        self.setUp()
        testMethod()
        # it will not run tearDown if there is an error in the test method.
        self.tearDown()

    def tearDown(self):
        path1 = os.path.join(self.data_dir, f"{self.file_prefix}_{self._testMethodName}_fig1.png")
        path2 = os.path.join(self.data_dir, f"{self.file_prefix}_{self._testMethodName}_fig2.png")
        if os.path.exists(path1):
            os.remove(path1)
        if os.path.exists(path2):
            os.remove(path2)

    @classmethod
    def tearDownClass(cls):
        """Remove the folder if it is empty."""
        if os.path.exists(cls.data_dir) and not os.listdir(cls.data_dir):
            shutil.rmtree(cls.data_dir)

    @classmethod
    def run_all_tests(cls):
        suite = unittest.TestLoader().loadTestsFromTestCase(cls)
        unittest.TextTestRunner().run(suite)
