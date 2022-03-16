import contextlib
import inspect
import threading
import warnings
from typing import (
    Callable,
    ContextManager,
    Final,
    overload,
    Type,
    TypeVar,
    Union,
)


_T = TypeVar('_T', bound=Union[Callable, Type])

_lock: Final[threading.Lock] = threading.Lock()


@overload
def export(obj: str, *, threadsafe: bool = ...) -> Callable[[_T], _T]: ...
@overload
def export(obj: _T, *, threadsafe: bool = ...) -> _T: ...


def export(
    obj: Union[_T, str],
    *,
    threadsafe: bool = False
) -> Union[_T, Callable[[_T], _T]]:
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

    """
    module = inspect.getmodule(inspect.stack()[1][0])
    if module is None:
        raise ModuleNotFoundError(f'could not find module of {obj!r}')

    if isinstance(obj, str):
        name = obj
        res = lambda _obj: _obj
    else:
        res = obj
        name = obj.__name__

    lock: ContextManager
    if threadsafe:
        lock = _lock
    else:
        lock = contextlib.nullcontext()

    with lock:
        if hasattr(module, '__all__'):
            if not isinstance(module.__all__, list):
                setattr(module, '__all__', list(module.__all__))
            exports = module.__all__[:]
        else:
            setattr(module, '__all__', [])
            exports = []

        if name in exports:
            warnings.warn(f'{name!r} already exported')

        else:
            exports.append(name)
            getattr(module, '__all__')[:] = exports

    return res


# you can't decorate yourself; it's a chicken/egg situation
export(export)


@overload
def export_threadsafe(obj: str) -> Callable[[_T], _T]: ...
@overload
def export_threadsafe(obj: _T) -> _T: ...


@export
def export_threadsafe(obj: Union[_T, str]) -> Union[_T, Callable[[_T], _T]]:
    """Thread-safe version of export().

    Uses threading.Lock when modifying __all__.

    This negatively impacts performance: Don't use if not needed!
    """
    return export(obj, threadsafe=True)
