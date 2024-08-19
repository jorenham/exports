<h1 align="center">python-exports</h1>

<p align="center">
    The DRY alternative to </code>__all__</code>
</p>

<p align="center">
    <a href="https://pypi.org/project/python-exports/">
        <img
            alt="exports - PyPI"
            src="https://img.shields.io/pypi/v/python-exports?style=flat"
        />
    </a>
    <a href="https://github.com/jorenham/exports">
        <img
            alt="exports - Python Versions"
            src="https://img.shields.io/pypi/pyversions/python-exports?style=flat"
        />
    </a>
    <a href="https://github.com/jorenham/exports">
        <img
            alt="exports - license"
            src="https://img.shields.io/github/license/jorenham/exports?style=flat"
        />
    </a>
</p>
<p align="center">
    <a href="https://github.com/jorenham/exports/actions?query=workflow%3ACI">
        <img
            alt="exports - CI"
            src="https://github.com/jorenham/exports/workflows/CI/badge.svg"
        />
    </a>
    <a href="https://github.com/pre-commit/pre-commit">
        <img
            alt="exports - pre-commit"
            src="https://img.shields.io/badge/pre--commit-enabled-orange?logo=pre-commit"
        />
    </a>
    <a href="https://github.com/KotlinIsland/basedmypy">
        <img
            alt="exports - basedmypy"
            src="https://img.shields.io/badge/basedmypy-checked-fd9002"
        />
    </a>
    <a href="https://detachhead.github.io/basedpyright">
        <img
            alt="exports - basedpyright"
            src="https://img.shields.io/badge/basedpyright-checked-42b983"
        />
    </a>
    <a href="https://github.com/astral-sh/ruff">
        <img
            alt="exports - ruff"
            src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"
        />
    </a>
</p>

-----

## Installation

To install the `exports` package, you can use
[`python-exports` on PyPI](https://pypi.org/project/python-exports/):

```bash
pip install python-exports
```

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

If the module has no `__all__`, it is created.
Otherwise, `__all__` is converted to a list, and the export is appended.

## Caveats

Exporting a function or class directly relies on the `__name__` attribute,
so consider the following example:

```pycon
>>> def eggs():
...     ...
>>> fake_eggs = eggs
```

If we want to export fake_eggs, then this **will not work**:

```pycon
>>> export(fake_eggs)  # BAD: this will add `'eggs'` to `__all__`
```

In such cases, use the name instead:

```pycon
>>> export('fake_eggs')  # GOOD
```

You'll be safe if you either

- decorate a function or a class directly with `@export`,
- pass the name string when using plain `export('...')` calls.
