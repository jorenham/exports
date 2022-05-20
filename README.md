# Explicit module exports

`@export` - The DRY alternative to `__all__`

-----

[![PyPI version shields.io](https://img.shields.io/pypi/v/python-exports.svg)](https://pypi.python.org/pypi/python-exports/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/python-exports.svg)](https://pypi.python.org/pypi/python-exports/)
[![PyPI license](https://img.shields.io/pypi/l/python-exports.svg)](https://pypi.python.org/pypi/python-exports/)

-----

## Installation

`pip install python-exports`


## Usage

```pycon
>>> from exports import export
```

Now you can use it to add to `__all__` as

- function decorator

    ```pycon
    >>> @export
    ... def spam():
    ...     ...
    ```

- class decorator:

    ```pycon
    >>> @export
    ... class Ham:
    ...     ...
    ```

- by name:

    ```pycon
    >>> from functools import reduce as fold
    >>> export('fold')
    ```

## Behaviour

If the module has no __all__, it is created. 
Otherwise, `__all__` is converted to a list, and the export is appended.

## Caveats

Exporting a function or class directly relies on the __name__ attribute,
so consider the following example:

```pycon
>>> def eggs():
...     ...
>>> fake_eggs = eggs
```

If we want to export fake_eggs, then this **will not work**:

```pycon
>>> export(fake_eggs)  # BAD: this will add 'eggs' to __all__
```

In such cases, use the name instead:

```pycon
>>> export('fake_eggs')  # GOOD
```

You'll be safe if you either

- decorate a function or a class directly with `@export`,
- pass the name string when using plain `export('...')` calls.
