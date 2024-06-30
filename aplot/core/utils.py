import typing as _t

from .typing import NoneType

if _t.TYPE_CHECKING:
    from .axes_class import AAxes
    from .typing import ArrayLike


_T = _t.TypeVar("_T")


def res(ax_or_any: _t.Union[_T, "AAxes[_T]"], /) -> _T:
    if hasattr(ax_or_any, "res"):
        return ax_or_any.res  # type: ignore
    return ax_or_any  # type: ignore


def filter_set_kwargs(obj, additional_: _t.Optional[_t.List[str]] = None, **kwargs):
    """Filter kwargs to one that can be set with set_... method."""
    for k in list(kwargs.keys()):
        if additional_ and k in additional_:
            continue
        func = getattr(obj, f"set_{k}", None)
        if not callable(func):
            kwargs.pop(k)
    return kwargs


def filter_none_types(kwargs: dict) -> dict:
    return {k: v for k, v in kwargs.items() if not isinstance(v, NoneType)}


def filter_none(data: _t.Optional[dict] = None, **kwargs) -> dict:
    if data is not None:
        kwargs.update(data)
    return {k: v for k, v in kwargs.items() if v is not None}


def imshow_kwds(
    x: _t.Optional["ArrayLike"] = None,
    y: _t.Optional["ArrayLike"] = None,
):
    """Return a dictionary of kwds that can be used to make
    imshow(z, **imshow_kwds(xarray, yarray)) look the same as pcolor(xarray, yarray, z)
    imshow will be way faster than pcolor, however, it will give the correct result only
    if xarray and yarray are regularly spaced arrays."""
    extent = [x[0], x[-1], y[0], y[-1]] if x is not None and y is not None else None
    return dict(aspect="auto", origin="lower", interpolation="None", extent=extent)


def get_auto_args(level: int = 0, name="plot"):
    import inspect
    import re

    stack = inspect.stack()
    if len(stack) < 3 + level:
        return []
    caller_frame = stack[2 + level]
    frame, filename, line_number, function_name, lines, index = caller_frame
    # print(function_name.capitalize(), lines)
    if lines:  # Lines is a list of lines of context from the source code
        # Use the first line of context, which should be the call
        line = " ".join(lines).strip()
        # print(line)
        # line = lines[0].strip()
        # Use regex to find variable names within the function call
        pattern = rf"{name}\(([^)]+)\)"
        match = re.search(pattern, line)
        if match:
            # Extract the argument part and split by commas to get variable names
            arguments = match.group(1).split(",")
            # Use strip to clean any spaces and capture only the variable names
            var_names = [var_to_label(arg.split("=")[-1]) for arg in arguments]
            return var_names
    return []


def var_to_label(var: str) -> str:
    var = var.strip().replace("__", ", ").replace("_", " ")
    if not var:
        return var
    if len(var) > 1:
        var = var[0].title() + var[1:]
    return var


def pop_from_dict(data, keys: _t.Union[str, _t.Tuple[str, ...]]):
    if isinstance(keys, str):
        keys = (keys,)
    if not isinstance(keys, tuple):
        keys = tuple(keys)
    main = data.copy()
    for key in keys:
        if key in main:
            main.pop(key)
    return main
