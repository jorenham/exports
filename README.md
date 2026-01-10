<h1 align="center">@exports</h1>

<p align="center">The DRY alternative to </code>__all__</code></p>

<p align="center">
<a href="https://github.com/jorenham/exports"><img alt="GitHub License" src="https://img.shields.io/github/license/jorenham/exports?style=flat-square&color=121d2f&labelColor=3d444d"></a>
<a href="https://pypi.org/project/python-exports"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/python-exports?style=flat-square&color=121d2f&labelColor=3d444d"></a>
<a href="https://github.com/jorenham/exports"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/python-exports?style=flat-square&color=121d2f&labelColor=3d444d"></a>
<br>
<a href="https://github.com/jorenham/exports"><img alt="Typing" src="https://img.shields.io/pypi/types/python-exports?style=flat-square&color=121d2f&labelColor=3d444d"></a>
<a href="https://detachhead.github.io/basedpyright"><img alt="basedpyright" src="https://img.shields.io/badge/basedpyright-262c36?style=flat-square&logoColor=fdc204"></a>
<a href="https://github.com/python/mypy"><img alt="mypy" src="https://img.shields.io/badge/mypy-262c36?style=flat-square&logo=python"></a>
<a href="https://github.com/facebook/pyrefly"><img alt="pyrefly" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/facebook/pyrefly/refs/heads/main/website/static/badge.json&style=flat-square&color=262c36&labelColor=262c36"></a>
<a href="https://github.com/astral-sh/ty"><img alt="ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json&style=flat-square&color=262c36&labelColor=262c36"></a>
<a href="https://github.com/astral-sh/ruff"><img alt="ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square&color=262c36&labelColor=262c36"></a>
</p>

---

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
