import typing as _t

import numpy as np


class NoneType:
    pass


noneType = NoneType()

ArrayLike = _t.Union[np.ndarray, _t.List]
