__all__ = ('public_all', )

from exports import export
from .external import external, external as external_alt  # pyright: ignore[reportUnusedImport]


def public_all() -> bool:
    return True


@export
def public_export() -> bool:
    return True


def private() -> bool:
    return False


export(external)
export('external_alt')
