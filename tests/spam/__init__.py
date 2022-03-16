__all__ = ('public_all', )

from exports import export
from .external import external, external as external_alt


def public_all():
    return True


@export
def public_export():
    return True


def private():
    return False


export(external)
export('external_alt')
