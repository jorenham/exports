from __future__ import annotations

import contextlib
import inspect
import threading
import warnings
from typing import Callable, Final, TypeVar, cast, overload


_T = TypeVar('_T', bound='Callable[..., object] | type | object')
_V = TypeVar('_V')

_lock: Final[threading.Lock] = threading.Lock()


def _identity(_obj: _V, /) -> _V:
    return _obj


@overload
def export(obj: str, /, *, threadsafe: bool = ...) -> Callable[[_T], _T]: ...
@overload
def export(obj: _T, /, *, threadsafe: bool = ...) -> _T: ...
def export(obj: _T | str, /, *, threadsafe: bool = False) -> Callable[[_T], _T] | _T:
    """Add a function, class or name to __all__.

    If the module has no __all__, it is created. Otherwise, the export is
    appended.

    Can be used as function decorator:

    >>> @export
    ... def spam():
    ...     ...

    as class decorator:

    >>> @export
    ... class Ham:
    ...     ...

    or by using the name directly:

    >>> from functools import reduce as fold
    >>> export('fold')

    Caveats:
        Exporting a function or class directly relies on the __name__ attribute,
        so consider the following example:

        >>> def eggs():
        ...     ...
        >>> fake_eggs = eggs

        If we want to export fake_eggs, then this **will not work**:

        >>> export(fake_eggs)  # BAD: this will add 'eggs' to __all__

        In such cases, use the name instead:

        >>> export('fake_eggs')  # GOOD

        You'll be safe if you either

        - decorate a function or a class directly with `@export`,
        - pass the name string when using plain `export('...')` calls.

    Raises:
        ModuleNotFoundError: if the module could not be found

    """
    module = inspect.getmodule(inspect.stack()[1][0])
    if module is None:
        raise ModuleNotFoundError(f'could not find module of {obj!r}')

    res: Callable[[_T], _T] | _T
    if isinstance(obj, str):
        name = obj
        res = _identity
    else:
        res = obj
        name = cast(str, getattr(obj, '__name__', None) or str(obj))

    with _lock if threadsafe else contextlib.nullcontext():
        exports: list[str] = list(getattr(module, '__all__', []))
        if name in exports:
            warnings.warn(f'{name!r} already exported', stacklevel=2)
        else:
            exports.append(name)
        module.__all__ = exports  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

    return res


# effectively self-decoration
export(export)
